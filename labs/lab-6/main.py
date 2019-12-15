from pyspark.sql import SparkSession

def main():
  """
  Fill in this function.

  1. Read words.parquet into a DataFrame.
  2. Count the number of partitions in the DataFrame.
  3. Select the word column and filter for “joy”.
  4. Count again.

  NOTE: Use Lambdas over new functions.
  NOTE: Use context.read.format('parquet').load(...) to read a parquet file.

  See https://spark.apache.org/docs/latest/sql-getting-started.html for help.
  See https://spark.apache.org/docs/2.1.0/api/python/pyspark.sql.html for help.
  """

  spark = SparkSession \
    .builder \
    .appName("words") \
    .master("local[4]") \
    .getOrCreate()

  df = spark.read.format('parquet').load("words.parquet")
  print(df.rdd.getNumPartitions())
  df = df.select('word').where('word = "joy"')
  print(df.rdd.getNumPartitions())

main()
