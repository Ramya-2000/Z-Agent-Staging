import pytest
import allure
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.read_data import get_data_from_excel

def test_data_from_excel():
    data = get_data_from_excel("data/test_data.xlsx", "Login")
    for row in data:
        email, password = row
        print(f"Email: {email}, Password: {password}")



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
    service = Service("C:\\Users\\admin\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    # Use the URL you gave
    # driver.get("https://web.zagent.stage.yavar.ai/")
    driver.get("https://web.zagent.stage.yavar.ai/bots")
    time.sleep(2)


    # ✅ Set the persist:root localStorage value (your provided JSON)
    persist_data = r"""{
          "auth": "{\"email\":\"ramya.p@yavar.ai\",\"id\":\"9f812baa-37d5-414c-bd2c-7de96017908d\",\"username\":null,\"account_id\":\"8e9a3514-c5e8-52e7-842d-cb4e2a0a0cdb\",\"is_active\":true,\"role\":\"ADMIN\",\"product\":\"Z-AGENT\",\"product_url\":\"https://app.20.242.183.197.nip.io\",\"sign_up\":false,\"access_token\":\"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjlmODEyYmFhLTM3ZDUtNDE0Yy1iZDJjLTdkZTk2MDE3OTA4ZCIsImVtYWlsIjoicmFteWEucEB5YXZhci5haSIsImV4cCI6MTc2MjkyMjI5NSwiYWNjb3VudF9pZCI6IjhlOWEzNTE0LWM1ZTgtNTJlNy04NDJkLWNiNGUyYTBhMGNkYiJ9.D2mn65AZjrrdXznAQqkmmbKvSV9DF0imL4pAwietUwk\"}",
          "_persist": "{\"version\":-1,\"rehydrated\":true}"
      }"""

    # ✅ Inject into localStorage
    driver.execute_script(f"window.localStorage.setItem('persist:root', `{persist_data}`);")
    driver.execute_script(f"window.localStorage.setItem('username', 'Ramya P');")

    # ✅ Reload so app picks up the new auth state
    driver.refresh()
    time.sleep(20)

    yield driver
    # driver.quit()

@allure.suite("Authentication")
@allure.sub_suite("Login")
@pytest.mark.usefixtures("driver")
class TestLogin:

    # def test_create_bot(self, driver):
    #     page = LetsGetStarted(driver)
    #     page.lets_gets_started()

    @allure.story("Blank Fields")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_blank_fields(self, driver):
        test_name = "test_blank_fields"
        driver.refresh()
        try:
            pass
        #     checkbox = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "//button[@id='terms']"))
        #     )
        #     if not checkbox.is_selected():
        #         checkbox.click()
        #     assert not checkbox.is_selected()
        #     btn = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))
        #     )
        #     btn.click()
        #
        #     # check expected error messages for missing email/password
            #assert "Invalid email address" in driver.page_source or "Enter email" in driver.page_source
           # assert "Password is required" in driver.page_source or "Enter password" in driver.page_source

            #take_screenshot(driver, test_name)
        except AssertionError as e:
            take_screenshot(driver, f"{test_name}_failure")
            raise

#     @pytest.mark.parametrize("email", ["invalid", "test@", "user@", "plainaddress", "@domain.com"])
#     @allure.story("Invalid Email Format")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_invalid_email_formats(self, driver, email):
#         test_name = f"test_invalid_email_{email}"
#         try:
#             email_ele = driver.find_element(By.XPATH, "//input[@type='email']")
#             email_ele.clear()
#             email_ele.send_keys(email)
#
#             password_ele = driver.find_element(By.XPATH, "//input[@type='password']")
#             password_ele.clear()
#             password_ele.send_keys("Test@123")
#
#             driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
#
#             # Wait for an error message about invalid email
#             WebDriverWait(driver, 5).until(
#                 EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'valid email')]"))
#             )
#             take_screenshot(driver, test_name)
#         except Exception as e:
#             take_screenshot(driver, f"{test_name}_failure")
#             raise
