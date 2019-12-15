from pyspark.sql import SparkSession
from pyspark.sql.types import *

def distinct_words(df):
  df = df.select(df['word'])
  df = df.distinct()
  return df

