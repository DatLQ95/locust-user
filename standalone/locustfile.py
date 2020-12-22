import time
from locust import HttpUser, task, Locust, TaskSet
from locust import LoadTestShape

class OdooUser(HttpUser):
    @task(1)
    def hello_world(self):
        self.client.get("/")
    @task(2)
    def view_item(self):
        self.client.get("/")

    def on_start(self):
        self.client.get("")
    

class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.
    Keyword arguments:
        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage
        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"duration": 60, "users": 12, "spawn_rate": 10},
        {"duration": 100, "users": 60, "spawn_rate": 50},
        {"duration": 180, "users": 40, "spawn_rate": 10},
        {"duration": 220, "users": 20, "spawn_rate": 10},
        {"duration": 230, "users": 8, "spawn_rate": 10}, 
        {"duration": 240, "users": 4, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None