# Databricks notebook source
from pyspark.sql.functions import current_timestamp


data = [
    ("Bogota", "2024-01-01", 18),
    ("Bogota", "2024-01-02", 17),
    ("Medellin", "2024-01-01", 25),
    ("Medellin", "2024-01-02", 27),
    ("Cali", "2024-01-01", 30),
    ("Cali", "2024-01-02", 32)
]

columns = ["city", "date", "temperature"]

df = spark.createDataFrame(data, columns)


df = df.withColumn("ingestion_date", current_timestamp())


df.write.format("delta").mode("overwrite").saveAsTable("bronze_weather")

# COMMAND ----------

spark.table("bronze_weather").show()