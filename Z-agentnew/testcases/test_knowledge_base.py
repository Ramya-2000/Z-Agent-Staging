# import pytest
#
# from pages.knowledge_base import KnowledgeBasePage
#
#
# @pytest.mark.usefixtures("driver")
# class TestKnowledgeBase:
#
#     # @pytest.mark.dependency(depends=["create_bot_done"])
#     @pytest.mark.order(4)
#     def test_knowledge_base(self,driver):
#         knowledge_base_page=KnowledgeBasePage(driver)
        # knowledge_base_page.file_upload()

        # knowledge_base_page.upload_two_random_files_loop()
        # knowledge_base_page.random_file_duplication()
        # knowledge_base_page.file_view()
        # knowledge_base_page.connected_apps_upload()

        # knowledge_base_page.web_scrapping_logic()
        # knowledge_base_page.web_scrapping_view_edit()
        # knowledge_base_page.web_scrapping_revert_changes()

import pytest
import allure
from pages.knowledge_base import KnowledgeBasePage

@allure.suite("Bot Onboarding")
@allure.sub_suite("Knowledge Base")
@pytest.mark.usefixtures("driver")
class TestKnowledgeBase:

    # --------------------------
    # 1. File Upload Test
    # --------------------------
    @allure.feature("Knowledge Base")
    @allure.story("File Upload")
    @allure.description("Upload a single file to the knowledge base and verify it appears correctly.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["model_config_done"],scope="session")
    # @pytest.mark.dependency(name="knowledge_base_done",scope="session")
    # @pytest.mark.order(16)
    # def test_file_upload(self, driver):
    #     knowledge_base_page = KnowledgeBasePage(driver)
    #     with allure.step("Upload a file"):
    #         knowledge_base_page.file_upload()

    # --------------------------
    # 2. Upload Two Random Files
    # --------------------------
    # @allure.feature("Knowledge Base")
    # @allure.story("Upload Two Random Files")
    # @allure.description("Upload two random files in a loop to verify batch upload functionality.")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.dependency(depends=["model_config_done"],scope="session")
    # @pytest.mark.order(17)
    # def test_upload_two_random_files_loop(self, driver):
    #     knowledge_base_page = KnowledgeBasePage(driver)
    #     with allure.step("Upload two random files"):
    #         knowledge_base_page.upload_two_random_files_loop()

    # --------------------------
    # 3. Random File Duplication
    # --------------------------
    # @allure.feature("Knowledge Base")
    # @allure.story("Random File Duplication")
    # @allure.description("Verify that duplicate files are handled correctly in the knowledge base.")
    # @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.dependency(depends=["model_config_done"],scope="session")
    # @pytest.mark.order(18)
    # def test_random_file_duplication(self, driver):
    #     knowledge_base_page = KnowledgeBasePage(driver)
    #     with allure.step("Test duplicate file handling"):
    #         knowledge_base_page.random_file_duplication()

    # --------------------------
    # 4. File View Test
    # --------------------------
    # @allure.feature("Knowledge Base")
    # @allure.story("File View")
    # @allure.description("Verify that uploaded files can be viewed correctly in the knowledge base.")
    # @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.dependency(depends=["model_config_done"],scope="session")
    # @pytest.mark.order(19)
    # def test_file_view(self, driver):
    #     knowledge_base_page = KnowledgeBasePage(driver)
    #     with allure.step("View uploaded files"):
    #         knowledge_base_page.file_view()

    # --------------------------
    # 5. Connected Apps Upload
    # --------------------------
    # @allure.feature("Knowledge Base")
    # @allure.story("Connected Apps Upload")
    # @allure.description("Upload files via connected apps integration and verify.")
    # @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.dependency(depends=["model_config_done"],scope="session")
    # @pytest.mark.order(20)
    # def test_connected_apps_upload(self, driver):
    #     knowledge_base_page = KnowledgeBasePage(driver)
    #     with allure.step("Upload files from connected apps"):
    #         knowledge_base_page.connected_apps_upload()

    # --------------------------
    # 6. Web Scraping Logic
    # --------------------------
    @allure.feature("Knowledge Base")
    @allure.story("Web Scraping Logic")
    @allure.description("Test web scraping logic to fetch and store content correctly.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["model_config_done"],scope="session")
    @pytest.mark.dependency(name="knowledge_base_done",scope="session")
    @pytest.mark.order(21)
    def test_web_scrapping_logic(self, driver):
        knowledge_base_page = KnowledgeBasePage(driver)
        with allure.step("Perform web scraping and validate logic"):
            knowledge_base_page.web_scrapping_logic()

    # --------------------------
    # 7. Web Scraping View/Edit
    # --------------------------
    @allure.feature("Knowledge Base")
    @allure.story("Web Scraping View and Edit")
    @allure.description("Verify that web-scraped content can be viewed and edited correctly.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["model_config_done"],scope="session")
    @pytest.mark.order(22)
    def test_web_scrapping_view_edit(self, driver):
        knowledge_base_page = KnowledgeBasePage(driver)
        with allure.step("View and edit web scraped content"):
            knowledge_base_page.web_scrapping_view_edit()

    # --------------------------
    # 8. Web Scraping Revert Changes
    # --------------------------
    @allure.feature("Knowledge Base")
    @allure.story("Web Scraping Revert Changes")
    @allure.description("Verify that changes to web-scraped content can be reverted correctly.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends=["model_config_done"],scope="session")
    @pytest.mark.order(23)
    def test_web_scrapping_revert_changes(self, driver):
        knowledge_base_page = KnowledgeBasePage(driver)
        with allure.step("Revert changes to web scraped content"):
            knowledge_base_page.web_scrapping_revert_changes()
