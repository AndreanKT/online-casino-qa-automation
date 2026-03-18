# tests/api/test_auth.py
import uuid                                   # Модул за уникални emails?
import os                                   # Модул за env променливи?
from jsonschema import validate
import pytest
from dotenv import load_dotenv               # Как зареждаме .env?
load_dotenv()                                         # Как викаме load_dotenv?
from utils.performance import assert_response_time
from utils.schemas.auth_schemas import LOGIN_SCHEMA, REGISTER_SCHEMA
from utils.auth_api import AuthAPI
from utils.logger import get_logger
logger = get_logger(__name__)
import json
with open("fixtures/auth_fixtures.json") as f:
    auth_data = json.load(f)


# Кой клас импортираме?

class TestAuth:                                    # Как се казва класа?

    def test_login_valid(self, auth):          # Какъв fixture?                      # Създаваме AuthAPI с?
        response = auth.login(                  # Кой метод?
            username=os.getenv("USER_EMAIL"),          # Email от env?
            password=os.getenv("USER_PASSWORD")           # Password от env?
        )

        assert response.status_code  == 200
        validate(response.json(), LOGIN_SCHEMA)
        assert_response_time(response, "login")
        logger.info("test_login_valid PASSED")


    def test_login_response_time(self, auth):
        response = auth.login(
            username=os.getenv("USER_EMAIL"),
            password=os.getenv("USER_PASSWORD")
        )
        assert response.elapsed.total_seconds() < 2.0

        # ❌ NEGATIVE

    @pytest.mark.parametrize("username, password, expected_status, expected_message", [
        (os.getenv("USER_EMAIL"), "Password123!", 400, "Incorrect email or password."),  # Wrong password
        ("nonexistent@abv.bg", "Password123!", 400, "Incorrect email or password."),  # Non existing email
        ("", "", 400, "Email is required"),  # Empty fields
        ("' OR '1'='1", "Password123!", 400, "Incorrect email or password."),  # SQL injection email
        ("nonexistent@abv.bg", "' OR '1'='1", 400, "Incorrect email or password."),  # SQL injection password
    ])
    def test_login_negative(self, auth, username, password, expected_status, expected_message):
        response = auth.login(
            username=username,
            password=password
        )
        assert response.status_code == expected_status
        assert response.json()["message"] == expected_message

        #Edge Case
    @pytest.mark.parametrize("username, password, expected_status", [
        (os.getenv("USER_EMAIL").upper(), os.getenv("USER_PASSWORD"), 400),  # ГЛАВНИ БУКВИ
        (" " + os.getenv("USER_EMAIL") + " ", os.getenv("USER_PASSWORD"), 400),  # ИНТЕРВАЛИ
        (os.getenv("USER_EMAIL"), os.getenv("USER_PASSWORD") + " ", 400),  # ИНТЕРВАЛ В КРАЯ
        (os.getenv("USER_EMAIL"), os.getenv("USER_PASSWORD").lower(), 400),  # БЕЗ ГЛАВНА БУКВА
        ("a" * 100 + "@abv.bg", os.getenv("USER_PASSWORD"), 400), # Too many symbols
    ])
    def test_login_edge(self, auth, username, password, expected_status):
           response = auth.login(
                username=username,
                password=password
           )
           assert response.status_code == expected_status

    def test_token_from_another_user(self, auth):
        import base64

        # Стъпка 1 — Регистрираш User 2
        unique_email = f"test_{uuid.uuid4()}@abv.bg"
        auth.register(
            firstName="second",
            lastName="user",
            userEmail=unique_email,
            userPassword="Password123!",
            confirmPassword="Password123!",
            userMobile="1111111111"
        )

        # Стъпка 2 — Логваш User 2 → вземаш неговия ID
        response2 = auth.login(
            username=unique_email,
            password="Password123!"
        )
        token2 = response2.json()["token"]
        payload2 = token2.split(".")[1]
        payload2 += "=" * (4 - len(payload2) % 4)
        user2_id = json.loads(base64.b64decode(payload2))["_id"]

        # Стъпка 3 — Логваш User 1 → вземаш токена!
        response1 = auth.login(
            username=os.getenv("USER_EMAIL"),
            password=os.getenv("USER_PASSWORD")
        )
        token1 = response1.json()["token"]

        response = auth.get_with_token(
            f"/api/ecom/user/get-cart-count/{user2_id}",
            token=token1
        )

        print(response.status_code)
        print(response.json())
        assert response.status_code == 400

    def test_brute_force_protection(self, auth):
        response = None

        for i in range(10):
            response = auth.login(
            username=os.getenv("USER_EMAIL"),
            password=f"WrongPassword{i}!"
            )
        assert response.status_code in [400, 429], \
            f"Expected rate limiting after 10 attempts but got {response.status_code}" # If the API does not give 429

    def test_register_valid(self, auth):
        unique_email = f"test_{uuid.uuid4()}@abv.bg"

        user_data = auth_data["new_user"].copy()
        user_data["userEmail"] = unique_email

        response = auth.register(**user_data)

        assert response.status_code == 200
        validate(response.json(), REGISTER_SCHEMA)
        assert_response_time(response, "register")