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
    def newTrainRequest(self):
        self.client.post(self.url+"/experiment/newTrainRequest",data=json.dumps({"experiment_id" : "5d4d93e87bd2e300b8f5dc52","framework" : "darknet","architecture" : "yolo","train_ratio" : 90,"subdivision" : 8,"batch" : 8,"model_boundary" : "1,5,9"}),headers = self.headers)
    @task(2)
    def listTrainRequest(self):
        self.client.post(self.url+"/experiment/listTrainRequest",headers = self.headers)
    @task(2)
    def deleteTrainRequest(self):
        self.client.post(self.url+"/experiment/deleteTrainRequest",data=json.dumps({"train_request_id":"5d4bad4cc078d500c053eaa1"}),headers = self.headers)
    @task(2)
    def viewTrainRequest(self):
        self.client.post(self.url+"/experiment/viewTrainRequest",data=json.dumps({"train_request_id":"5d4be76252d5790038dae768"}),headers = self.headers)
    @task(2)
    def startTraining(self)
        self.client.post(self.url+"/experiment/startTraining",data=json.dumps({"train_request_id":"5d4ddcc4cb6f040027dabc84"}),headers = self.headers)
    @task(2)
    def stopTraining(self)
        self.client.post(self.url+"/experiment/stopTraining",data=json.dumps({"train_request_id":"5d4bf7a252d57909dbd9fea4"}),headers = self.headers)
    @task(2)
    def upgradeModel(self)
        self.client.post(self.url+"/experiment/upgradeModel",data=json.dumps({"train_request_id":"5d4ce1cf52d5790117de3fd8","title":"testing go http"}),headers = self.headers)
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
