from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2023, 5, 1, 0,0,0),
    'owner': 'Airflow'
}

def on_success_dag(dict):
    print("on_success_dag")
    print(dict)

def on_failed_dag(dict):
    print("on_failure_dag")
    print(dict)
    
with DAG(
    dag_id='alert_dag',
    schedule_interval="0 0 * * *",
    default_args=default_args,
    catchup=True, dagrun_timeout=timedelta(seconds=5),
    on_success_callback=on_success_dag,
    on_failure_callback=on_failed_dag) as dag:
    
    # Task 1
    t1 = BashOperator(task_id='t1', bash_command="echo 'Hello there!' && sleep 10 && echo 'Oops! I fell asleep for a couple seconds!'")
    # t1 = BashOperator(task_id='t1', bash_command="exit 1")
    
    # Task 2
    t2 = BashOperator(task_id='t2', bash_command="echo 'second task'")

    t1 >> t2