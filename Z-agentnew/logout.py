import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Utility function to capture and attach screenshots to Allure report
def take_screenshot(driver, test_name):
    """Capture a screenshot and attach it to Allure report."""
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)
    allure.attach.file(screenshot_path, name=test_name, attachment_type=allure.attachment_type.PNG)

# Fixture to initialize and quit the WebDriver
@pytest.fixture(scope="class")
def driver():
    service = Service('C:\\Users\\admin\\Videos\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://copper-ai-agent-dev.yavar.ai/login")
    yield driver
    driver.quit()

@allure.suite("Authentication")
@allure.sub_suite("Logout")
@pytest.mark.usefixtures("driver")
@pytest.mark.run(order=3)
class TestLogoutFunctionality:
    @allure.story("Logout Functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_logout(self, driver):
        """Test the logout functionality."""
        test_name = "test_user_logout"
        try:
            with allure.step("Login with valid credentials"):
                driver.find_element(By.XPATH, "//input[@placeholder='Enter your email address']").send_keys("test45@yopmail.com")
                driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Tester@1234")
                driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()
                WebDriverWait(driver, 10).until(EC.url_contains("/"))
                time.sleep(4)
            with allure.step("Click on profile icon"):
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//button[.//span[contains(@class, 'avatar-container')]]"))
                )
                profile_icon = driver.find_element(By.XPATH, "//button[.//span[contains(@class, 'avatar-container')]]")
                profile_icon.click()

            with allure.step("Click on log out button"):
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Log out')]"))
                )
                logout_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Log out')]")
                logout_button.click()

            with allure.step("Verify successful logout"):
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]")
                ))
                assert driver.current_url == "https://copper-ai-agent-dev.yavar.ai/login", "Logged out successfully."

            take_screenshot(driver, test_name)  # Screenshot on pass

        except Exception as e:
            take_screenshot(driver, f"{test_name}_failure")  # Screenshot on failure
            raise
