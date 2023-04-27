from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
file_path_1 = '/opt/airflow/dags/testfile.py'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 27),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'exchange_values',
    default_args=default_args,
    description='Exchange the values of x and y every 5 minutes',
    schedule_interval=timedelta(minutes=5),
)

t1 = BashOperator(
    task_id='exchange_values',
    bash_command=f'python {file_path_1}',
    dag=dag,
)

t1
