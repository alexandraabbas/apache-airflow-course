#!/usr/bin/python
from pyspark.sql import SparkSession

spark = SparkSession \
  .builder \
  .master('yarn') \
  .appName('bigquery-analytics-avg-tire-pressure') \
  .getOrCreate()

bucket = 'YOUR-BUCKET-NAME-HERE'
spark.conf.set('temporaryGcsBucket', bucket)

history = spark.read.format('bigquery') \
  .option('table', 'vehicle_analytics.history') \
  .load()
history.createOrReplaceTempView('history')

avg_tire_pressure = spark.sql(
    'SELECT vehicle_id, date, AVG(tire_pressure) AS avg_tire_pressure FROM history GROUP BY vehicle_id, date'
)
avg_tire_pressure.show()
avg_tire_pressure.printSchema()

avg_tire_pressure.write.format('bigquery') \
    .option('table', 'vehicle_analytics.avg_tire_pressure') \
    .mode('append') \
    .save()
