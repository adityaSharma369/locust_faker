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
    @task(1)
    def list(self):
        self.client.post(self.url+"/holiday/list",headers = self.headers)
    @task(2)
    def add(self):
        self.client.post(self.url+"/holiday/add",data=json.dumps({"type":self.fake.name(),"title":self.fake.name(),"comment":"festival","date":"2019-09-30","groups":"5d92e311e78e42009b7d8a5a"}),headers = self.headers)
    @task(2)
    def edit(self):
        self.client.post(self.url+"/holiday/edit",data=json.dumps({"holiday_id":"5d91a2f99ce4e000579eb942","type":"first","title":"last","date":"2019-09-30","role":"admin"}),headers = self.headers)
    @task(2)
    def view(self):
        self.client.post(self.url+"/holiday/view",data=json.dumps({"holiday_id":"5da1a5f8e10b6900309ddf7a"}),headers = self.headers)
    @task(2)
    def delete(self):
        self.client.post(self.url+"/holiday/delete",data=json.dumps({"holiday_id":"5d92df9a9ce4e0008e3e3edc"}),headers = self.headers)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
