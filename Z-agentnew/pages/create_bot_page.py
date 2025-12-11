import time

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from utils.data_generator import generate_bot_name, generate_invalid_name

class CreateBotPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators only (no find_element here)

        self.cancel_button = (By.XPATH, "//button[text()='Cancel']")

        self.enter_bot_name = (By.XPATH, "//input[@placeholder='Enter your bot name']")
        self.click_create_bot=(By.XPATH, "//button[normalize-space()='Create Bot']")
        self.create_cancel_button = (By.XPATH, "(//div[@class='flex flex-row justify-end gap-4']//button)[1]")
        self.validation_bot_name = (By.XPATH, "//p[text()='Bot name is required']")
        self.success_msg = (By.XPATH, "//*[contains(text(), 'Bot Created Successfully')]")
        self.validation_invalid_bot_name = (By.XPATH, "//p[contains(text(), 'Enter a valid bot name')]")
        self.choose_project_name=(By.XPATH, "//div[text()='Select from below']")
        self.validation_project_type = (By.XPATH, "//p[text()='Project type is required']")
        self.select_project= (By.XPATH, "//div[@role='option' and text()='General']")


        self.update_button = (By.XPATH, "//button[normalize-space()='Update Bot']")
        self.update_cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
        self.update_msg = (By.XPATH, "//*[normalize-space()='Bot Updated Successfully']")

        self.delete_btn = (By.XPATH, "//div[@role='menuitem' and normalize-space()='Delete']")
        self.delete_cancel_btn = (By.XPATH, "//button[normalize-space()='Cancel']")
        self.delete_del_btn = (By.XPATH, "//button[normalize-space()='Delete']")

    @allure.step("Click on Let's Get Started")
    def lets_get_started(self):
        try:
        # Try clicking "Create Bot"
            create_bot = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Create Bot']"))
            )
            create_bot.click()
            print("Clicked: Create Bot")

        except Exception:
        # If not found, click "Create another Bot"
            create_another = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Create another Bot']"))
            )
            create_another.click()
            print("Clicked: Create another Bot")

    #     xpath = "//p[text()='Create Bot' or text()='Create another Bot']"
    #     self.driver.find_element(By.XPATH, xpath).click()
        time.sleep(5)
        bot_button= "//button[@title='Create Bot' or normalize-space()='Create another Bot']"
        self.driver.find_element(By.XPATH,bot_button).click()
        time.sleep(2)

    def click_cancel_btn(self):
        self.driver.find_element(*self.create_cancel_button).click()
        print("cancel clickedddddd")

    def create_btn_disabled(self):

        click_create_bot_btn_dis=self.driver.find_element(*self.click_create_bot)
        assert not click_create_bot_btn_dis.is_enabled(), "Create Bot button should be disabled when Bot Name is empty"
        print("Create Bot is correctly disabled")
        time.sleep(3)

        self.driver.find_element(*self.create_cancel_button).click()
        print("cancel clickedddddd")

    @allure.step("Validate without entering bot name")
    def without_bot_name(self):
        self.lets_get_started()

        bot_name_field=self.driver.find_element(*self.enter_bot_name)
        bot_name_field.click()
        time.sleep(2)

        self.driver.execute_script("arguments[0].blur();", bot_name_field)
        # click empty spot
        time.sleep(2)
        print("clicked outside")


        error_message = WebDriverWait(self.driver, 10).until(
              EC.visibility_of_element_located(self.validation_bot_name)
            ).text
        print("Validation Message:", error_message )
        self.driver.find_element(*self.create_cancel_button).click()

    @allure.step("Validate without entering bot name")
    def enter_invalid_bot_name(self):
        self.lets_get_started()

        invalid_bot_name = generate_invalid_name()
        self.driver.find_element(*self.enter_bot_name).send_keys(invalid_bot_name)
        self.driver.find_element(*self.click_create_bot).click()

        validation_bot_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.validation_invalid_bot_name)
        )
        print("Validation message displayed correctly:", validation_bot_name.text)

        assert validation_bot_name.text == "Enter a valid bot name", f"Unexpected validation: {validation_bot_name.text}"


        validation_project = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.validation_project_type)
        )
        print("Validation message displayed correctly:", validation_project.text)

        assert validation_project.text == "Project type is required", f"Unexpected validation: {validation_project.text}"
        time.sleep(2)
        self.driver.find_element(*self.cancel_button).click()
        print("cancel")

    @allure.step("Enter valid bot name and create bot")
    def with_valid_bot_name(self):
        self.lets_get_started()

        bot_name = generate_bot_name()
        self.driver.find_element(*self.enter_bot_name).send_keys(bot_name)

        self.driver.find_element(*self.choose_project_name).click()
        time.sleep(5)

        wait = WebDriverWait(self.driver, 10)
        option = wait.until(EC.element_to_be_clickable(self.select_project))
        self.driver.execute_script("arguments[0].scrollIntoView();", option)
        self.driver.execute_script('arguments[0].click()', option)


        self.driver.find_element(*self.click_create_bot).click()

        success_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_msg)
        )
        print("success message",success_msg.text)
        assert "Bot Created Successfully" in success_msg.text, "Bot create message not displayed!"

    @allure.step("Edit the bot name")
    def edit_bot_name(self):
        bot_action_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Bot actions']"))
        )
        bot_action_button.click()

        edit_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem'][contains(., 'Edit')]"))
        )
        edit_option.click()

        bot_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.enter_bot_name)
        )

        bot_name_input.click()
        bot_name_input.send_keys(Keys.CONTROL + "a")
        bot_name_input.send_keys(Keys.BACKSPACE)

        # self.driver.find_element(*self.update_button).click()
        # print("update clickeddddddddddddd")
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.validation_bot_name)
        ).text
        print("Edit Validation Message:", error_message)
        self.driver.find_element(*self.update_cancel_button).click()

    @allure.step("Edit valid bot name and update")
    def update_bot_name(self):
        bot_action_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Bot actions']"))
        )
        bot_action_button.click()

        edit_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem'][contains(., 'Edit')]"))
        )
        edit_option.click()

        bot_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.enter_bot_name)
        )
        bot_name_input.clear()

        bot_name = generate_bot_name()
        self.driver.find_element(*self.enter_bot_name).send_keys(bot_name)
        self.driver.find_element(*self.update_button).click()

        update_success_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.update_msg)
        )
        print(update_success_msg.text)
        assert "Bot Updated Successfully" in update_success_msg.text, "Bot update message not displayed!"
        time.sleep(5)

    def delete_bot(self):
        bot_action_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Bot actions']"))
        )
        bot_action_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_btn)
        ).click()
        self.driver.find_element(*self.delete_cancel_btn).click()

    @allure.step("Delete bot")
    def click_confirm_delete_btn(self):
        bot_action_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Bot actions']"))
        )
        bot_action_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_btn)
        ).click()
        self.driver.find_element(*self.delete_del_btn).click()
        delete_success_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Chatbot deleted successfully')]"))
        )
        print("delete message",delete_success_msg.text)
        assert "Chatbot deleted successfully" in delete_success_msg.text, "Bot delete message not displayed!"
