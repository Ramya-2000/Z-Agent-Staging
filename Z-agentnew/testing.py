import pytest
import allure
import os
import time
from selenium import webdriver
from lets_get_started import LetsGetStarted
from selenium.webdriver.chrome.service import Service


def take_screenshot(driver, test_name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)
    allure.attach.file(screenshot_path, name=test_name, attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="class")
def driver():
    service = Service("C:\\Users\\admin\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://web.zagent.stage.yavar.ai/bots")
    time.sleep(2)


    yield driver

    # 👇 Keep driver open until you close it manually
    print("\n⚙️ Waiting for you to close the browser manually...")
    while True:
        try:
            driver.title  # Will raise error when browser is closed
            time.sleep(1)
        except Exception:
            print("✅ Browser closed. Exiting test.")
            break


@allure.suite("Authentication")
@allure.sub_suite("Login")
@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_create_bot(self, driver):  # ✅ driver fixture is injected here
        page = LetsGetStarted(driver)  # ✅ driver is the real WebDriver now
        page.lets_gets_started()

    @allure.story("Blank Fields")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_blank_fields(self, driver):
        test_name = "test_blank_fields"
        driver.refresh()
        try:
            pass
            # Example (commented logic):
            # checkbox = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "//button[@id='terms']"))
            # )
            # if not checkbox.is_selected():
            #     checkbox.click()
            # assert not checkbox.is_selected()
            #
            # btn = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))
            # )
            # btn.click()
            #
            # assert "Enter email" in driver.page_source
            # take_screenshot(driver, test_name)

        except AssertionError as e:
            take_screenshot(driver, f"{test_name}_failure")
            raise


