from pages.login_page import LoginPage
from pages.users_page import UsersPage


def test_admin_users_page_access(driver):

    login_page = LoginPage(driver)
    users_page = UsersPage(driver)

    login_page.open_login_page()
    login_page.login("admin@example.com", "Admin@123")

    users_page.open_users_page()

    assert users_page.users_table_visible()





def test_non_admin_cannot_access_users(driver):

    login_page = LoginPage(driver)

    login_page.open_login_page()

    # login as normal user
    login_page.login_as_user()

    driver.get("https://react-frontend-api-testing.vercel.app/users")

    assert "permission" in driver.page_source.lower()
    