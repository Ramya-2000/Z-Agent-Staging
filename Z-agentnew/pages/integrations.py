import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC,wait

class IntegrationsPage:
    def __init__(self, driver):
        self.driver = driver

        self.next_button = (By.XPATH, "//button[text()='Next']")
        self.web_integration_expand=(By.XPATH, "//button[.//h3[normalize-space()='Web Integration']]")
        self.copy_url =(By.XPATH, "//button[.//img[@src='/assets/icons/copy.svg']]")
        self.complete_button = driver.find_element(By.XPATH, "//button[text()='Complete setup']")
        self.setup_success_msg=(By.XPATH, "//div[contains(text(),'Bot setup completed successfully')]")

    def integration_module(self):
        time.sleep(4)
        self.driver.find_element(*self.web_integration_expand).click()
        time.sleep(4)
        url =self.driver.find_element(*self.copy_url).get_attribute("value")
        # Step 2: Open a new tab with the URL
        self.driver.execute_script(f"window.open('{url}', '_blank');")

        # Step 3: Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Optional: wait for page to load
        time.sleep(2)

        # Step 4: Switch back to the original tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(4)
        self.driver.find_element(*self.complete_button).click()

        wait = WebDriverWait(self.driver, 20)
        complete_setup_msg = wait.until(
            EC.visibility_of_element_located(self.setup_success_msg)
        )
        assert "Bot setup completed successfully" in complete_setup_msg.text
        time.sleep(2)




