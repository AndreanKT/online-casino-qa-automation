import pytest
from playwright.sync_api import Page


class TestLoginUI:

    def test_valid_login(self, page: Page):
        """Логин с валидни данни"""
        page.goto("https://the-internet.herokuapp.com/login")

        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")

        assert "secure" in page.url
        assert page.locator(".flash.success").is_visible()

    def test_invalid_login(self, page: Page):
        """Логин с грешни данни"""
        page.goto("https://the-internet.herokuapp.com/login")

        page.fill("#username", "wrong")
        page.fill("#password", "wrong")
        page.click("button[type='submit']")

        assert page.locator(".flash.error").is_visible()

    def test_empty_login(self, page: Page):
        """Логин с празни полета"""
        page.goto("https://the-internet.herokuapp.com/login")

        page.click("button[type='submit']")

        assert page.locator(".flash.error").is_visible()