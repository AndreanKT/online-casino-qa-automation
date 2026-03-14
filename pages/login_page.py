from pages.base_page import BasePage


class LoginPage(BasePage):

    # Selectors → намери ги с F12!
    EMAIL_INPUT = "input[placeholder='email@example.com']"
    PASSWORD_INPUT = "input[placeholder='enter your passsword']"
    SUBMIT_BUTTON = "#login"

    def __init__(self, page):
        super().__init__(page)
        self.navigate("https://rahulshettyacademy.com/client")

    def login(self, email, password):
        self.fill(self. EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)
        self.page.wait_for_url("**/dashboard**", timeout=10000)

    def is_logged_in(self):
        return "dashboard" in self.page.url
