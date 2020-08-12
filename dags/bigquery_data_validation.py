from airflow import DAG
from airflow.utils.dates import days_ago

from airflow.operators.bigquery_plugin import (
    BigQueryDataValidationOperator,
    BigQueryDatasetSensor,
)

default_arguments = {"owner": "YOUR-NAME-HERE", "start_date": days_ago(1)}

with DAG(
    "bigquery_data_validation",
    schedule_interval="@daily",
    catchup=False,
    default_args=default_arguments,
    user_defined_macros={"project": "YOUR-PROJECT-NAME-HERE"},
) as dag:

    is_table_empty = BigQueryDataValidationOperator(
        task_id="is_table_empty",
        sql="SELECT COUNT(*) FROM `{{ project }}.vehicle_analytics.history`",
        location="europe-west2",
    )

    dataset_exists = BigQueryDatasetSensor(
        task_id="dataset_exists",
        project_id="{{ project }}",
        dataset_id="vehicle_analytics",
    )

dataset_exists >> is_table_empty
