import uuid

from utils.auth_api import AuthAPI


class TestAuth:

    def test_login_valid(self, base_url, valid_credentials):
        auth = AuthAPI(base_url)
        token = auth.login(
            valid_credentials["username"],
            valid_credentials["password"]
        )
        assert token is not None
        assert isinstance(token, str)

    def test_login_invalid(self, base_url, invalid_credentials):
        auth = AuthAPI(base_url)
        token = auth.login(
            invalid_credentials["username"],
            invalid_credentials["password"]
        )
        assert token is None

    def test_login_empty(self, base_url):
        auth = AuthAPI(base_url)
        token = auth.login(" ", " ")
        assert token is None

    def test_register(self, base_url):
        auth = AuthAPI(base_url)
        unique_email = f"test_{ uuid.uuid4()}@abv.bg"

        response = auth.register(

            email=unique_email,
            password="Kubrat803!",
            firstname="Andrean",
            lastname="Test",
            mobile="1111111111"
        )

        assert response["message"] == "Registered Successfully"



