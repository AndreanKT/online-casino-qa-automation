from utils.base_api import BaseAPI


class AuthAPI(BaseAPI):

    def __init__(self, base_url):
        super().__init__(base_url)
        self.token = None

    def login(self, username, password ):
        response = self.post("/api/ecom/auth/login", {
            "userEmail": username,
            "userPassword": password
        })

        if response.status_code != 200:
            return None

        return response.json().get("token")

    def register(self, email, password, firstname, lastname, mobile):
        response = self.post("/api/ecom/auth/register", {
            "userEmail": email,
            "userPassword": password,
            "confirmPassword": password,
            "firstName": firstname,
            "lastName": lastname,
            "userMobile": mobile,
            "userRole": "customer"
        })

        if response.status_code not in [200, 201]:
            return None
        return response.json()

