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

    # def logout(self):
    #     self.client.post(self.url+"/account/logout")

    @task(1)
    def list(self):
        self.client.post(self.url+"/request/list",headers = self.headers)
    @task(2)
    def add(self):
        self.client.post(self.url+"/request/add",data=json.dumps({"experiment_id" : "5d3f9a843dc4e0002ab10727","request_type": "per_class","rules":{"classes" : {"cat" : 20,"dog" : 10}}}),headers = self.headers)
    @task(2)
    def delete(self):
        self.client.post(self.url+"/request/delete",data=json.dumps({"request_id":"5d2cef63d24c0d0038594383"}),headers = self.headers)
    @task(2)
    def edit(self):
        self.client.post(self.url+"/request/edit",data=json.dumps({"model_id":"5d25d54930c4dc0075aca322","is_active":"true"}),headers = self.headers)
    class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
