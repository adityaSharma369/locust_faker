from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    # url = "http://testapi.teric.ai:3500"
    url = "http://13.250.2.214:3500"
    token="lckB0ZXJpY3NvZnQuY29tIiwiZXhwIjoxNTcxMzkyMjUyLCJmaXJzdF9uYW1lIjoiRGVmYXVsdCBVc2VyIiwibGFzdF9uYW1lIjoiIiwicGhvbmUiOiIwMDAwMDAwMDAwIiwicm9sZSI6Im1hbmFnZXIifX0.8GizBedLmW5fSttiwe0eK8FWoUugj95p9q8UXU74jiY"
    
    headers = {
        # "X-Requested-With": "XMLHttpRequest",
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        
        "Content-Type": "application/json",
        "Authorization": "Bearer "+token
    }
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    # def on_stop(self):
    #     """ on_stop is called when the TaskSet is stopping """
    #     self.logout()

    def login(self):
        self.client.post(self.url+"/account/login", {"username":"manager@tericsoft.com", "password":"123456"})

    # def logout(self):
    #     self.client.post(self.url+"/account/logout")
    @task(1)
    def list(self):
        self.client.get(self.url+"/account/checklogin",headers = self.headers)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
