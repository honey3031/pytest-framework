from pages.login_page import LoginPage


def test_valid_admin_login(driver):

    login_page = LoginPage(driver)

    login_page.open_login_page()

    login_page.login("admin@example.com", "Admin@123")

    assert "Dashboard" in driver.page_source

import pytest


@pytest.mark.parametrize(
    "email,password",
    [
        ("admin@example.com", "wrongpassword"),
        ("wrong@example.com", "password"),
        ("", "password"),
        ("admin@example.com", ""),
    ]
)
def test_invalid_login(driver, email, password):

    login_page = LoginPage(driver)

    login_page.open_login_page()

    login_page.login(email, password)

    # user should still remain on login page
    assert "/login" in driver.current_url

from utils.logger import get_logger

logger = get_logger(__name__)

def test_valid_admin_login(driver):

    logger.info("Test started")

    driver.get("https://example.com")

    logger.info("Website opened successfully")