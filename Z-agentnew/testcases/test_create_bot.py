# import pytest
# from pages.create_bot_page import CreateBotPage
#
# @pytest.mark.usefixtures("driver")
# class TestCreateBot:
#
#     @pytest.mark.order(2)
#     def test_lets_get_started(self):
#         create_bot_page = CreateBotPage(self.driver)
#         create_bot_page.lets_get_started()
#
#     @pytest.mark.order(3)
#     def test_without_bot_name(self):
#         create_bot_page = CreateBotPage(self.driver)
#         create_bot_page.without_bot_name()
#
#     def test_enter_invalid_bot_name(self):
#         create_bot_page = CreateBotPage(self.driver)
#         create_bot_page.enter_invalid_bot_name()
#
#     def test_with_bot_name(self):
#         create_bot_page = CreateBotPage(self.driver)
#         create_bot_page.with_bot_name()
#
#     def test_edit_bot_name_validation(self):
#         create_bot_page = CreateBotPage(self.driver)
#         create_bot_page.edit_bot_name()
#
#     def test_update_bot_name(self):
#         create_bot_page = CreateBotPage(self.driver)
#         create_bot_page.update_bot_name()
#
#     def test_delete_bot_cancel(self):
#         create_bot_page = CreateBotPage(self.driver)
#         create_bot_page.delete_bot()
#
#     def test_delete_bot_confirm(self):
#         create_bot_page = CreateBotPage(self.driver)
#         create_bot_page.click_confirm_delete_btn()
import allure
import pytest


from pages.create_bot_page import CreateBotPage

@allure.suite("Bot Onboarding")
@allure.sub_suite("Create Bot Flow")
@pytest.mark.usefixtures("driver")
class TestCreateBot:

    @allure.feature("Bot Creation")
    @allure.story("Start Bot Creation")
    @allure.description("Validates the 'Let's Get Started' button functionality.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["login_success"],scope="session")
    @pytest.mark.dependency(name="create_bot_done", scope="session")
    @pytest.mark.order(2)
    def test_lets_get_started_button(self, driver):
        create_bot_page = CreateBotPage(driver)
        create_bot_page.lets_get_started()

    # -------------------------------
    # Test Case 2: Cancel Button
    # -------------------------------
    @allure.feature("Bot Creation")
    @allure.story("Cancel Bot Creation")
    @allure.description("Checks if the 'Cancel' button works during bot creation.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends=["login_success"],scope="session")
    @pytest.mark.order(3)
    def test_cancel_button(self, driver):
        create_bot_page = CreateBotPage(driver)
        create_bot_page.click_cancel_btn()

    # -------------------------------
    # Test Case 3: Create Bot with Valid Name
    # -------------------------------
    @allure.feature("Bot Creation")
    @allure.story("Create Bot")
    @allure.description("Enters valid bot details and completes creation.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["login_success"],scope="session")
    @pytest.mark.order(4)
    def test_create_bot_with_valid_name(self, driver):
        create_bot_page = CreateBotPage(driver)
        create_bot_page.with_valid_bot_name()
        # create_bot_page.create_btn_disabled()
        # create_bot_page.without_bot_name()
        # create_bot_page.enter_invalid_bot_name()

        # create_bot_page.with_valid_bot_name()
        # create_bot_page.edit_bot_name()
        # create_bot_page.update_bot_name()


        # create_bot_page.delete_bot()
        # create_bot_page.click_confirm_delete_btn()




    @allure.feature("Bot Creation")
    @allure.story("Validation: Bot name is empty")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends=["login_success"],scope="session")
    @pytest.mark.order(5)
    def test_without_bot_name(self, driver):
        create_bot_page = CreateBotPage(driver)
        create_bot_page.without_bot_name()


    @allure.feature("Bot Creation")
    @allure.story("Validation: Invalid bot name is rejected")
    @allure.description("Verifies error messages for invalid bot name formats.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends=["login_success"],scope="session")
    @pytest.mark.order(6)
    def test_enter_invalid_bot_name(self, driver):
        create_bot_page = CreateBotPage(driver)
        create_bot_page.enter_invalid_bot_name()

    @allure.feature("Bot Creation")
    @allure.story("Bot Creation succeeds with valid name")
    @allure.description("Creates bot successfully using valid bot name.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["login_success"],scope="session")
    @pytest.mark.order(7)
    def test_with_bot_name(self, driver):
        create_bot_page = CreateBotPage(driver)
        create_bot_page.with_valid_bot_name()

    @allure.feature("Bot Creation")
    @allure.story("User can edit bot name")
    @allure.description("Validates editing an existing bot name.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends=["login_success"],scope="session")
    @pytest.mark.order(8)
    def test_edit_bot_name_validation(self, driver):
        create_bot_page = CreateBotPage(driver)
        create_bot_page.edit_bot_name()

    @allure.feature("Bot Creation")
    @allure.story("User can update bot name successfully")
    @allure.description("Checks updating bot name and saving correctly.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["login_success"],scope="session")
    @pytest.mark.order(9)
    def test_update_bot_name(self, driver):
        create_bot_page = CreateBotPage(driver)
        create_bot_page.update_bot_name()

    @allure.feature("Bot Management")
    @allure.story("Delete Bot cancelled by user")
    @allure.description("Checks the delete confirmation dialog cancel button.")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dependency(depends=["login_success"],scope="session")
    @pytest.mark.order(10)
    def test_delete_bot_cancel(self, driver):
        create_bot_page = CreateBotPage(driver)
        create_bot_page.delete_bot()

    @allure.feature("Bot Management")
    @allure.story("Delete Bot confirmed")
    @allure.description("Validates bot deletion flow.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["login_success"], scope="session")
    @pytest.mark.order(11)
    def test_delete_bot_confirm(self, driver):
        create_bot_page = CreateBotPage(driver)
        create_bot_page.click_confirm_delete_btn()
