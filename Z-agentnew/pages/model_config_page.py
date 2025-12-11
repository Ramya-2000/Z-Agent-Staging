import time

from selenium.webdriver.support import expected_conditions as EC,wait

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.data_generator import generate_top_k, generate_chunk_size, generate_chunk_overlap


class ModelConfigPage:
    def __init__(self, driver):
        self.driver=driver

        self.config_btn= (By.XPATH, "//button[normalize-space()='Configure Bot']")

        self.llm_save_btn= (By.XPATH, "//button[@title='Save']")
        self.vector_save_btn = (By.XPATH, "//h4[text()='Vector DB Configuration']/following::button[contains(., 'Save')][1]")
        self.expand_model_config =(By.XPATH, "//button[.//h4[normalize-space()='LLM Model Configuration']]")
        self.expand_vectordb_config =(By.XPATH, "//button[.//h4[normalize-space()='Vector DB Configuration']]")

        self.next_btn= (By.XPATH, "//button[normalize-space()='Next']")
        self.back_btn = (By.XPATH, "//button[normalize-space()='Back']")
        self.llm_provider = (By.XPATH, "//label[contains(text(),'Select LLM Provider')]//following::div[text()='Select from the list'][1]")
        self.choose_llm_provider=(By.XPATH, "//div[@role='option' and text()='GeminiAI']")
        self.llm_model = (By.XPATH, "//label[contains(text(),'Select LLM Model')]//following::div[text()='Select from the list'][1]")
        self.llm_enter_api_key=(By.XPATH, "//input[@name='llm_api_key']")
        self.embedding_enter_api_key= (By.XPATH, "//input[@name='embedding_api_key']")
        self.embedding_provider = (By.XPATH, "//label[contains(text(),'Select Embedding Provider')]//following::div[text()='Select from the list'][1]")
        self.embedding_model= (By.XPATH, "//label[contains(text(),'Select Embedding Model')]//following::div[text()='Select from the list'][1]")
        self.click_vector_db= ( By.XPATH, "//div[text()='Select Vector DB Value']")

        self.llm_success_msg =(By.XPATH, "//div[contains(text(),'Configuration saved successfully')]")
        self.vector_db_msg=(By.XPATH, "//div[contains(text(),'Vector DB settings configured successfully.')]")

        self.llm_provider_value= (By.XPATH, "//div[@role='option' and text()='GeminiAI']")
        self.llm_model_value =(By.XPATH, "//div[text()='gemini-2.5-flash']")

        self.embedding_provider_value=(By.XPATH,"//div[@id='react-select-4-option-0' and text()='GeminiAI']")
        self.embedding_model_value=(By.XPATH, "//div[@id='react-select-5-option-2' and text()='text-embedding-004']")


        self.llm_model_validation = (By.XPATH, "//p[contains(text(),'LLM Model is required')]")
        self.llm_api_key_validation= (By.XPATH, "//p[contains(text(),'LLM API key is required')]")
        self.embedding_provider_validation = (By.XPATH, "//p[contains(text(), 'LLM Model is required')]")
        self.embedding_model_validation =(By.XPATH, "//p[contains(text(), 'Embedding Model is required')]")
        self.embedding_api_key_validation = (By.XPATH, "//p[contains(text(), 'Embedding API key is required')]")

        self.db_value=(By.XPATH, "//div[text()='PG_VECTOR']")
        self.top_k_value=(By.XPATH, "//input[@placeholder='Enter top_k value']")
        self.chunk_size =(By.XPATH, "//input[@placeholder='Enter Chunk Size']")
        self.chunk_overlap=(By.XPATH, "//input[@placeholder='Enter Chunk Overlap']")
        self.top_k_error_msg = (By.XPATH, "//p[text()='Top_k is required']")
        self.chunk_size_error_msg = (By.XPATH, "//p[text()='Chunk size is required']")
        self.chunk_overlap_error_msg = (By.XPATH, "//p[text()='Chunk overlap is required']")

    def next_btn_disabled(self):
        time.sleep(3)
        self.driver.find_element(*self.config_btn).click()
        # next_button =self.driver.find_element(*self.next_btn)
        #
        # assert not next_button.is_enabled(), "next button must be disabled"
        # print("next btn disabled correctly")
        time.sleep(5)
        self.driver.find_element(*self.expand_model_config).click()
        time.sleep(4)

        self.driver.find_element(*self.llm_provider).click()
        wait = WebDriverWait(self.driver, 15)

        option = wait.until(EC.element_to_be_clickable(self.choose_llm_provider))
        option.click()
        time.sleep(2)
        self.driver.find_element(*self.llm_save_btn).click()
        time.sleep(2)

        validation_msg_llm_model = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.llm_model_validation)
        )
        print(" validation_msg_llm_model message:", validation_msg_llm_model.text)

        validation_msg_llm_api_key = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.llm_api_key_validation)
        )
        print(" validation_msg_llm api key message:", validation_msg_llm_api_key.text)

        validation_msg_embedding_provider = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.embedding_provider_validation)
        )
        print(" validation_msg embedding provider message:", validation_msg_embedding_provider.text)

        validation_msg_embedding_model = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.embedding_model_validation)
        )
        print(" validation_msg embedding message:", validation_msg_embedding_model.text)

        validation_msg_embedding_api_key = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.embedding_api_key_validation)
        )
        print(" validation_msg embedding api key message:", validation_msg_embedding_api_key.text)
        time.sleep(3)
        self.driver.find_element(*self.llm_save_btn).click()

    def valid_llm_details(self):
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element(*self.expand_model_config).click()
        time.sleep(2)

        self.driver.find_element(*self.llm_provider).click()
        time.sleep(3)

        self.driver.find_element(*self.llm_provider_value).click()
        time.sleep(3)

        self.driver.find_element(*self.llm_model).click()
        time.sleep(1)

        self.driver.find_element(*self.llm_model_value).click()
        time.sleep(3)

        self.driver.find_element(*self.llm_enter_api_key).send_keys("AIzaSyAcDz50H--5MQ3qcVLql89nKbTJYysiVug")

        self.driver.find_element(*self.embedding_provider).click()
        time.sleep(2)
        self.driver.find_element(*self.embedding_provider_value).click()

        self.driver.find_element(*self.embedding_model).click()
        time.sleep(5)
        self.driver.find_element(*self.embedding_model_value).click()

        self.driver.find_element(*self.embedding_enter_api_key).send_keys("AIzaSyAcDz50H--5MQ3qcVLql89nKbTJYysiVug")
        time.sleep(2)
        self.driver.find_element(*self.llm_save_btn).click()
        wait = WebDriverWait(self.driver, 10)

        msg_element = wait.until(
            EC.visibility_of_element_located(self.llm_success_msg)
        )
        assert "Configuration saved successfully" in msg_element.text

    def with_vector_db(self):
        time.sleep(2)
        self.driver.find_element(*self.expand_vectordb_config).click()
        time.sleep(2)
        self.driver.find_element(*self.click_vector_db).click()
        time.sleep(3)
        self.driver.find_element(*self.db_value).click()
        print("db value selecteddddddddddddd")
        time.sleep(4)
        element = self.driver.find_element(*self.vector_save_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

        top_error_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.top_k_error_msg)
        ).text
        print("Validation Message:", top_error_msg)

        top_chunk_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.chunk_size_error_msg)
        ).text
        print("Validation Message:", top_chunk_msg)

        top_chunk_overlap_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.chunk_overlap_error_msg)
        ).text
        print("Validation Message:", top_chunk_overlap_msg)

    def valid_vector_db_configuration(self):

        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element(*self.expand_vectordb_config).click()
        time.sleep(3)
        self.driver.find_element(*self.click_vector_db).click()
        time.sleep(3)
        self.driver.find_element(*self.db_value).click()
        print("db value selected")
        time.sleep(2)

        top_k_value_generate=generate_top_k()
        self.driver.find_element(*self.top_k_value).send_keys(top_k_value_generate)

        chunk_size_generate= generate_chunk_size()
        self.driver.find_element(*self.chunk_size).send_keys(chunk_size_generate)

        chunk_overlap_generate=generate_chunk_overlap()
        self.driver.find_element(*self.chunk_overlap).send_keys(chunk_overlap_generate)

        element = self.driver.find_element(*self.vector_save_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

        success_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.vector_db_msg)
        )
        print("success message", success_msg.text)
        assert "Vector DB settings configured successfully." in success_msg.text, "vector db message not displayed!"
        time.sleep(3)


