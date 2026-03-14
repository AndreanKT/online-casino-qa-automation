import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope="session")
def valid_credentials():
    return {
        "username": os.getenv("USER_EMAIL"),
        "password": os.getenv("USER_PASSWORD")
    }

@pytest.fixture(scope="session")
def invalid_credentials():
    return {
        "username": "wrong",
        "password": "wrong"
    }