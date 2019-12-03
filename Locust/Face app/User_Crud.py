from locust import HttpLocust, TaskSet, task
import random
import string
import json
from faker import Faker 
from random import randint

class UserBehavior(TaskSet):
    url = "http://13.250.2.214:3500"
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjVkOTBmZmUyMzFkNDc2MDYwMGExOTg4MiIsImVtYWlsIjoibWFuYWdlckB0ZXJpY3NvZnQuY29tIiwiZXhwIjoxNTcxMzk2MTA2LCJmaXJzdF9uYW1lIjoiRGVmYXVsdCBVc2VyIiwibGFzdF9uYW1lIjoiIiwicGhvbmUiOiIwMDAwMDAwMDAwIiwicm9sZSI6Im1hbmFnZXIifX0.ssl0pv0KKD95y-llg8dY8Jkm7PKQP0pUCHShDU4rAok"
    fake = Faker()

    headers = {
        # "X-Requested-With": "XMLHttpRequest",
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        
        "Content-Type": "application/json",
        "Authorization": "Bearer "+token
    }
    @task(2)
    def listlite(self):
        self.client.post(self.url+"/user/listLite",headers = self.headers)
    
    @task(1)
    def list(self):
        self.client.post(self.url+"/user/list",headers = self.headers)
    @task(2)
    def add(self):
        self.client.post(self.url+"/user/add",data=json.dumps({"first_name":self.fake.name(),"last_name":self.fake.name(),"email":self.fake.email(),"password":"123456","phone":self.fake.random_int(9000000000,9999999999),"role":"admin"}),headers = self.headers)
    @task(2)
    def edit(self):
        self.client.post(self.url+"/user/edit",data=json.dumps({"user_id":"5d91a2f99ce4e000579eb942","first_name":"first","last_name":"last","email":"email@gmail.com","password":"123456","phone":"9012345678","role":"admin","is_active":"true"}),headers = self.headers)
    @task(2)
    def view(self):
        self.client.post(self.url+"/user/view",data=json.dumps({"user_id":"5da1a5f8e10b6900309ddf7a"}),headers = self.headers)
    @task(2)
    def delete(self):
        self.client.post(self.url+"/user/delete",data=json.dumps({"user_id":"5d92df9a9ce4e0008e3e3edc"}),headers = self.headers)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
