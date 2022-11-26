from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
   
    
    @task
    def index(self):
        self.client.get("/")
     
    @task
    def index2(self):
        self.client.get("/home")
    @task
    def login(self):
        self.client.get("/login")
    @task
    def login(self):
        self.client.get("/dashboard")           
    @task
    def login(self):
        self.client.get("/request")
