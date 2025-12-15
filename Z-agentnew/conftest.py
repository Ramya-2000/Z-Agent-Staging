# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
#
# @pytest.fixture(scope="session")
# def driver(request):
#     """Setup and teardown for WebDriver"""
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     # Optional: run headless
#     # chrome_options.add_argument("--headless=new")
#
#     chrome_options.add_experimental_option("detach", True)  # keeps the browser window open
#     prefs = {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False,
#         "profile.password_manager_leak_detection": False
#     }
#     chrome_options.add_experimental_option("prefs", prefs)
#
#
#     # Initialize the Chrome driver
#     service = Service()  # Use default ChromeDriver from PATH
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#
#     # ✅ Attach the driver to the test class
#     request.cls.driver = driver
#
#     yield driver
#
#     # ✅ Quit browser after test class
#     driver.quit()
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from utils.screenshot import take_screenshot


@pytest.fixture(scope="session")
def driver():
    """Session-scoped WebDriver shared across all tests"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless=new")  # optional headless

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)


    service = Service()  # Make sure chromedriver is in PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    driver = item.funcargs.get("driver", None)
    if driver and report.when == "call":
        # ---- handle failed test ----
        if report.failed:
            try:
                screenshot = take_screenshot(driver, f"{item.name}_failed")
                if screenshot:  # prevent NoneType issue
                    allure.attach.file(
                        screenshot,
                        name="Failure Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
            except Exception as e:
                print(f"⚠ Error taking failure screenshot: {e}")

        # ---- handle passed test ----
        if report.passed:
            try:
                screenshot = take_screenshot(driver, f"{item.name}_passed")
                if screenshot:
                    allure.attach.file(
                        screenshot,
                        name="Success Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
            except Exception as e:
                print(f"⚠ Error taking success screenshot: {e}")

@pytest.fixture(autouse=True)
def measure_latency(request):
    """
    Fixture to measure and print latency for each test case automatically.
    autouse=True ensures it runs for all tests.
    """
    start_time = time.time()
    yield
    end_time = time.time()
    latency = end_time - start_time
    print(f"Latency for test '{request.node.name}': {latency:.2f} seconds")