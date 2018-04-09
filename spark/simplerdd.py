# coding: UTF-8
from pyspark.sql import SparkSession
"""
pyspark调用代码测试
==================
默认使用local模式运行，同时可以指定远程的spark配置
"""
spark = SparkSession.builder.master('local').appName("SimpleApp").getOrCreate()
sc = spark.sparkContext

num=1
def show_title(s):
    global num
    print("=" * 20)
    data=s.split()
    print("{2}.[{0}]{1}".format(data[0],data[1],num))
    print("=" * 20)
    num+=1


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
rdd2.sample(False, 0.8, 8).foreach(lambda x: print('->', x))

show_title('union 合并')
res=rdd2.sample(False, 0.8, 8).union(rdd2)
res.foreach(lambda  x:print('->',x))
