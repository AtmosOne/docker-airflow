"""
I want to pass connection to Airflow as environment variable.
But i can't list it in Airflow UI.
From stack overflow guys recommend to test it in DAG:
https://stackoverflow.com/questions/59669390/airflow-connection-is-not-being-created-when-using-environment-variables

So, let's check it out:
"""
import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.models import Connection


default_args = {
    "owner": "Adil",
    "depends_on_past": False,
    "start_date": datetime(2015, 6, 1),
    "email": ["adil.rashitov.98@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

def print_connection():
    conn = os.getenv('AIRFLOW_CONN_TEST_CONNECTION')
    print(f"CONNECTION YOUU WANT IS: {conn}")

def print_hello():
    print(f"Hello world")

dag = DAG("test_connection", default_args=default_args, schedule_interval=timedelta(1))


t1 = PythonOperator(task_id='print_connection',
                    python_callable=print_connection,
                    dag=dag)

t2 = PythonOperator(task_id='print_hello',
                    python_callable=print_hello,
                    dag=dag)


t1 >> t2
"""
SUMMARY: as a way to manage connections, simlpy pass to AIRFLOW env vars and get them)
BONUS: They won't shown in your UI
"""
