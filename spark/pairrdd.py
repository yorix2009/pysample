# coding: UTF-8
from pyspark.sql import SparkSession
import sparklib.sparkutil as sparkutil

"""
"""
spark = SparkSession.builder.master('local').appName("SimpleApp").getOrCreate()
sc = spark.sparkContext
num = 1


def show_title(s):
    global num
    print("=" * 20)
    data = s.split()
    print("{2}.[{0}]{1}".format(data[0], data[1], num))
    print("=" * 20)
    num += 1


def process(data):
    list = data.split()
    return (list[0], list[1:])


# map值对对应的是一个元组，使用filter可以分别对data[0] data[1]进行处理
show_title('map 创建键值对')
rdd = sc.parallelize(["hello world", "just a sample script", "hello china", "just a little"])
sparkutil.show_rdd(rdd)
prdd = rdd.map(process)
sparkutil.show_maprdd(prdd)
# reduceByKey x,y分别对应两个相同key的value结果集
prdd1 = prdd.reduceByKey(lambda x, y: set(x).intersection(set(y)))
sparkutil.show_maprdd(prdd1)
# groupByKey分组合并
# groupByKey() 就会使用RDD 中的键来对数据进行分组。对于一个由类型K 的键和类型V 的值组成的RDD，所得到的结果RDD 类型会是
# [K, Iterable[V]]
# 例如，rdd.reduceByKey(func)与rdd.groupByKey().mapValues(value => value.reduce(func)) 等价
prdd.groupByKey().mapValues(list).sortByKey().foreach(lambda x: print('->', x))
prdd.take(10)
# [('hello', ['world']), ('just', ['a', 'sample', 'script']), ('hello', ['china']), ('just', ['a', 'little'])]
#统计key的值数量
data1 = prdd.countByKey()
# defaultdict(<class 'int'>, {'hello': 2, 'just': 2})
#按照key合并数据，重复的key会被后面的覆盖
prdd.collectAsMap()
# {'hello': ['china'], 'just': ['a', 'little']}
#查找数据集，合并相同key的数据
prdd.lookup('hello')
# [['world'], ['china']]
prdd.lookup('just')
# [['a', 'sample', 'script'], ['a', 'little']]
