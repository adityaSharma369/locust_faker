from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
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

    # def on_stop(self):
    #     """ on_stop is called when the TaskSet is stopping """
    #     self.logout()

    # def login(self):
    #     self.client.post(self.url+"/account/login", {"username":"admin@tericsoft.com", "password":"123456"})

    # def logout(self):
    #     self.client.post(self.url+"/account/logout")

    @task(2)
    def list(self):
        self.client.get(self.url+"/dataset/list",headers = self.headers)
    @task(2)
    def add(self):
        self.client.get(self.url+"/dataset/add",data=json.dumps({"title":"the indian dogs","Description":"but it just dogs","dataset_type":"manual"}),headers = self.headers)
    @task(2)
    def delete(self):
        self.client.get(self.url+"/dataset/delete",data=json.dumps({"dataset_id":"5d4c7daf1d7ca5020fec93e6"}),headers = self.headers)
    @task(2)
    def edit(self):
        self.client.get(self.url+"/dataset/Edit",data=json.dumps({"title":"the indian dogs","Description":"dogs aalso feel pain"}),headers = self.headers)
    @task(2)
    def view(self):
        self.client.get(self.url+"/dataset/view",data=json.dumps({"dataset_id":"5d4c7daf1d7ca5020fec93e6"}),headers = self.headers)
    @task(2)
    def imageExists(self):
        self.client.get(self.url+"dataset/ImageExists",data=json.dumps({"dataset_id":"5d4c7daf1d7ca5020fec93e6","hash":"234"}),headers = self.headers)

    @task(1)
    def uploadImages(self):
        self.client.post(self.url+"/dataset/uploadSingleImage", data=json.dumps({"dataset_id":"5d4c7daf1d7ca5020fec93e6","dataset_image":"/home/tericsoft/Pictures/30_photos/2019-06-19-160202.png","hash":"123"}),headers = self.headers)
    @task(2)
    def images(self):
        self.client.get(self.url+"/dataset/listImages",data=json.dumps({"dataset_id":"5d4c7daf1d7ca5020fec93e6"}),headers = self.headers)
    @task(2)
    def deleteImage(self):
        self.client.get(self.url+"/dataset/deleteImage",data=json.dumps({"image_id":"5d4bea631d7ca501edb48e1e","dataset_id":"5d4c7daf1d7ca5020fec93e6"}),headers = self.headers)
     
    

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000