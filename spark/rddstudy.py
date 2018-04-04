from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
sc = spark.sparkContext


def show_title(s):
    print("=" * 20)
    print(s)
    print("=" * 20)


data = [x for x in range(100)]
rdd = sc.parallelize(["hello world", "a sample script"])
show_title('filter 过滤')
rdd.filter(lambda x: 'sample' in x).foreach(lambda x: print('->', x))
show_title('map 映射')
rdd1 = rdd.map(lambda x: x.split())
rdd1.foreach(lambda x: print('->', x))
print("\n")
print("数据集=", rdd1.count())
show_title('flatMap 展开map')
rdd2 = rdd.flatMap(lambda x: x.split())
rdd2.foreach(lambda x: print('->', x))
print("数据集=", rdd2.count())
show_title('sample 抽样')
rdd2.sample(False,0.8,8).foreach(lambda x: print('->', x))
show_title('union 合并')
rdd2.sample(False,0.8,8).union(rdd2)