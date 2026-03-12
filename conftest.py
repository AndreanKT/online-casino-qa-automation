import pytest
import requests
from playwright.sync_api import sync_playwright

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    return session

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def auth_token(api_client):
    response = api_client.post(
        f"{BASE_URL}/auth",
        json={"username": "admin", "password": "password123"}
    )
    return response.json().get("token")

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()