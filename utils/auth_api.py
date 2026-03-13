from utils.base_api import BaseAPI


class AuthAPI(BaseAPI):

    def __init__(self, base_url):
        super().__init__(base_url)
        self.token = None

    def login(self, username, password):
        response = self.post("/auth", {
            "username": username,
            "password": password
        })
        self.token = response.json().get("token")
        return self.token