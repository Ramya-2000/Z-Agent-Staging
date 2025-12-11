import pytest
import allure
import os
import time
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
class TestSignup:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Runs automatically before each test"""
        self.driver = driver


        config_path = os.path.join(os.getcwd(), "config", "config.yaml")
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

        base_url = self.config.get("base_url")
        if base_url:
            self.driver.get(base_url)
        else:
            raise ValueError("base_url not found in config.yaml")

def take_screenshot(driver, test_name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)
    allure.attach.file(
        screenshot_path,
        name=test_name,
        attachment_type=allure.attachment_type.PNG
    )

# -------------------- Test Suite --------------------
@allure.suite("Authentication")
@allure.sub_suite("Signup")
@pytest.mark.usefixtures("driver")
class TestSignup:

    # ---------- Negative Test: Blank Fields ----------
    @allure.story("Blank Fields")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_blank_fields(self, driver):
        test_name = "test_blank_fields"
        driver.refresh()
        try:
            signup_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign Up')]"))
            )
            signup_btn.click()

            # Check error messages
            assert "required" in driver.page_source or "Please fill" in driver.page_source
            take_screenshot(driver, test_name)
        except AssertionError:
            take_screenshot(driver, f"{test_name}_failure")
            raise

    # ---------- Positive Test: Valid Signup ----------
    @allure.story("Valid Signup")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_signup(self, driver):
        test_name = "test_valid_signup"
        try:
            driver.refresh()
            wait = WebDriverWait(driver, 15)

            # Fill valid signup details
            wait.until(EC.visibility_of_element_located((By.NAME, "first_name"))).send_keys("Abarna")
            wait.until(EC.visibility_of_element_located((By.NAME, "last_name"))).send_keys("S")
            email_value = "abarna07@yopmail.com"
            wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(email_value)
            wait.until(EC.visibility_of_element_located((By.NAME, "organization_name"))).send_keys("Yavar Tech")
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter phone number']"))).send_keys("9876543210")

            signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign Up')]")))
            signup_btn.click()

            # Verify navigation to "Verify your email" page
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Verify your email')]"))
            )

            take_screenshot(driver, test_name)

            # ---------- Step 2: Go to Yopmail ----------
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get("https://yopmail.com/en/")

            email_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your inbox here']"))
            )
            email_field.clear()
            email_field.send_keys(email_value)
            driver.find_element(By.XPATH, "//button[contains(@title, 'Check Inbox @yopmail.com')]").click()
            sleep(5)

            driver.find_element(By.ID, "refresh").click()
            sleep(10)
            driver.switch_to.frame("ifmail")

            verify_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Verify Email & Set Password')]"))
            )
            verify_btn.click()

            # ---------- Step 3: Set Password ----------
            driver.switch_to.default_content()
            driver.switch_to.window(driver.window_handles[2])

            pwd_field = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.NAME, "new_password"))
            )
            pwd_field.send_keys("Test@123")

            next_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
            next_btn.click()

            # Confirm Password Page
            confirm_pwd = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.NAME, "confirm_password"))
            )
            confirm_pwd.send_keys("Test@123")

            confirm_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Confirm Password')]")
            confirm_btn.click()

            # # ---------- Step 4: Confirmation Page ----------
            # WebDriverWait(driver, 15).until(
            #     EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'You're All Set!')]"))
            # )

            go_dashboard = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Go to Dashboard')]"))
            )
            go_dashboard.click()

            take_screenshot(driver, f"{test_name}_completed")

        except Exception as e:
            print(f"Error: {e}")
            take_screenshot(driver, f"{test_name}_failure")
            raise
