from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)  # Har bir so‘rov orasidagi kutish vaqti (sekundlarda)

    @task
    def test_homepage(self):
        self.client.get("/")  # Asosiy URLga GET so‘rov yuborish

    # @task
    # def test_about_page(self):
    #     self.client.get("/about")  # /about URLga GET so‘rov yuborish
