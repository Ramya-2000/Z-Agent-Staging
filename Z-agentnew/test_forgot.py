from time import sleep

import pytest
import allure
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_screenshot(driver, test_name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)
    allure.attach.file(screenshot_path, name=test_name, attachment_type=allure.attachment_type.PNG)

@pytest.fixture(scope="class")
def driver():
    # Adjust path to your chromedriver
    service = Service("C:\\Users\\admin\\Documents\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    # Use the URL you gave
    driver.get("https://web.zagent.stage.yavar.ai/auth?redirect_uri=%2F")
    yield driver
    driver.quit()

    @allure.story("Forgot Password Flow")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_forgot_password_flow(self, driver):
        test_name = "test_forgot_password_flow"
        try:
            wait = WebDriverWait(driver, 20)

            # Step 1: Click Forgot Password link
            forgot_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Forgot password')]"))
            )
            forgot_link.click()

            # Step 2: Enter registered email ID
            email_field = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='you@company.com']"))
            )
            email_field.clear()
            email_field.send_keys("abarna1234@yopmail.com")

            # Step 3: Click Send Reset Link
            send_link_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Send Reset Link')]"))
            )
            send_link_btn.click()

            # Optional: Wait for success message confirmation
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Reset link sent') or contains(text(),'Check your email')]"))
            )

            take_screenshot(driver, test_name + "_link_sent")

            # Step 4: Open Yopmail in new tab
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get("https://yopmail.com/en/")

            # Step 5: Open Yopmail inbox
            email_input = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your inbox here']"))
            )
            email_input.clear()
            email_input.send_keys("abarna1234@yopmail.com")

            check_btn = driver.find_element(By.XPATH, "//button[contains(@title, 'Check Inbox @yopmail.com')]")
            check_btn.click()

            # Refresh inbox and wait for email
            sleep(5)
            driver.find_element(By.ID, "refresh").click()
            sleep(5)

            # Switch to mail iframe
            driver.switch_to.frame("ifmail")

            # Step 6: Find the reset password link
            reset_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Reset Password')]"))
            )
            reset_url = reset_link.get_attribute("href")
            print(f"Reset Password URL: {reset_url}")

            # Step 7: Open Reset Password link in new tab
            driver.switch_to.default_content()
            driver.execute_script("window.open(arguments[0]);", reset_url)
            driver.switch_to.window(driver.window_handles[2])

            # Step 8: Wait for Reset Password page
            new_pwd_field = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter new password']"))
            )
            confirm_pwd_field = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Confirm new password']"))
            )

            new_pwd_field.send_keys("Test@1234")
            confirm_pwd_field.send_keys("Test@1234")

            # Step 9: Click Reset/Submit button
            reset_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Reset Password')]"))
            )
            reset_btn.click()

            # Step 10: Verify success message or navigation
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Password reset successfully') or contains(text(),'Login')]"))
            )
            take_screenshot(driver, test_name + "_success")

        except Exception as e:
            print(f"Error in forgot password flow: {e}")
            take_screenshot(driver, f"{test_name}_failure")
            raise

