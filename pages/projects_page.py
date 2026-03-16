from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProjectsPage(BasePage):

    PROJECTS_MENU = (By.XPATH, "//a[@href='/projects']")
    ADD_PROJECT_BUTTON = (By.XPATH, "//button[contains(.,'New Project')]")
    TITLE_INPUT = (By.XPATH, "//label[text()='Title']/following::input[1]")
    DESCRIPTION_INPUT = (By.XPATH, "//label[text()='Description']/following::textarea[1]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(.,'Save')]")
    PROJECT_TABLE = (By.XPATH, "//table")

    def open_projects_page(self):
        self.click(self.PROJECTS_MENU)

    def click_add_project(self):
        self.click(self.ADD_PROJECT_BUTTON)

    def enter_project_name(self, name):
        self.type(self.TITLE_INPUT, name)

    def enter_description(self, desc):
        self.type(self.DESCRIPTION_INPUT, desc)

    def save_project(self):
        self.click(self.SAVE_BUTTON)

    def project_created(self):
        return self.find(self.PROJECT_TABLE).is_displayed()