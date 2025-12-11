import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.first_name = (By.NAME, "first_name")
        self.last_name = (By.NAME, "last_name")
        self.email = (By.NAME, "email")
        self.org_name = (By.NAME, "organization_name")
        self.phone = (By.XPATH, "//input[@placeholder='Enter phone number']")
        self.signup_btn = (By.XPATH, "//button[contains(text(),'Sign Up')]")

        self.verify_email_text = (By.XPATH, "//*[contains(text(),'Verify your email')]")


    def click_sign_up_btn(self):
        signup_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign Up')]"))
        )
        signup_btn.click()

    def fill_signup_form(self, fname, lname, email, org, phone):

        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(fname)
        self.wait.until(EC.visibility_of_element_located(self.last_name)).send_keys(lname)
        self.wait.until(EC.visibility_of_element_located(self.email)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.org_name)).send_keys(org)
        self.wait.until(EC.visibility_of_element_located(self.phone)).send_keys(phone)
        self.wait.until(EC.element_to_be_clickable(self.signup_btn)).click()

    def verify_email_screen(self):
        self.wait.until(EC.visibility_of_element_located(self.verify_email_text))


class YopmailPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_yopmail(self, email):
        # Open Yopmail in new tab
        self.driver.switch_to.new_window(WindowTypes.TAB)
        self.driver.get("https://yopmail.com/en/")

        field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your inbox here']"))
        )
        field.clear()
        field.send_keys(email)

        # Load inbox
        self.driver.find_element(By.XPATH, "//button[contains(@title,'Check Inbox')]").click()
        time.sleep(2)

        # Refresh inbox one time only
        self.driver.find_element(By.ID, "refresh").click()
        time.sleep(10)

        # Switch to email frame
        self.driver.switch_to.frame("ifmail")

    def open_verification_link(self):
        # Already inside iframe here based on previous method

        verify_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Verify Email & Set Password')]"))
        ).get_attribute("href")


        # Click using JS to ensure new tab opens
        # self.driver.execute_script("arguments[0].click();", verify_btn)

        # Step 1: leave iframe
        self.driver.switch_to.default_content()

        self.driver.switch_to.new_window(WindowTypes.TAB)
        self.driver.get(verify_btn)


        # # Step 2: wait till new tab opens
        # WebDriverWait(self.driver, 10).until(
        #     lambda d: len(d.window_handles) > 2
        # )
        #
        # # Step 3: switch to the latest tab
        # new_tab = self.driver.window_handles[-1]
        # self.driver.switch_to.window(new_tab)


class PasswordSetupPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def set_password(self, password):
        pwd = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "new_password"))
        )
        pwd.send_keys(password)

        conf_pwd = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "confirm_password"))
        )
        conf_pwd.send_keys(password)

        self.driver.find_element(
            By.XPATH, "//button[contains(text(),'Confirm Password')]"
        ).click()

    def go_to_dashboard(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Go to Dashboard')]"))
        )
        btn.click()
