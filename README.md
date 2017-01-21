# ScalableMachineLearning
Scalable Machine Learning Tutorial

Jay Urbain, PhD

Objectives:  

Lectures (not yet completed)
- Apache Hadoop Environment from Hortonworks  
- Python using the Anaconda Distribution  
- Apache Spark  
- Google’s Tensor Flow  
- Configuring any number of dedicated computers and therefore not those hosted by Amazon AWS, or Google App Engine  

Tutorials and cheat sheets:  

Git: http://rogerdudler.github.io/git-guide/

. = ScalableMachineLearning

1 - ./Anaconda_environment_cheat_sheet.txt
Anaconda download, installation, and setting up development environments.

2 - code/Numpy Pandas Scipy Tutorial.ipynb
Tutorial of using Python numpy, pandas, and scipy packages targeted towards data analysis.

3 - code/Market Data Analysis.ipynb
Jupyter notebook tutorial using stock market to illustrate use of numpy and pandas to analyze waveform/temporal.

4 - code/Pandas JSON.ipynb
Jupyter notebook tutorial using stock market to illustrate storing and retrieving waveform data in JSON format.

5 - ./Hortnonworks_cheat_sheet.txt
Hortonworks download, installation, and references.

6 - ./PySpark_standalone_cheat_sheet.txt
Running Spark standalone on a local machine using PySpark. Very helpful 
for development. No need for VM or running Hadoop cluster.

7 - code/pypark_sql_people_example.py
Python script illustrating reading delimited text or JSON files into Spark RDD, defining dataframe with schema, and execution of basic SQL queries.
Can be run in standalone mode, VM, or cluster.

Data files are assumed to be in ./data

8 - code/Market Data Analysis PySpark.ipynb
Run the Jupyter notebook tutorial using stock market as PySpark Notebook:
export SPARK_HOME=/Users/jayurbain/Dropbox/spark-1.6.2-bin-hadoop2.6
export IPYTHON=1
export PYSPARK_PYTHON=/Applications/anaconda/bin/python3.5
export PYSPARK_DRIVER_PYTHON=ipython3.5
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"

/Users/jayurbain/Dropbox/spark-1.6.2-bin-hadoop2.6/bin/pyspark

9 - Spark-ts (not yet completed)
Spark package for distributed temporal analysis
http://sryza.github.io/spark-timeseries/0.3.0/index.html

10 - Deploying Hadoop to Cloud cluster (not yet completed)

References:

Apache Hadoop
http://hadoop.apache.org/

Spark Overview
http://spark.apache.org/docs/latest/index.html

Spark SQL, DataFrames and Datasets Guide
http://spark.apache.org/docs/latest/sql-programming-guide.html

Learning Spark, O'Reilly
Holden Karau, Andy Konwinski, Patrick Wendell & Matei Zaharia

Hortonworks
http://hortonworks.com/

A New Library for Analyzing Time-Series Data with Apache Spark
December 14, 2015By Sandy Ryza
https://blog.cloudera.com/blog/2015/12/spark-ts-a-new-library-for-analyzing-time-series-data-with-apache-spark/

Python for Financial Data Analysis with pandas
2011, Wes McKinney
Slides: http://www.slideshare.net/wesm/python-for-financial-data-analysis-with-pandas

Multivariate Time Series Analysis: With R and Financial Applications

Machine Learning for Sequential Data: A Review (2002)

Machine Learning Strategies for Time Series Forecasting (2013)


