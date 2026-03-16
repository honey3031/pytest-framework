from pages.login_page import LoginPage
from pages.scenarios_page import ScenariosPage
import time


def test_frames_and_windows(driver):

    login_page = LoginPage(driver)
    scenarios = ScenariosPage(driver)

    login_page.open_login_page()
    login_page.login("admin@example.com", "Admin@123")

    scenarios.open_test_scenarios()

    main_window = driver.current_window_handle

    # -------- IFRAME --------
    scenarios.switch_to_iframe()
    time.sleep(2)   # see iframe content
    assert "example domain" in driver.page_source.lower()

    driver.switch_to.default_content()

    # -------- NEW TAB --------
    scenarios.open_new_tab()

    time.sleep(2)   # WAIT so you can see the tab open

    new_window = [w for w in driver.window_handles if w != main_window][0]
    driver.switch_to.window(new_window)

    time.sleep(2)   # see the tab content

    assert "example domain" in driver.page_source.lower()

    driver.close()
    driver.switch_to.window(main_window)

    # -------- POPUP WINDOW --------
    scenarios.open_popup()

    time.sleep(2)   # WAIT so popup is visible

    popup = [w for w in driver.window_handles if w != main_window][0]
    driver.switch_to.window(popup)

    time.sleep(2)   # observe popup

    driver.close()
    driver.switch_to.window(main_window)