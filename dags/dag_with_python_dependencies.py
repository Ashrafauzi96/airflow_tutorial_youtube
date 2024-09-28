from datetime import datetime,timedelta
from airflow import DAG 
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_sklearn():
    import sklearn
    print(f"scikit-learn with version: {sklearn.__version__}")

def get_matplotlib():
    import matplotlib
    print(f"matplotlib hok version: {matplotlib.__version__} , kemah keming")

with DAG(
    dag_id = 'dag_with_python_dependencies_v02',
    default_args=default_args,
    start_date=datetime(2024, 9, 1),
    schedule_interval='@daily'
)as dag:
    task1 = PythonOperator(
        task_id = 'get_sklearn',
        python_callable=get_sklearn
    )

    task2 = PythonOperator(
        task_id = 'get_matplotlib',
        python_callable=get_matplotlib
    )

    task1>>task2