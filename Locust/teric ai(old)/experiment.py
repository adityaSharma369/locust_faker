from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    # url = "http://testapi.teric.ai:3500"
    url = "http://3.0.102.169:3500"
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjVkNGQ5MzFkOWIwNzYzMDAyYjdlZjFhYiIsImVtYWlsIjoiZHNAdGVyaWNzb2Z0LmNvbSIsImV4cCI6MTU2NTk1NzY5OSwibmFtZSI6InRlc3QxIiwicGhvbmUiOiI5OTk5OTk5OTk5Iiwicm9sZSI6ImRhdGFzY2llbnRpc3QifX0.4lnvBT8r3GMLcEx989MS5Rbaj3QO-BuCj1s9k1hWvZw"
    
    headers = {
        # "X-Requested-With": "XMLHttpRequest",
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        
        "Content-Type": "application/json",
        "Authorization": "Bearer"+token
    }
    # def on_start(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     self.login()

    # # def on_stop(self):
    # #     """ on_stop is called when the TaskSet is stopping """
    # #     self.logout()

    # def login(self):
    #     self.client.post(self.url+"/account/login", {"username":"ds@tericsoft.com", "password":"123456"})

    # # def logout(self):
    # #     self.client.post(self.url+"/account/logout")

    @task(1)
    def list(self):
        self.client.post(self.url+"/experiment/list",headers = self.headers)
    @task(2)
    def add(self):
        self.client.post(self.url+"/experiment/add",data=json.dumps({"problem_type":"detection","title":"the indian animals","classes":"dog","classes":"cat","project_id":"5d4d201e4b2de10062873816"}),headers = self.headers)
    @task(2)
    def delete(self):
        self.client.post(self.url+"/experiment/delete",data=data=json.dumps({"experiment_id":"5d4d506ededf08044f0d1dac"}),headers = self.headers)
    @task(2)
    def edit(self):
        self.client.post(self.url+"/experiment/edit",data=json.dumps({"experiment_id":"5d4d201e4b2de10062873816","title":"the indian dogs","Description":"dogs aalso feel pain"}),headers = self.headers)
    @task(2)
    def view(self):
        self.client.post(self.url+"/experiment/view",data=json.dumps({"experiment_id":"5d4d201e4b2de10062873816"}),headers = self.headers)
    @task(2)
    def images(self):
        self.client.post(self.url+"/experiment/images",data=json.dumps({"experiment_id":"5d4d201e4b2de10062873816","width":500}),headers = self.headers)
    @task(2)
    def deleteImage(self):
        self.client.post(self.url+"/experiment/deleteImage",data=json.dumps({"image_id":"5d4ba9fac078d5002e2d8fa0"}),headers = self.headers)
    @task(2)
    def classlist(self):
        self.client.post(self.url+"/experiment/class/list",data=json.dumps({"experiment_id":"5d4579b72aec66002e94889c"}),headers = self.headers)
    @task(2)
    def classadd(self):
        self.client.post(self.url+"/experiment/class/add",data=json.dumps({"experiment_id":"5d274375fedb96032b527d2f","name":"Iam ironman"}),headers = self.headers)
    @task(2)
    def classdelete(self):
        self.client.post(self.url+"/experiment/class/delete",data=json.dumps({"class_id":"5d274375fedb96032b527d2f"}),headers = self.headers)
    @task(2)
    def history(self):
        self.client.post(self.url+"/experiment/history",data=json.dumps({"experiment_id":"5d4ba98ec078d5002e2d8f98","source":"machine"}),headers = self.headers)
    @task(2)
    def exportAnnotations(self):
        self.client.post(self.url+"/experiment/exportAnnotations",data=json.dumps({"experiment_id":"5d4c790452d579002c58fbd2","train_ratio":50,"export_format":"ssd"}),headers = self.headers)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
