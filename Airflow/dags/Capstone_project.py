from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries

AWS_KEY = os.environ.get('AWS_KEY')
AWS_SECRET = os.environ.get('AWS_SECRET')

default_args = {
    'owner': 'Capstone_project',
    'start_date': datetime(2020, 1, 30),
    'depends_on_pasr': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'Catchup': False,
    'email_on_retry': False
    
}

dag = DAG('capstone_project',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          schedule_interval='0 * * * *'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

stage_flights_to_redshift = StageToRedshiftOperator(
    task_id='Stage_flights',
    dag=dag,
    table="public.staging_flights",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="capstone-dend",
    s3_key="/flights_data/",
    file_type="csv"
)

stage_airlines_to_redshift = StageToRedshiftOperator(
    task_id='Stage_airlines',
    dag=dag,
    table="public.staging_airlines",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="capstone-dend",
    s3_key="/airlines_data/",
    file_type="csv"
)

stage_airports_to_redshift = StageToRedshiftOperator(
    task_id='Stage_airports',
    dag=dag,
    table="public.staging_airports",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="capstone-dend",
    s3_key="/airports_data/",
    file_type="csv"
)

stage_cities_to_redshift = StageToRedshiftOperator(
    task_id='Stage_cities',
    dag=dag,
    table="public.staging_cities",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="capstone-dend",
    s3_key="/cities_data/",
    file_type="csv"
)

load_flights_table = LoadFactOperator(
    task_id='Load_flights_fact_table',
    dag=dag,
    redshift_conn_id="redshift",
    sql_insert= sql_queries.flights_table_insert
)

load_airlines_dimension_table = LoadDimensionOperator(
    task_id='airlines',
    dag=dag,
    redshift_conn_id="redshift",
    sql_insert= sql_queries.airlines_table_insert
)

load_airports_dimension_table = LoadDimensionOperator(
    task_id='Load_airports_dim_table',
    dag=dag,
    redshift_conn_id="redshift",
    sql_insert= sql_queries.airports_table_insert
)

load_cities_dimension_table = LoadDimensionOperator(
    task_id='Load_cities_dim_table',
    dag=dag,
    redshift_conn_id="redshift",
    sql_insert= sql_queries.cities_table_insert
)



run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    tables= ['public.flights', 'public.airlines', 'public.airports', 'public.cities'],
    redshift_conn_id="redshift"
    
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> stage_flights_to_redshift
start_operator >> stage_airlines_to_redshift
start_operator >> stage_airports_to_redshift
start_operator >> stage_cities_to_redshift

stage_flights_to_redshift >> load_flights_table 
stage_airlines_to_redshift >> load_flights_table
stage_airports_to_redshift >> load_flights_table
stage_cities_to_redshift >> load_flights_table

load_flights_table >> load_airlines_dimension_table
load_flights_table >> load_airports_dimension_table
load_flights_table >> load_cities_dimension_table

load_airlines_dimension_table >> run_quality_checks
load_airports_dimension_table >> run_quality_checks
load_cities_dimension_table >> run_quality_checks

run_quality_checks >> end_operator
