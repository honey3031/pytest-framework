from pages.login_page import LoginPage
from pages.scenarios_page import ScenariosPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_alert_confirm_prompt(driver):

    login_page = LoginPage(driver)
    test_page = ScenariosPage(driver)

    login_page.open_login_page()
    login_page.login("admin@example.com", "Admin@123")

    test_page.open_test_scenarios()

    # ALERT
    test_page.trigger_alert()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    # CONFIRM
    test_page.trigger_confirm()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    confirm = driver.switch_to.alert
    confirm.dismiss()

    # PROMPT
    test_page.trigger_prompt()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    prompt = driver.switch_to.alert
    prompt.send_keys("Automation Test")
    prompt.accept()