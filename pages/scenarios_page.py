from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ScenariosPage(BasePage):

    TEST_SCENARIOS_MENU = (By.XPATH, "//a[@href='/test-scenarios']")

    ALERT_BUTTON = (By.XPATH, "//button[contains(text(),'Trigger Alert')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Trigger Confirm')]")
    PROMPT_BUTTON = (By.XPATH, "//button[contains(text(),'Trigger Prompt')]")
    IFRAME_TEXT = (By.XPATH, "//h3")

    def open_test_scenarios(self):
        self.click(self.TEST_SCENARIOS_MENU)

    def trigger_alert(self):
        self.click(self.ALERT_BUTTON)

    def trigger_confirm(self):
        self.click(self.CONFIRM_BUTTON)

    def trigger_prompt(self):
        self.click(self.PROMPT_BUTTON)

    SCENARIO_MENU = (By.XPATH, "//a[@href='/test-scenarios']")
    NEW_TAB_BUTTON = (By.ID, "btn-new-tab")
    POPUP_BUTTON = (By.ID, "btn-popup-window")

    IFRAME = (By.CSS_SELECTOR, "iframe")


    def open_test_scenarios(self):
        self.click(self.SCENARIO_MENU)


    def open_new_tab(self):
        self.click(self.NEW_TAB_BUTTON)


    def open_popup(self):
        self.click(self.POPUP_BUTTON)


    def switch_to_iframe(self):
        iframe = self.find(self.IFRAME)
        self.driver.switch_to.frame(iframe)

    def switch_to_default(self):
        self.driver.switch_to.default_content()