from pyspark.sql import SparkSession
from pyspark.sql.types import *
import mine

def main():
  """
  Fill in this function.

  1. Write a function in a separate file that will be used in a DataFrame map operation.
  2. Create a dataframe with words.
  3. Use function for map operation.

  NOTE: Use Lambdas over new functions.
  NOTE: Use context.read.format('parquet').load(...) to read a parquet file.

  See https://spark.apache.org/docs/latest/sql-getting-started.html for help.
  See https://spark.apache.org/docs/2.1.0/api/python/pyspark.sql.html for help.

  Try spark-submit :)
  """

  spark = SparkSession \
    .builder \
    .appName("words") \
    .master("local[4]") \
    .getOrCreate()

  # Fill in here

main()
