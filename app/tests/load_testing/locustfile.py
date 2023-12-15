import time
from locust import HttpUser, task, between

fake_proposal = {
    "description": "charla sobre el futuro del mercado laboral con la IA",
    "subject": "IA",
    "proposal_type": "CHARLA",
    "state": "PENDIENTE DE ADMISIÓN",
    "innosoft_day_id":1,
    "user_id":1
}

fake_token_request ={
    "num_token":1,
    "description":"Quiero hacer una competición de mario coches"
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
    
    def on_stop(self):
        self.client.get("/logout")
    
class TokenRequestClass(HttpUser):
    wait_time = between(1, 5)
    
    def on_start(self):
        self.client.post("/login",data={
            "username":"alumno1",
            "password":"alumno1"
        })
    
    @task
    def create_token_request(self):
        self.client.post("/token_request/create",json=fake_token_request)
   
    @task
    def view_all_token_request(self):
         self.client.get("/token_request/all")
    
    @task
    def view_PENDING_OF_ACEPTATION_token(self):
        self.client.get("/token_request/all?state=PENDING_OF_ACEPTATION")
        
    @task
    def view_ACCEPTED_token(self):
        self.client.get("/token_request/all?state=ACCEPTED")
        
    @task
    def view_ACCEPTED_token(self):
        self.client.get("/token_request/all?state=REJECTED")
    
    
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
        
class VotationClass(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        })
        
    @task
    def view_all_votations(self):
         self.client.get("/innosoft_days/2/votations")
         
    @task
    def view_IN_PROGRESS_votations(self):
         self.client.get("/innosoft_days/2/votations/?state=IN_PROGRESS")
         
    @task
    def view_ACCEPTED_votations(self):
         self.client.get("/innosoft_days/2/votations/?state=ACCEPTED")
    
    @task
    def view_REJECTED_votations(self):
         self.client.get("/innosoft_days/2/votations/?state=REJECTED")
