import allure
import pytest
from pages.model_config_page import ModelConfigPage

@allure.suite("Bot Onboarding")
@allure.sub_suite("Model Configuration")
@pytest.mark.usefixtures("driver")
class TestModelConfig:

    # def test_model_config(self,driver):
    #     model_config_page=ModelConfigPage(driver)
    #     model_config_page.next_btn_disabled()
    #     model_config_page.valid_llm_details()
    #     # model_config_page.with_vector_db()
    #     model_config_page.valid_vector_db_configuration()

    @allure.feature("Model Configuration")
    @allure.story("Next Button Disabled")
    @allure.description("Ensures the Next button is disabled initially before providing LLM details.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends=["create_bot_done"],scope="session")
    @pytest.mark.dependency(name="model_config_done",scope="session")
    @pytest.mark.order(12)
    def test_next_btn_disabled(self, driver):
        model_config_page = ModelConfigPage(driver)
        with allure.step("Verify 'Next' button is disabled"):
            model_config_page.next_btn_disabled()

    # --------------------------
    # 2. Valid LLM Configuration
    # --------------------------
    @allure.feature("Model Configuration")
    @allure.story("Valid LLM Details")
    @allure.description("Fill valid LLM API key and model details.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["create_bot_done"],scope="session")
    @pytest.mark.order(13)
    def test_valid_llm_details(self, driver):
        model_config_page = ModelConfigPage(driver)
        with allure.step("Enter valid LLM configuration details"):
            model_config_page.valid_llm_details()

    # --------------------------
    # 3. With Vector DB (Enable / Toggle)
    # --------------------------
    @allure.feature("Model Configuration")
    @allure.story("Enable Vector DB Option")
    @allure.description("Validates if Vector DB toggle / option works correctly before entering config.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends=["create_bot_done"],scope="session")
    @pytest.mark.order(14)
    def test_with_vector_db(self, driver):
        model_config_page = ModelConfigPage(driver)
        with allure.step("Enable Vector DB configuration option"):
            model_config_page.with_vector_db()

    # --------------------------
    # 4. Valid Vector DB Configuration
    # --------------------------
    @allure.feature("Model Configuration")
    @allure.story("Valid Vector DB Config")
    @allure.description("Fill valid Vector DB connection details.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["create_bot_done"],scope="session")
    @pytest.mark.order(15)
    def test_valid_vector_db_configuration(self, driver):
        model_config_page = ModelConfigPage(driver)
        with allure.step("Enter valid Vector DB configuration"):
            model_config_page.valid_vector_db_configuration()
