import requests


class BaseAPI:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def post(self, endpoint, payload):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=payload
        )

    def get(self, endpoint):
        return self.session.get(
            f"{self.base_url}{endpoint}"
        )

    def delete(self, endpoint, token):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            headers={"Cookie": f"token={token}"}
        )

    def put(self, endpoint, payload, token):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            json=payload,
        headers = {"Cookie": f"token={token}"}
        )