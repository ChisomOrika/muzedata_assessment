from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Define the file paths for the two Python scripts
file_path_1 = '/opt/airflow/dags/test_save_csv.py'
file_path_2 = '/opt/airflow/dags/test_check_csv.py'

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 27),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'exchange_values_save_csv',
    default_args=default_args,
    description='Exchange the values of x and y every 5 minutes',
    schedule_interval=timedelta(minutes=5),
)

# Define the BashOperator for task 1, which runs the Python script that saves output to a CSV file
t1 = BashOperator(
    task_id='exchange_values',
    bash_command=f'python {file_path_1}',
    dag=dag,
)

# Define the BashOperator for task 2, which runs the Python script that checks if the CSV file is saved
t2 = BashOperator(
    task_id='check_csv_file',
    bash_command=f'python {file_path_2}',
    dag=dag,
)

# Set the dependency between tasks, so that task 2 runs after task 1 completes
t1 >> t2
