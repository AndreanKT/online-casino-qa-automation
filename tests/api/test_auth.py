import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"

class TestAuthentication:

    def test_login_valid_credentials(self):
        """Логин с валидни данни трябва да върне token"""
        response = requests.post(
            f"{BASE_URL}/auth",
            json={
                "username": "admin",
                "password": "password123"
            }
        )
        assert response.status_code == 200
        assert "token" in response.json()
        print(f"Token: {response.json()['token']}")

    def test_login_invalid_credentials(self):
        """Логин с грешни данни не трябва да върне token"""
        response = requests.post(
            f"{BASE_URL}/auth",
            json={
                "username": "wrong",
                "password": "wrong"
            }
        )
        assert response.status_code == 200
        assert response.json().get("reason") == "Bad credentials"

    def test_login_empty_credentials(self):
        """Логин с празни полета"""
        response = requests.post(
            f"{BASE_URL}/auth",
            json={
                "username": "",
                "password": ""
            }
        )
        assert response.status_code == 200
        assert "token" not in response.json()