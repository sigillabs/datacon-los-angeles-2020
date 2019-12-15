from pyspark import SparkConf, SparkContext

def main():
  """
  Fill in this function.

  1. Read the file /home/dataconla2020/tutorial/labs/lab-4/words.txt into an RDD.
  2. Print the count of the number of words in the RDD.
  3. Filter the RDD for 'aardvark'.
  4. Print the count of the number words of words in the RDD.

  NOTE: Use Lambdas over new functions.

  See https://spark.apache.org/docs/latest/rdd-programming-guide.html for help.
  """

  conf = SparkConf().setAppName("words").setMaster("local[4]")
  context = SparkContext(conf=conf)

  # Fill in here

main()
