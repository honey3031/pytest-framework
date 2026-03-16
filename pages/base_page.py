from utils.wait_utils import WaitUtils


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.wait_for_visible(locator)

    def click(self, locator):
        element = self.wait.wait_for_clickable(locator)
        element.click()

    def type(self, locator, text):
        element = self.wait.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.wait_for_visible(locator)
        return element.text