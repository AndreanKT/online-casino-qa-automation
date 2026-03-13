import pytest
import requests
from playwright.sync_api import sync_playwright

BASE_URL = "https://restful-booker.herokuapp.com"

# scope="session" → дефинирани ВЕДНЪЖ → ползвани навсякъде
@pytest.fixture(scope="session")
def valid_credentials():
    return {
        "username": "admin",
        "password": "password123"
    }

# scope="session" → невалидни данни за negative тестове
@pytest.fixture(scope="session")
def invalid_credentials():
    return {
        "username": "wrong",
        "password": "wrong"
    }  # ← ЗАТВОРЕНА СКОБА!

# scope="session" → създава се ВЕДНЪЖ за целия test run
@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

# scope="session" → една HTTP сесия за всички тестове
@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json"
    })
    yield session
    session.close()

# scope="session" → логваме се ВЕДНЪЖ
@pytest.fixture(scope="session")
def auth_token(api_client):
    response = api_client.post(
        f"{BASE_URL}/auth",
        json={"username": "admin", "password": "password123"}
    )
    token = response.json().get("token")
    assert token is not None, "Failed to get auth token!"
    return token

# scope="function" → clean state за всеки тест
@pytest.fixture(scope="function")
def created_booking(api_client, auth_token):
    response = api_client.post(
        f"{BASE_URL}/booking",
        json={
            "firstname": "Test",
            "lastname": "User",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-01-01",
                "checkout": "2025-01-10"
            }
        }
    )
    booking_id = response.json()["bookingid"]
    yield booking_id

    # TEARDOWN → clean up след теста
    api_client.delete(
        f"{BASE_URL}/booking/{booking_id}",
        headers={"Cookie": f"token={auth_token}"}
    )

# scope="session" → headless за CI/CD pipeline
@pytest.fixture(scope="session")
def browser_type_launch_options():
    return {
        "headless": True,
        "args": ["--no-sandbox", "--disable-dev-shm-usage"]
    }

# scope="session" → браузърът се отваря ВЕДНЪЖ
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

# scope="function" → нова страница за всеки UI тест
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()