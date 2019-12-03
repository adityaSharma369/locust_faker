from locust import HttpLocust, TaskSet, task
import random
import string
import json
from faker import Faker

class UserBehavior(TaskSet):
    # url = "http://testapi.teric.ai:3500"
    url = "http://192.168.0.113:3500"
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjVkNGQ5MzFkOWIwNzYzMDAyYjdlZjFhYiIsImVtYWlsIjoiZHNAdGVyaWNzb2Z0LmNvbSIsImV4cCI6MTU2NTk1NzY5OSwibmFtZSI6InRlc3QxIiwicGhvbmUiOiI5OTk5OTk5OTk5Iiwicm9sZSI6ImRhdGFzY2llbnRpc3QifX0.4lnvBT8r3GMLcEx989MS5Rbaj3QO-BuCj1s9k1hWvZw"
    faker = Faker()

    headers = {
        # "X-Requested-With": "XMLHttpRequest",
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        
        "Content-Type": "application/json",
        "Authorization": "Bearer"+token
    }
    def randomString(stringLength=10):
        """Generate a random string of fixed length """
        
    # def on_start(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     self.login()

    # def on_stop(self): 
    #     """ on_stop is called when the TaskSet is stopping """
    #     self.logout()

    # def login(self):
    #     self.client.post(self.url+"/account/login", {"username":"ds@tericsoft.com", "password":"123456"})

    # def logout(self):
    #     self.client.post(self.url+"/account/logout")
    @task(1)
    def list(self):
        self.client.get(self.url+"/account/checklogin",headers = self.headers)

    @task(2)
    def list(self):
        self.client.post(self.url+"/project/list",headers = self.headers)
    
    @task(1)
    def add(self):
        rand = self.randomString()
        self.client.post(self.url+"/project/add",data=json.dumps({"title":{faker.name()}, "classes":"dog", "classes":"cat" ,"description":"bla bla bka"}),headers = self.headers)
    @task(2)
    def delete(self):
        self.client.post(self.url+"/project/delete",data=json.dumps({"project_id":"5d4d506ededf08044f0d1dac"}),headers = self.headers)
    @task(2)
    def edit(self):
        self.client.post(self.url+"/project/edit",data=json.dumps({"project_id":"5d4d506ededf08044f0d1dac","title":"the indian dogs","Description":"dogs aalso feel pain"}),headers = self.headers)
    @task(2)
    def view(self):
        self.client.post(self.url+"/project/view",data=json.dumps({"project_id":"5d52aed2200ad30054ac055c"}),headers = self.headers)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
