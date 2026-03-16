import pytest
import os
from utils.driver_factory import create_driver
from utils.screenshot_utils import capture_screenshot


@pytest.fixture(scope="function")
def driver(request):

    driver = create_driver()

    yield driver

    # take screenshot if test failed
    if request.node.rep_call.failed:
        capture_screenshot(driver, request.node.name)

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)