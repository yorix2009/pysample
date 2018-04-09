# coding: UTF-8
from pyspark.sql import SparkSession
from pyspark.sql import Row
import pyspark.sql.types as types
import os


# 手工处理数据，配套响应的schema，然后使用sql查询
# 需要启动hdfs
def load_csv_with_schema():
    spark = SparkSession.builder.appName("SimpleSqlApp").getOrCreate()
    sc = spark.sparkContext

    filename = os.environ['HOME'] + "/hadoop/spark-2.3.0/bank.csv"
    with open(filename) as f:
        data = f.read()
    # print(data)
    bankRDD = sc.parallelize(data.split("\n"))
    bankRDD = bankRDD.map(lambda s: s.split(";")).filter(lambda x: x[0] != '"age"' and x[0] != '')
    print("RDD 记录数=", bankRDD.count())
    # bankRDD.foreach(lambda  x:print('->',x))
    # map转换为一条记录表
    # 使用Row对象将需要的字段映射为数据库表字段
    # 下面也是一种可选的方法用来构建schema
    # schemaString = "name age"
    #
    # fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
    # schema = StructType(fields)
    #
    # # Apply the schema to the RDD.
    # schemaPeople = spark.createDataFrame(people, schema)
    bankRDD = bankRDD.map(lambda s: Row(age=int(s[0]), job=s[1].replace('"', ''), marital=s[2].replace('"', ''),
                                        education=s[3].replace('"', ''), balance=int(s[5])))
    print('开始创建dataframe')
    schemaBank = spark.createDataFrame(bankRDD)
    schemaBank.createTempView("bank")
    # schemaBank.createOrReplaceTempView("bank")
    # 查询方法，同时也可以支持schemaBank.where("age=40").show()
    # 这样就是一个连环操作，可以不断的使用的dataframe
    # schemaBank.filter("age>40").groupBy("age").count().show()
    # schemaBank.filter("age=40").show()
    result = spark.sql("SELECT * from bank where age=40")
    print("SQL查询结果=", result.rdd.count())
    result.rdd.foreach(lambda x: print(x))
    spark.sql("SELECT * from bank where age>40").show()
    spark.stop()


def load_csv_as_table():
    spark = SparkSession.builder.appName("SimpleSqlApp").getOrCreate()
    filename = os.environ['HOME'] + "/hadoop/spark-2.3.0/bank.csv"
    schema = types.StructType()
    schema.add("age", types.IntegerType(), True)
    schema.add("job", types.StringType(), True)
    schema.add("marital", types.StringType(), True)
    schema.add("education", types.StringType(), True)
    schema.add("default", types.StringType(), True)
    schema.add("balance", types.IntegerType(), True)
    df = spark.read.csv(path='file://' + filename, schema=schema, sep=';', encoding='utf-8', header=True,
                        inferSchema=False)
    df.printSchema()
    df.show()
    df.filter("age=30").orderBy(df.balance.desc()).show()
    df.select("age", "job", "balance").summary('count', 'min', 'max').show()

#需要安装jdbc驱动到spark目录，然后调用sql
def load_jdbc_mysql():
    spark = SparkSession.builder.appName("SimpleSqlApp").getOrCreate()
    url='jdbc:mysql://192.168.7.13:3306/shbiot2?useUnicode=true&characterEncoding=UTF-8'
    prop={}
    prop['user']='root'
    prop['password']=''
    df=spark.read.jdbc(url=url,table='judp_user',properties=prop)
    #df.show()
    df.filter("user_account='admin'").select("user_fullname","user_account").show()


if __name__ == '__main__':
    load_jdbc_mysql()
