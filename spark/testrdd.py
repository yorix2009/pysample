# coding: UTF-8
"""
实现基于python的Spark调用
"""
# 一种初始化方法
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
sc = spark.sparkContext

logFile = "input/hadoop/hdfs-site.xml"  # Should be some file on your system
logData = spark.read.text(logFile).cache()
numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

# 读取文件内容RDD处理
line = sc.textFile('input/hadoop/hdfs-site.xml')
line = line.filter(lambda x: 'name' in x)
line.foreach(lambda x: print(x))

spark.stop()
