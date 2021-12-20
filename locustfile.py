from locust import HttpUser, task, between

class User(HttpUser):
    time = between(1, 5)
    host = 'https://reqres.in/api'

    @task(1)
    def list_of_users(self):
        self.client.get("/users")

    @task(3)
    def create_user(self):
        self.client.post("/users", json={
            "name": "Veronika Santo",
            "job": "Front-end developer"
        })

    @task(3)
    def update_user(self):
        self.client.put("/users", json={
            "name": "Veronika Santo",
            "surname": "Santo"
        })

    @task(1)
    def delete_user(self):
        self.client.delete("/users/2")

    @task(1)
    def registration_user(self):
        self.client.post("/register", json=
            {
                "email": "eve.holt@reqres.in",
                "password": "pistol"
            }
        )

    @task(1)
    def login_user(self):
        self.client.post("/login", json=
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
