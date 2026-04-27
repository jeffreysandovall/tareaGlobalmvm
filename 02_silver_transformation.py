# Databricks notebook source
from pyspark.sql.functions import col, to_timestamp

df = spark.table("bronze_weather")

df_clean = df.dropna()

df_clean = df_clean.withColumn(
    "date",
    to_timestamp(col("date"), "yyyy-MM-dd")
)

df_clean = df_clean.withColumn(
    "temperature",
    col("temperature").cast("double")
)

df_clean = df_clean.filter(col("temperature").isNotNull())

df_clean.write.format("delta").mode("overwrite").saveAsTable("silver_weather")

# COMMAND ----------

spark.table("silver_weather").show()