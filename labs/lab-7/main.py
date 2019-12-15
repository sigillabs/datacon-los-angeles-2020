from pyspark.sql import SparkSession
from pyspark.sql.types import *
from mine import killer

def main():
  """
  Fill in this function.

  1. Write a function in a separate file that will be used in a DataFrame map operation.
  2. Create a dataframe with words.
  3. Use function for map operation.

  NOTE: Use Lambdas over new functions.
  NOTE: Use context.read.format('parquet').load(...) to read a parquet file.
  NOTE: Make sure standalone spark cluster is running.

  See https://spark.apache.org/docs/latest/sql-getting-started.html for help.
  See https://spark.apache.org/docs/2.1.0/api/python/pyspark.sql.html for help.
  See https://spark.apache.org/docs/latest/spark-standalone.html for help.
  """

  spark = SparkSession \
    .builder \
    .appName("words") \
    .master("spark://127.0.1.1:7077") \
    .getOrCreate()

  # Fill in here

main()
