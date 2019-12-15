from pyspark.sql import SparkSession
from pyspark.sql.types import *

def main():
  spark = SparkSession \
    .builder \
    .appName("words") \
    .master("local[4]") \
    .getOrCreate()

  schema = StructType([
    StructField("word", StringType(), True)
  ])

  df = spark.read.format('csv').schema(schema).load("words.txt")
  df = df.write.format('parquet').save('/tmp/parquet')

main()
