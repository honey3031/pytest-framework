from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    USERS_MENU = (By.XPATH, "//a[@href='/users']")

    def users_menu_visible(self):
        elements = self.driver.find_elements(*self.USERS_MENU)
        return len(elements) > 0