#!/usr/bin/python
from pyspark.sql import SparkSession

spark = SparkSession \
  .builder \
  .master('yarn') \
  .appName('bigquery-analytics-avg-temperature') \
  .getOrCreate()

bucket = 'YOUR-BUCKET-NAME-HERE'
spark.conf.set('temporaryGcsBucket', bucket)

history = spark.read.format('bigquery') \
  .option('table', 'vehicle_analytics.history') \
  .load()
history.createOrReplaceTempView('history')

avg_temperature = spark.sql(
    'SELECT vehicle_id, date, AVG(temperature) AS avg_temperature FROM history GROUP BY vehicle_id, date'
)
avg_temperature.show()
avg_temperature.printSchema()

avg_temperature.write.format('bigquery') \
    .option('table', 'vehicle_analytics.avg_temperature') \
    .mode('append') \
    .save()
