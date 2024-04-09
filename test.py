from sessionCreation import *

# Spark session created.
spark = sparkSession()

l1 = [(1,),(2,),(3,),(4,)]
cols = ['id']

# Generate the data in the file
genearateInputFile(l1,cols)

df = spark.read.format('csv').option('header','true') \
                             .option('inferSchema','true') \
                             .load('C:/Users/LENOVO/AWSBootCamp/AWSBootCamp/Practice-00/input.csv')

df.show()

