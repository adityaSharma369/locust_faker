from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    url = "http://3.0.102.169:3500"
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post(self.url+"/account/login", {"username":"admin@tericsoft.com", "password":"123456"})

    def logout(self):
        self.client.post(self.url+"/account/logout")

    @task(2)
    def index(self):
        self.client.post(self.url+"/dataset/list",{"is_active": "true"})

    @task(1)
    def listImages(self):
        self.client.post(self.url+"/dataset/uploadSingleImage", {"dataset_id":"5d303722d709aa002e184257","dataset_image":"/home/tericsoft/Pictures/30_photos/2019-06-19-160202.png","hash":"123"})


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000