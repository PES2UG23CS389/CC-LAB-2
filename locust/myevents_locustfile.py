from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_my_events(self):
        # use a valid user that exists in DB
        self.client.get("/my-events?user=PES2UG23CS389")
