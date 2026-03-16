from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TasksPage(BasePage):

    TASKS_MENU = (By.XPATH, "//a[@href='/tasks']")

    DONE_BUTTON = (By.XPATH, "//button[contains(text(),'Done')]")

    STATUS_DONE = (By.XPATH, "//span[contains(text(),'done')]")

    def open_tasks_page(self):
        self.click(self.TASKS_MENU)

    def mark_task_done(self):
        self.click(self.DONE_BUTTON)

    def status_is_done(self):
        return self.find(self.STATUS_DONE).is_displayed()