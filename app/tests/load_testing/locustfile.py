import time
from locust import HttpUser, task, between

class UserClass(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/innosoft_days")

    def on_start(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        })