from pages.login_page import LoginPage
from pages.tasks_page import TasksPage


def test_task_status_update(driver):

    login_page = LoginPage(driver)
    tasks_page = TasksPage(driver)

    login_page.open_login_page()
    login_page.login("admin@example.com", "Admin@123")

    tasks_page.open_tasks_page()

    tasks_page.mark_task_done()

    driver.refresh()

    assert tasks_page.status_is_done()