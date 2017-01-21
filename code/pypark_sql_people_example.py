
cd into working directory


######################################

# experiment with JSON

from pyspark.sql import SQLContext
from pyspark.sql.types import *

sqlContext = SQLContext(sc)

people = sqlContext.read.json("people.json")

# Displays the content of the DataFrame to stdout
people.show()

fields = [StructField("name", StringType(), True),
	StructField("age", IntegerType(), True)]
schemaPeople = StructType(fields)

# Apply the schema to the RDD.
schemaPeople = sqlContext.createDataFrame(people, schemaPeople)

schemaPeople.printSchema()

# Register the DataFrame as a table.
schemaPeople.registerTempTable("people")

# SQL can be run over DataFrames that have been registered as a table.
results = sqlContext.sql("SELECT name, age FROM people")

# The results of SQL queries are RDDs and support all the normal RDD operations.
names = results.map(lambda p: "Name: " + p.name + " Age: " + p.age)
for name in names.collect():
  print(name)


######################################

# experiment with CSV

# Import SQLContext and data types
from pyspark.sql import SQLContext
from pyspark.sql.types import *

# sc is an existing SparkContext.
sqlContext = SQLContext(sc)

# Load a text file and convert each line to a tuple.
lines = sc.textFile("hdfs:///user//maria_dev//data//peopleheader.txt")
parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p: (p[0], int(p[1].strip()) ) )

# The schema is encoded in a string.
#schemaString = "name age"

#fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
#schema = StructType(fields)

fields = [StructField("name", StringType(), True),
	StructField("age", IntegerType(), True)]
schema = StructType(fields)

# Apply the schema to the RDD.
schemaPeople = sqlContext.createDataFrame(people, schema)

schemaPeople.printSchema()

# Register the DataFrame as a table.
schemaPeople.registerTempTable("people")

# SQL can be run over DataFrames that have been registered as a table.
results = sqlContext.sql("SELECT name, age FROM people")

# The results of SQL queries are RDDs and support all the normal RDD operations.
names = results.map(lambda p: "Name: " + p.name + " Age: " + str(p.age))
for name in names.collect():
  print(name)