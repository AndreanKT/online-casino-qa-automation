class TestScreenshotCheck:

    def test_failing_on_purpose(self, page):
        from pages.login_page import LoginPage
        login_page = LoginPage(page)

        # Умишлено грешен assert!
        assert "dashboard" in page.url  # ← ще фейлне!