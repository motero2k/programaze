import time
from locust import HttpUser, task, between

fake_proposal = {
    "description": "charla sobre el futuro del mercado laboral con la IA",
    "subject": "IA",
    "proposal_type": "CHARLA",
    "state": "ENDIENTE DE ADMISIÓN",
    "innosoft_day_id":1,
    "user_id":1
}

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
   
    
class ProposalClass(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        })
   
    @task
    def view_all_proposals(self):
         self.client.get("/innosoft_days/1/proposals")
    
    @task
    def create_gamer(self):
        self.client.post("/innosoft_days/1/proposal/create/", json=fake_proposal)
    @task
    def view_proposals_details(self):
        self.client.get("/proposal/view/1")