from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='dag_with_taskflow_api_v04',
     default_args=default_args,
     start_date=datetime(2021, 10, 26),
     schedule_interval=('@daily'))
def hello_world_etl():
    

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jerry',
            'last_name' : 'fauzi'
        }
    
    @task()
    def get_age():
        return 19
    
    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World!, MY name is {first_name} {last_name}"
              f"and i am {age} years old!")
        
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],
        last_name=name_dict['last_name'],
        age=age)

greet_dag123 = hello_world_etl()