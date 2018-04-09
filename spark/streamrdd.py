# coding: UTF-8
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = SparkSession.builder.appName("StructuredNetworkWordCount").getOrCreate()
lines = spark.readStream.format("socket") \
    .option("host", "localhost").option("port", 9999).load()  # Split the lines into words
words = lines.select(
    explode(
        split(lines.value, " ")
    ).alias("word")
)
wordCounts = words.groupBy("word").count()
query = wordCounts.writeStream.outputMode("complete").format("console").start()

query.awaitTermination()
