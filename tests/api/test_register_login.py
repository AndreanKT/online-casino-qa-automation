import uuid

from pages.login_page import LoginPage
from utils.auth_api import AuthAPI


class TestRegisterAndLogin:

    def test_register_via_api_login_via_ui(self, base_url, page, testing_password):
        auth = AuthAPI(base_url)
        unique_email = f"test_{uuid.uuid4()}@abv.bg"

        response = auth.register(
            email=unique_email,
            password=testing_password,
            firstname="Andrean",
            lastname="Test",
            mobile="1111111111"
        )
        assert response["message"] == "Registered Successfully"

        login_page = LoginPage(page)
        login_page.login(unique_email, testing_password)

        assert login_page.is_logged_in()