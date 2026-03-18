import pytest
import os
from dotenv import load_dotenv
from utils.auth_api import AuthAPI

load_dotenv()


# ═══ HOOK → за screenshots при failure ═══
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# ═══ BASE URL ═══
@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


# ═══ CREDENTIALS ═══
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

@pytest.fixture(scope="session")
def testing_password():
    return os.getenv("TEST_PASSWORD")


# ═══ PLAYWRIGHT → Videos ═══
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    os.makedirs("reports/videos", exist_ok=True)
    return {
        **browser_context_args,
        "record_video_dir": "reports/videos/",
        "record_video_size": {
            "width": 1280,
            "height": 720
        }
    }


# ═══ PLAYWRIGHT → Page + Screenshots при failure ═══
@pytest.fixture(scope="function")
def page(browser, request):
    page = browser.new_page()
    yield page

    # Screenshot само при failure!
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("reports/screenshots", exist_ok=True)
        page.screenshot(
            path=f"reports/screenshots/{request.node.name}.png"
        )

    page.close()

@pytest.fixture
def auth(base_url):
    return AuthAPI(base_url)