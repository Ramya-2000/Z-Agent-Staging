import os
import random
import time

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC,wait
from selenium.webdriver.support.wait import WebDriverWait

from utils.data_generator import get_random_file_path, get_unique_random_file

class KnowledgeBasePage:
    def __init__(self, driver):
        self.driver=driver

        self.next_btn= (By.XPATH, "//button[text()='Next']")

        self.file_upload_document =(By.XPATH,"//button[contains(text(),'Upload Document')]")
        self.click_here_btn =(By.XPATH,"//span[text(),'Click here')]")
        self.upload_cancel_btn= (By.XPATH, "//button[text()='Cancel']")
        self.upload_file_btn= (By.XPATH, "//button[text()='Upload File']")
        self.add_more_btn = (By.XPATH, "//button[text()='Add more']")
        self.remove_btn = (By.XPATH, "//button[@aria-label='Remove Yavar.docx']")
        self.upload_success_msg =(By.XPATH, "//div[contains(text(),'Document uploaded successfully!')]")
        self.upload_file=(By.XPATH, "//input[@type='file']")
        self.folder_path = r"C:\Users\admin\PycharmProjects\ZagentStage\Z-agentnew\files"
        self.all_files = [
            f for f in os.listdir(self.folder_path)
            if os.path.isfile(os.path.join(self.folder_path, f))
        ]
        self.selected_files = []

        self.file_upload_view= (By.XPATH, "//button[@title='preview file']")
        self.file_download =(By.XPATH, "//button[@title='Download Data Source']")
        self.file_delete =(By.XPATH, "//button[@title='Delete Data Source']")
        self.file_cancel =(By.XPATH, "//button[@title='Cancel']")
        self.file_confirm_delete =(By.XPATH, "//button[@title='Delete']")

        self.file_upload_success_msg=(By.XPATH, "//div[contains(text(),'Document uploaded successfully!')]")
        self.file_delete_success_msg=(By.XPATH, "//div[contains(text(),'Data source deleted successfully')]")

        self.duplication_msg = (By.XPATH, "//div[contains(text(),'File duplications are not allowed')]")

        self.connected_apps=(By.XPATH, "//button[normalize-space(.)='Connected Apps']")
        self.connect_other_apps= (By.XPATH, "//button[normalize-space()='Connect other apps']")

        self.connect_onedrive_files =(By.XPATH, "//button[@aria-label='Connect OneDrive']")
        self.connect_google_drive_files =(By.XPATH, "//button[@aria-label='Connect Google Drive']")

        self.success_onedrive_msg =(By.XPATH, "//div[contains(text(),'Microsoft login successful')]")
        self.success_google_drive_msg =(By.XPATH, "//div[contains(text(),'Google login successful')]")

        self.websites=(By.XPATH, "//button[normalize-space(.)='Websites']")
        self.add_website_btn =(By.XPATH, "//button[normalize-space(.)='Add Website']")
        self.add_website=(By.XPATH, "//div[contains(@class,'flex') and .//p[normalize-space()='Data Sources']]//button[normalize-space()='Add Website']")
        self.website_url=(By.XPATH, "//input[@placeholder='https://www.yavar.ai/']")
        self.website_cancel_btn=(By.XPATH, "//button[normalize-space(.)='Cancel']")
        self.add_website_url =(By.XPATH, "//button[normalize-space(.)='Add website']")
        self.success_msg_website_added =(By.XPATH, "//div[contains(text(), 'Website URL added successfully, select the links to ingest')]")

        self.checkbox_webpages =(By.CSS_SELECTOR, "button[role='checkbox']")
        self.ingest_btn =(By.XPATH, "//button[text()='Ingest']")
        self.cancel_btn=(By.XPATH, "//button[normalize-space()='Cancel']")
        self.ingesting_msg = (By.XPATH, "//div[contains(text(), 'Website ingestion started!')]")

        self.website_view=(By.XPATH, "//button[@title='View']")
        self.website_delete=(By.XPATH, "//button[@title='Delete Data Source']")
        self.website_edit=(By.XPATH, "//button[normalize-space()='Edit']")
        self.revert_changes=(By.XPATH, "//button[normalize-space()='Revert Changes']")
        self.website_cancel_btn=(By.XPATH, "//button[normalize-space()='Cancel']")
        self.website_save_changes_btn =(By.XPATH, "//button[normalize-space()='Save Changes']")
        self.update_success_msg=(By.XPATH, "//div[contains(text(), 'Website Ingestion updated successfully')]")

        self.delete_data_source=(By.XPATH, "//button[@title='Delete Data Source']")
        self.cancel_btn_data_source=(By.XPATH, "//button[text()='Cancel']")
        self.confirm_delete_btn=(By.XPATH, "//button[text()='Delete']")
        self.delete_data_source_msg =(By.XPATH, "//div[contains(text(),'Data source deleted successfully')]")


        self.next_btn_to_bot_settings=(By.XPATH, "//button[normalize-space()='Next']")


    @allure.step("Click on File Upload button")
    def file_upload(self):
        time.sleep(5)
        next_btn=self.driver.find_element(*self.next_btn)
        if next_btn.is_enabled():
            print("Next button is enabled")
        else:
            print("Next button is disabled")
        next_btn.click()
        time.sleep(3)
        self.driver.find_element(*self.file_upload_document).click()
        time.sleep(3)

        # 1. Folder containing your files
        folder_path = r"C:\Users\admin\PycharmProjects\ZagentStage\Z-agentnew\files"

        # 2. Get all file names inside the folder
        all_files = os.listdir(folder_path)
        print("all filesss", all_files)

        # 4. Pick a random file
        random_file = random.choice(all_files)

        # 5. Build full file path
        file_path = os.path.join(folder_path, random_file)
        print("Uploading file:", file_path)

        # -------- Upload the random file --------
        file_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(file_path)

        time.sleep(3)
        # After both uploads → click final Upload button
        print("Clicking Upload File button...")
        time.sleep(3)
        self.driver.find_element(*self.upload_file_btn).click()

        wait = WebDriverWait(self.driver, 50)
        file_msg_elt = wait.until(
            EC.visibility_of_element_located(self.file_upload_success_msg)
        )
        assert "Document uploaded successfully!" in file_msg_elt.text


    def upload_two_random_files_loop(self):

        file_input = self.driver.find_element(*self.upload_file)

        # Loop 2 times to upload 2 random files
        for i in range(2):

            # Pick a random file each iteration
            file_path = get_unique_random_file(self.folder_path, self.all_files, self.selected_files)
            print(f"Uploading random file {i + 1}: {file_path}")

            file_input.send_keys(file_path)
            time.sleep(2)

        # After both uploads → click final Upload button
        print("Clicking Upload File button...")
        time.sleep(3)
        self.driver.find_element(*self.upload_file_btn).click()
        time.sleep(10)

        wait = WebDriverWait(self.driver, 20)
        file_msg_elt = wait.until(
            EC.presence_of_element_located(self.file_upload_success_msg))
        assert "Document uploaded successfully!" in file_msg_elt.text

    def random_file_duplication(self):
        wait = WebDriverWait(self.driver, 10)

        file_input = wait.until(
            EC.element_to_be_clickable(self.upload_file)
        )
        file_path = get_random_file_path(self.folder_path, self.selected_files)
        file_input.send_keys(file_path)

        msg_element = wait.until(
            EC.visibility_of_element_located(self.duplication_msg)
        )
        assert "File duplications are not allowed" in msg_element.text


    def file_view(self):
        time.sleep(3)
        print("file detailsss")
        self.driver.find_element(*self.file_upload_view).click()
        time.sleep(3)
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()
        time.sleep(3)
        self.driver.find_element(*self.file_download).click()
        time.sleep(3)
        self.driver.find_element(*self.file_delete).click()
        time.sleep(2)
        self.driver.find_element(*self.file_cancel).click()

    def file_confirm_delete(self):
        self.file_view()
        self.driver.find_element(*self.file_delete).click()
        time.sleep(2)
        self.driver.find_element(*self.file_confirm_delete).click()
        wait = WebDriverWait(self.driver, 10)

        msg_element = wait.until(
            EC.visibility_of_element_located(self.file_delete_success_msg)
        )
        assert "Data source deleted successfully" in msg_element.text

    def connected_apps_upload(self):
        time.sleep(3)
        self.driver.find_element(*self.connected_apps).click()
        time.sleep(3)
        self.driver.find_element(*self.connect_other_apps).click()
        time.sleep(3)
        self.driver.find_element(*self.connect_onedrive_files).click()
        time.sleep(3)

        wait = WebDriverWait(self.driver, 20)

        # Switch to Microsoft login window
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # Step 1: Enter email
        wait.until(EC.visibility_of_element_located((By.ID, "i0116"))).send_keys("ramya.p@yavar.ai")
        self.driver.find_element(By.ID, "idSIButton9").click()

        # Step 2: Enter password
        wait.until(EC.visibility_of_element_located((By.ID, "i0118"))).send_keys("Iamdaugtherofbaby@6383")
        self.driver.find_element(By.ID, "idSIButton9").click()

        # Step 3: Stay signed in? → Yes
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        wait = WebDriverWait(self.driver, 20)

        msg_element = wait.until(
            EC.visibility_of_element_located(self.success_onedrive_msg)
        )
        assert "Microsoft login successful" in msg_element.text

        self.driver.find_element(*self.connect_google_drive_files).click()
        time.sleep(3)
        drive_msg_element = wait.until(
            EC.visibility_of_element_located(self.success_google_drive_msg)
        )
        assert "Google login successful" in drive_msg_element.text

    # def upload_onedrive_files(self):






    def web_scrapping_logic(self):
        time.sleep(5)
        self.driver.find_element(*self.next_btn).click()
        time.sleep(10)
        self.driver.find_element(*self.websites).click()
        time.sleep(2)
        try:
        # Try clicking "Add website"
            add_website = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(.)='Add Website']"))
            )
            add_website.click()
            print("Clicked: Initial Add Website")

        except Exception:
        # If not found, click "Add website another"
            website_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(.)='Websites']"))
            )
            website_btn.click()
            print("Clicked: Another add website")

        website_list = [
            "https://www.yavar.ai/",
            "https://www.aisats.in/",
            "https://www.mkimmigrationlaw.com/"
        ]
        # Pick a random URL
        random_url = random.choice(website_list)

        # Type into the input field
        self.driver.find_element(*self.website_url).send_keys(random_url)
        time.sleep(2)
        self.driver.find_element(*self.add_website_url).click()

        wait = WebDriverWait(self.driver, 30)
        success_injection = wait.until(
            EC.visibility_of_element_located(self.success_msg_website_added))
        print("success_injection", success_injection)
        assert "Website URL added successfully, select the links to ingest" in success_injection.text

        checkboxes= self.driver.find_elements(*self.checkbox_webpages)
        total = len(checkboxes)

        # Choose 2–4 random checkboxes
        num_to_unselect = min(random.randint(2, 4), total)
        if num_to_unselect == 0:
            raise Exception("No checkboxes found to unselect")

        random_boxes = random.sample(checkboxes, num_to_unselect)

        for cb in random_boxes:
            # Scroll checkbox into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cb)
            time.sleep(2)

            # Uncheck it if selected
            if cb.get_attribute("data-state") == "checked":
                cb.click()
                print("Unchecked:", cb)
            else:
                print("Already unchecked:", cb)
        ingest_button = self.driver.find_element(*self.ingest_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ingest_button)
        ingest_button.click()
        time.sleep(5)

        ingesting_message= WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.ingesting_msg)
        )
        print("success message", ingesting_message.text)

    def web_scrapping_view_edit(self):
        time.sleep(3)
        self.driver.find_element(*self.website_view).click()
        time.sleep(3)
        self.driver.find_element(*self.website_edit).click()
        time.sleep(2)

        checkboxes = self.driver.find_elements(*self.checkbox_webpages)
        total = len(checkboxes)

        # Choose 2–4 random checkboxes
        num_to_unselect = min(random.randint(2, 4), total)
        if num_to_unselect == 0:
            raise Exception("No checkboxes found to unselect")

        random_boxes = random.sample(checkboxes, num_to_unselect)

        for cb in random_boxes:
            # Scroll checkbox into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cb)
            time.sleep(2)

            # Uncheck it if selected
            if cb.get_attribute("data-state") == "checked":
                cb.click()
                print("Unchecked:", cb)
            else:
                print("Already unchecked:", cb)

        self.driver.find_element(*self.website_save_changes_btn).click()
        wait = WebDriverWait(self.driver, 20)
        website_update_msg = wait.until(
            EC.visibility_of_element_located(self.update_success_msg))
        print("update msg website", website_update_msg)
        assert "Website Ingestion updated successfully" in website_update_msg.text

    def web_scrapping_revert_changes(self):
        time.sleep(2)
        self.driver.find_element(*self.website_view).click()
        time.sleep(3)
        self.driver.find_element(*self.website_edit).click()
        time.sleep(2)

        checkboxes = self.driver.find_elements(*self.checkbox_webpages)
        total = len(checkboxes)

        # Choose 2–4 random checkboxes
        num_to_unselect = min(random.randint(2, 4), total)
        if num_to_unselect == 0:
            raise Exception("No checkboxes found to unselect")

        random_boxes = random.sample(checkboxes, num_to_unselect)

        for cb in random_boxes:
            # Scroll checkbox into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cb)
            time.sleep(2)

            # Uncheck it if selected
            if cb.get_attribute("data-state") == "checked":
                cb.click()
                print("Unchecked:", cb)
            else:
                print("Already unchecked:", cb)

        self.driver.find_element(*self.revert_changes).click()
        time.sleep(2)
        self.driver.find_element(*self.website_cancel_btn).click()
        print("reverted changesssssssssssss")
        time.sleep(3)
        self.next_btn_to_bot_settings=(By.XPATH, "//button[normalize-space()='Next']")

    def delete_data_source(self):
        time.sleep(2)
        self.driver.find_element(*self.delete_data_source).click()
        time.sleep(2)
        self.driver.find_element(*self.cancel_btn_data_source).click()
        time.sleep(2)
        self.driver.find_element(*self.delete_data_source).click()
        time.sleep(2)
        self.driver.find_element(*self.confirm_delete_btn).click()
        wait = WebDriverWait(self.driver, 10)

        del_msg = wait.until(
            EC.visibility_of_element_located(self.delete_data_source_msg)
        )
        assert "Data source deleted successfully" in del_msg.text
















