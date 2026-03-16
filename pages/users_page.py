from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UsersPage(BasePage):

    USERS_MENU = (By.XPATH, "//a[@href='/users']")
    USERS_TABLE = (By.XPATH, "//table")

    def open_users_page(self):
        self.click(self.USERS_MENU)

    def users_table_visible(self):
        return self.find(self.USERS_TABLE).is_displayed()