#  (Databricks)

## Descripción

Este proyecto implementa un pipeline de datos utilizando la arquitectura Medallion (Bronze, Silver, Gold) en Databricks. El objetivo es procesar datos meteorológicos desde su estado crudo hasta generar métricas listas para análisis.

## Tecnologías utilizadas

* Databricks
* PySpark
* Delta Lake

## Arquitectura del Pipeline

### 🟤 Bronze

* Ingesta de datos sin transformar
* Preservación del dato original
* Adición de la columna `ingestion_date`

### ⚪ Silver

* Limpieza de datos
* Eliminación de valores nulos
* Conversión de tipos de datos (string → timestamp, numeric)

### 🟡 Gold

* Cálculo de métricas agregadas
* Promedio de temperatura por ciudad y mes
* Identificación de condiciones climáticas extremas

## Automatización

Se configuró un Workflow en Databricks para ejecutar el pipeline de forma secuencial (Bronze → Silver → Gold).

## Resultado

El pipeline permite transformar datos crudos en información estructurada y lista para análisis, siguiendo buenas prácticas de ingeniería de datos.

