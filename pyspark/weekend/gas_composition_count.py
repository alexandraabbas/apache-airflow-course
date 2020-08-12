#!/usr/bin/python
from pyspark.sql import SparkSession

spark = SparkSession \
  .builder \
  .master('yarn') \
  .appName('bigquery-analytics-gas-composition-count') \
  .getOrCreate()

bucket = 'YOUR-BUCKET-NAME-HERE'
spark.conf.set('temporaryGcsBucket', bucket)

history = spark.read.format('bigquery') \
  .option('table', 'vehicle_analytics.history') \
  .load()
history.createOrReplaceTempView('history')

gas_composition_count = spark.sql(
    'SELECT vehicle_id, date, COUNT(DISTINCT gas_composition) AS gas_composition_count FROM history GROUP BY vehicle_id, date'
)
gas_composition_count.show()
gas_composition_count.printSchema()

gas_composition_count.write.format('bigquery') \
    .option('table', 'vehicle_analytics.gas_composition_count') \
    .mode('append') \
    .save()
