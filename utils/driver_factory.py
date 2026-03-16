from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import GRID_URL, HEADLESS


def create_driver():

    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    return driver