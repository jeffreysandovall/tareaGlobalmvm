-- Databricks notebook source
CREATE OR REPLACE TABLE gold_weather_summary AS
SELECT
    city,
    date_format(date, 'yyyy-MM') AS month,
    AVG(temperature) AS avg_temperature,
    MAX(temperature) AS max_temperature,
    MIN(temperature) AS min_temperature
FROM silver_weather
GROUP BY city, month;

-- COMMAND ----------

SELECT * FROM gold_weather_summary;

-- COMMAND ----------

SELECT *
FROM silver_weather
WHERE temperature > 30 OR temperature < 15;