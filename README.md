# Weather Data Pipeline (Databricks)

## Descripción

Este proyecto implementa un pipeline de datos usando la arquitectura Medallion (Bronze, Silver, Gold) en Databricks.

## Tecnologías

* Databricks
* PySpark
* Delta Lake

## Capas del Pipeline

### Bronze

Ingesta de datos sin transformar, agregando columna ingestion_date.

### Silver

* Limpieza de datos
* Eliminación de nulos
* Conversión de tipos

### Gold

* Promedio de temperatura por ciudad y mes
* Detección de valores extremos

## Automatización

Se configuró un Workflow en Databricks para ejecutar el pipeline.
