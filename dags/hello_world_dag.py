from airflow.sdk import dag, task
import pendulum

@dag(
    schedule=None,
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
)
def hello_world_dag():
    @task()
    def say_hello():
        print("Hello from Airflow!")

    say_hello()

hello_world_dag()