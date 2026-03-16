from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage


def test_create_project(driver):

    login_page = LoginPage(driver)
    projects_page = ProjectsPage(driver)

    login_page.open_login_page()
    login_page.login("admin@example.com", "Admin@123")

    projects_page.open_projects_page()

    projects_page.click_add_project()

    projects_page.enter_project_name("Automation Project")

    projects_page.enter_description("Created by Selenium Test")

    projects_page.save_project()

    assert projects_page.project_created()