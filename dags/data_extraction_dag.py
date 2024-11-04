from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from utils.extraction.mainExtraction import *

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'data_extraction_dag',
    default_args=default_args,
    description='A DAG for automated football data extraction',
    schedule_interval=timedelta(days=1), 
    start_date=datetime(2024, 11, 1), 
    catchup=False,
) as dag:

    basic_stats_task = PythonOperator(
        task_id='basic_stats_extraction',
        python_callable=basic_stats_scrape,
    )

    GK_stats_task = PythonOperator(
        task_id='GK_stats_extraction',
        python_callable=GK_stats_scrape,
    )

    GK_adv_stats_task = PythonOperator(
        task_id='GK_adv_stats_extraction',
        python_callable=GK_adv_stats_scrape,
    )

    shooting_stats_task = PythonOperator(
        task_id='shooting_stats_extraction',
        python_callable=Shooting_stats_scrape,
    )

    passing_stats_task = PythonOperator(
        task_id='passing_stats_extraction',
        python_callable=Passing_stats_scrape,
    )

    pass_types_task = PythonOperator(
        task_id='pass_types_extraction',
        python_callable=PassTypes_stats_scrape,
    )

    goal_shot_creation_task = PythonOperator(
        task_id='goal_shot_creation_extraction',
        python_callable=Goal_ShotCreation_stats_scrape,
    )

    def_actions_task = PythonOperator(
        task_id='defensive_actions_extraction',
        python_callable=DefActions_stats_scrape,
    )

    possession_stats_task = PythonOperator(
        task_id='possession_stats_extraction',
        python_callable=Possession_stats_scrape,
    )

    playing_time_task = PythonOperator(
        task_id='playing_time_extraction',
        python_callable=PlayingTime_stats_scrape,
    )

    misc_stats_task = PythonOperator(
        task_id='misc_stats_extraction',
        python_callable=Misc_stats_scrape,
    )

    [
        basic_stats_task,
        GK_stats_task,
        GK_adv_stats_task,
        shooting_stats_task,
        passing_stats_task,
        pass_types_task,
        goal_shot_creation_task,
        def_actions_task,
        possession_stats_task,
        playing_time_task,
        misc_stats_task,
    ]