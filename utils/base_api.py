import requests


class BaseAPI:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
        })

    def get(self, endpoint):
            return self.session.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint, payload):
            return self.session.post(
                f"{self.base_url}{endpoint}",
                json=payload,
            )