from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'text-red')]")
    USER_DEMO_BUTTON = (By.CSS_SELECTOR, "button.btn-outline-secondary")


    def open_login_page(self):
        self.open(BASE_URL + "/login")

    def enter_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    



    def login_as_user(self):
        self.click(self.USER_DEMO_BUTTON)   # fills email & password
        self.click(self.LOGIN_BUTTON)       # submit login

        WebDriverWait(self.driver, 10).until(
        EC.url_contains("dashboard")
    )