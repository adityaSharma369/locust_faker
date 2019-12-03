from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    # url = "http://testapi.teric.ai:3500"
    url = "http://3.0.102.169:3500"
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2R1bGVzIjp7ImFjdGl2ZWxlYXJuaW5nIjpbIioiXSwiYW5ub3RhdGlvbiI6WyIqIl0sImRhdGFwb2ludCI6WyIqIl0sImRhdGFzZXQiOlsiKiJdLCJleHBlcmltZW50IjpbIioiXSwibW9kZWwiOlsiKiJdLCJwcm9qZWN0IjpbIioiXSwicmVxdWVzdCI6WyIqIl0sInRhc2siOlsiKiJdLCJ0ZWFtIjpbIioiXX0sInRlYW1zIjpbeyJuYW1lIjoiVGVhbSBlZGl0ZWQiLCJyb2xlIjoiYWRtaW4iLCJ0ZWFtX2lkIjoiNWQzYzFhOTAwYTMxMmUwMGUxZWNiMTY1In1dLCJ1c2VyIjp7Il9pZCI6IjVkMjgzOGJkYTkyNDJmMDJmYzRmMzI3YSIsImVtYWlsIjoiYWRtaW5AdGVyaWNzb2Z0LmNvbSIsImV4cCI6MTU2NTYxNzc5OSwibmFtZSI6InVzZXIiLCJwaG9uZSI6IjY5OTk5OTk5NTUiLCJyb2xlIjoiYWRtaW4ifX0.UZvonkw7RW4zQ8wibjetJcaGDWTrsQoDQKXgwCewVNk"
    
    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        "Content-Type": "application/json",
        "Authorization": "Bearer "+str(token)
    }
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    # def on_stop(self):
    #     """ on_stop is called when the TaskSet is stopping """
    #     self.logout()

    def login(self):
        self.client.post(self.url+"/account/login", {"username":"admin  @tericsoft.com", "password":"123456"})

    # def logout(self):
    #     self.client.post(self.url+"/account/logout")

    @task(1)
    def list(self):
        self.client.post(self.url+"/task/list",{"annotator_id":"5d330e0778500f002d9889bf"},self.headers)
    @task(2)
    def add(self):
        self.client.post(self.url+"/task/add",{"request_id" : "5d43e235276bfe00f6f1c56a","annotators" : {"5d3c229a0a312e0a78639d67" :{"count":4}}},self.headers)
    @task(2)
    def delete(self):
        self.client.post(self.url+"/task/delete",{"task_id":"5d43e972276bfe00d712c9e6"},self.headers)
    @task(2)
    def edit(self):
        self.client.post(self.url+"/task/edit",{"task_id":"5d43e972276bfe00d712c9e6","status":"pending"},self.headers)
    @task(2)
    def view(self):
        self.client.post(self.url+"/task/view",{"task_id":"5d43e972276bfe00d712c9e6"},self.headers)
    @task(2)
    def getimage(self):
        self.client.post(self.url+"/task/getimage",{"task_id":"5d43e972276bfe00d712c9e6"},self.headers)
    @task(2)
    def imageHistory(self):
        self.client.post(self.url+"/task/imageHistory",{"task_id":"5d43ec7f276bfe01679d53b0"},self.headers)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
