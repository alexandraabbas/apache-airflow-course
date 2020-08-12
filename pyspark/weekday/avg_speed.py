#!/usr/bin/python
from pyspark.sql import SparkSession

spark = SparkSession \
  .builder \
  .master('yarn') \
  .appName('bigquery-analytics-avg-speed') \
  .getOrCreate()

bucket = 'YOUR-BUCKET-NAME-HERE'
spark.conf.set('temporaryGcsBucket', bucket)

history = spark.read.format('bigquery') \
  .option('table', 'vehicle_analytics.history') \
  .load()
history.createOrReplaceTempView('history')

avg_speed = spark.sql(
    'SELECT vehicle_id, date, AVG(speed) AS avg_speed FROM history GROUP BY vehicle_id, date'
)
avg_speed.show()
avg_speed.printSchema()

avg_speed.write.format('bigquery') \
    .option('table', 'vehicle_analytics.avg_speed') \
    .mode('append') \
    .save()
