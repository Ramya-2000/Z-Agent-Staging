from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.XPATH, "//input[@placeholder='you@company.com']")
        self.password_input = (By.XPATH, "//input[@placeholder='Enter your password']")
        self.login_button = (By.XPATH, "//button[contains(text(),'Login')]")
        self.checkbox_terms = (By.XPATH, "//button[@id='terms']")
        self.password_eye_icon = (By.CSS_SELECTOR, "button[title='Show/Hide Password']")

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_input)).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

    def toggle_terms(self):
        checkbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkbox_terms))
        checkbox.click()

    def toggle_password_visibility(self):
        self.driver.find_element(*self.password_eye_icon).click()

    def get_password_field_type(self):
        return self.driver.find_element(*self.password_input).get_attribute("type")

    def clear_fields(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_input)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).clear()

    def fetch_otp_from_yopmail(self, email):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://yopmail.com/en/")

        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your inbox here']"))
        )
        email_field.clear()
        email_field.send_keys(email)
        self.driver.find_element(By.XPATH, "//button[contains(@title, 'Check Inbox @yopmail.com')]").click()
        time.sleep(8)
        self.driver.find_element(By.ID, "refresh").click()
        time.sleep(5)

        self.driver.switch_to.frame("ifmail")
        otp_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), '(OTP)')]"))
        ).text
        otp_code = otp_text.split(":")[-1].strip()
        print(f"Extracted OTP: {otp_code}")

        self.driver.switch_to.default_content()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return otp_code

