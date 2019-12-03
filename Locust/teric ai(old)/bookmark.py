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
        self.client.post(self.url+"/bookmark/list",data=json.dumps({"image_id":"5d47e6dc03acd3009abdc0x4"}),headers = self.headers)
    @task(2)
    def add(self):
        self.client.post(self.url+"/bookmark/add",data=json.dumps({"title":"bookmark testing","bookmark_type":"manual","experiment_id":"5d26e301fedb96002c844cf0"}),headers = self.headers)
    @task(2)
    def delete(self):
        self.client.post(self.url+"/bookmark/delete",data=json.dumps({"bookmark_id":"5d4a64b227a27d00c2ec1098"}),headers = self.headers)
    @task(2)
    def edit(self):
        self.client.post(self.url+"/bookmark/edit",data=json.dumps({"bookmark_id":"5d26fe44729b6e04454f556c","title":"bookmark 1"}),headers = self.headers)
    class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
