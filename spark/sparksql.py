# coding: UTF-8
from pyspark.sql import SparkSession
from pyspark.sql import Row
import os

spark = SparkSession.builder.appName("SimpleSqlApp").getOrCreate()
sc = spark.sparkContext

filename = os.environ['HOME']+"/hadoop/spark-2.3.0/bank.csv"
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

result1 = result.rdd.map(lambda p: "Name: " + p.name).collect()
for name in result1:
    print(name)
spark.stop()
