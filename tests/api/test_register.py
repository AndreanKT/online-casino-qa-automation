import uuid

from utils.auth_api import AuthAPI

class TestRegister:
   def test_register(self, base_url):
    auth = AuthAPI(base_url)
    unique_email = f"test_{uuid.uuid4()}@abv.bg"

    response = auth.register(

        email=unique_email,
        password="Kubrat803!",
        firstname="Andrean",
        lastname="Test",
        mobile="1111111111"
    )

    assert response["message"] == "Registered Successfully"
