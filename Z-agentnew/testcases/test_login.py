# import pytest
# import allure
# import time
# import yaml
# import os
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pages.login_page import LoginPage
# from utils.screenshot import take_screenshot
#
#
# @allure.suite("Authentication")
# @allure.sub_suite("Login")
# @pytest.mark.usefixtures("driver")   # tells pytest to use the 'driver' fixture from conftest.py
# class TestLogin:
#
#     @pytest.fixture(autouse=True)
#     def setup(self):
#         """Runs automatically before each test"""
#         # ✅ Use self.driver directly (injected by the fixture)
#         self.login_page = LoginPage(self.driver)
#
#         # ✅ Load config.yaml
#         config_path = os.path.join(os.getcwd(), "config", "config.yaml")
#         with open(config_path, "r") as file:
#             self.config = yaml.safe_load(file)
#
#         # ✅ Navigate to base_url
#             base_url = self.config.get("base_url")
#             if base_url:
#                 self.driver.get(base_url)
#             else:
#                 raise ValueError("base_url not found in config.yaml")
#
#     @allure.story("Blank Fields")
#     def test_blank_fields(self):
#         test_name = "test_blank_fields"
#         try:
#             self.driver.refresh()
#             self.login_page.toggle_terms()
#             self.login_page.click_login()
#
#             assert "Email is required" in self.driver.page_source or "Enter email" in self.driver.page_source
#             assert "Password is required" in self.driver.page_source or "Enter password" in self.driver.page_source
#             take_screenshot(self.driver, test_name)
#         except Exception:
#             take_screenshot(self.driver, f"{test_name}_failure")
#             raise
#
#     @pytest.mark.parametrize("email", ["invalid", "test@", "user@", "plainaddress", "@domain.com"])
#     @allure.story("Invalid Email Formats")
#     def test_invalid_email_formats(self, email):
#         test_name = f"test_invalid_email_{email}"
#         try:
#             self.login_page.clear_fields()
#             self.login_page.enter_email(email)
#             self.login_page.enter_password("Test@123")
#             self.login_page.click_login()
#             take_screenshot(self.driver, test_name)
#         except Exception:
#             take_screenshot(self.driver, f"{test_name}_failure")
#             raise
#
#     @allure.story("Password Masking")
#     def test_password_masking(self):
#         test_name = "test_password_masking"
#         try:
#             assert self.login_page.get_password_field_type() == "password"
#             take_screenshot(self.driver, test_name)
#         except AssertionError:
#             take_screenshot(self.driver, f"{test_name}_failure")
#             raise
#
#     @allure.story("Password Toggle")
#     def test_password_toggle(self):
#         test_name = "test_password_toggle"
#         try:
#             self.login_page.enter_password("Test@1234")
#             assert self.login_page.get_password_field_type() == "password"
#             self.login_page.toggle_password_visibility()
#             time.sleep(1)
#             assert self.login_page.get_password_field_type() == "text"
#             self.login_page.toggle_password_visibility()
#             assert self.login_page.get_password_field_type() == "password"
#             take_screenshot(self.driver, test_name)
#         except Exception:
#             take_screenshot(self.driver, f"{test_name}_failure")
#             raise
#
#     @allure.story("Valid Login with OTP")
#     @pytest.mark.order(1)
#     def test_valid_login(self):
#         test_name = "test_valid_login"
#         try:
#             self.login_page.clear_fields()
#             self.login_page.enter_email(self.config["email"])
#             self.login_page.enter_password(self.config["password"])
#             self.login_page.toggle_terms()   # ✅ Added checkbox click here too
#             self.login_page.click_login()
#
#             otp = self.login_page.fetch_otp_from_yopmail(self.config["email"])
#             print (f"Fetched OTP:{otp}")
#
#             # Switch to main window
#             self.driver.switch_to.window(self.driver.window_handles[0])
#             self.driver.switch_to.default_content()
#
#             # Wait for OTP input
#             otp_input = WebDriverWait(self.driver, 20).until(
#                 EC.element_to_be_clickable((By.XPATH, "//input[@name='otp']"))
#             )
#
#             otp_input.send_keys(otp)
#             time.sleep(10)
#
#             take_screenshot(self.driver, test_name)
#         except Exception:
#             take_screenshot(self.driver, f"{test_name}_failure")
#             raise


import pytest
import allure
import time
import yaml
import os


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.screenshot import take_screenshot

@allure.suite("Authentication")
@allure.sub_suite("Login Flow")
@allure.feature("Login Module")
@pytest.mark.usefixtures("driver")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Runs automatically before each test"""
        self.driver = driver
        self.login_page = LoginPage(self.driver)

        config_path = os.path.join(os.getcwd(), "config", "config.yaml")
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

        base_url = self.config.get("base_url")
        if base_url:
            self.driver.get(base_url)
        else:
            raise ValueError("base_url not found in config.yaml")

    @allure.story("Valid Login with OTP")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(name="login_success", scope="session")
    @pytest.mark.order(1)
    def test_valid_login(self, driver):
        test_name = "test_valid_login"
        try:
            self.login_page.clear_fields()
            self.login_page.enter_email(self.config["email"])
            self.login_page.enter_password(self.config["password"])
            self.login_page.toggle_terms()
            self.login_page.click_login()

            otp = self.login_page.fetch_otp_from_yopmail(self.config["email"])
            print(f"Fetched OTP: {otp}")

            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.switch_to.default_content()

            otp_input = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='otp']"))
            )
            otp_input.send_keys(otp)
            time.sleep(5)

            screenshot_path = take_screenshot(self.driver, test_name)
            allure.attach.file(
                screenshot_path,
                name="Successful Login Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        except Exception as e:
            # Attach failure screenshot
            screenshot_path = take_screenshot(self.driver, f"{test_name}_failure")
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise e
