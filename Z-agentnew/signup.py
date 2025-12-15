import os

import pytest
import allure
from time import sleep
import time


import yaml

from pages.signup_page import SignupPage, YopmailPage, PasswordSetupPage
from utils.data_generator import (
    generate_first_name,
    generate_last_name,
    generate_email,
    generate_org_name,
    generate_phone_number
)
from utils.screenshot import take_screenshot
from utils.window_helper import close_other_tabs

@pytest.mark.usefixtures("driver")
class TestSignup:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Runs automatically before each test"""
        self.driver = driver
        self.login_page = SignupPage(self.driver)


        config_path = os.path.join(os.getcwd(), "config", "config.yaml")
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

        base_url = self.config.get("base_url")
        if base_url:
            self.driver.get(base_url)
        else:
            raise ValueError("base_url not found in config.yaml")



    @pytest.mark.dependency(name="signup_done")
    @allure.story("Signup Form")
    def test_submit_signup_form(self, driver):
        signup = SignupPage(driver)
        signup.click_sign_up_btn()

        fname = generate_first_name()
        lname = generate_last_name()
        email = generate_email()
        org = generate_org_name()
        phone = generate_phone_number()

        # Save email for next test
        self.__class__.email_value = email

        signup.fill_signup_form(fname, lname, email, org, phone)
        signup.verify_email_screen()

        take_screenshot(driver, "signup_form_submitted")

    @pytest.mark.dependency(depends=["signup_done"], name="email_verification")
    @allure.story("Verify Email from Yopmail")
    def test_verify_email_from_yopmail(self, driver):
        yopmail = YopmailPage(driver)
        yopmail.open_yopmail(TestSignup.email_value)
        sleep(3)
        yopmail.open_verification_link()
        # close_other_tabs(driver, keep_last=1)
        take_screenshot(driver, "yopmail_verification_clicked")

    @pytest.mark.dependency(name="password_set")
    @allure.story("Set Password")
    def test_set_password(self, driver):
        pwd_page = PasswordSetupPage(driver)
        time.sleep(3)
        password = "Test@123"
        pwd_page.set_password(password)
        pwd_page.go_to_dashboard()
        # close_other_tabs(driver, keep_last=1)
        take_screenshot(driver, "password_set_success")
