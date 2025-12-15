#
# from pages.bot_settings import BotSettingsPage
# class TestBotSettingsPage:
#
#
#     def test_bot_settings(self,driver):
#         bot_settings_page=BotSettingsPage(driver)
#         # bot_settings_page.validation_msg_bot()
#
#         bot_settings_page.valid_bot_personalization()
#         # bot_settings_page.theme_settings()
#         bot_settings_page.general_settings()
#         bot_settings_page.toggle_all()
#         bot_settings_page.tts_settings()



import pytest
import allure
from pages.bot_settings import BotSettingsPage

@allure.suite("Bot Onboarding")
@allure.sub_suite("Bot Settings")
@pytest.mark.usefixtures("driver")
class TestBotSettingsPage:

    # 1. Validation Message Test (Optional / Commented)
    # --------------------------
    @allure.feature("Bot Settings")
    @allure.story("Validation Messages")
    @allure.description("Verify validation messages appear correctly for bot settings (if implemented).")
    @allure.severity(allure.severity_level.MINOR)
    # @pytest.mark.dependency(depends=["knowledge_base_done"], scope="session")
    # @pytest.mark.dependency(name="bot_settings_done",scope="session")
    @pytest.mark.dependency(name="validation_msg_done", depends=["knowledge_base_done"], scope="session")
    @pytest.mark.order(24)
    def test_validation_msg_bot(self, driver):
        bot_settings_page = BotSettingsPage(driver)
        with allure.step("Check validation messages for bot settings"):
            bot_settings_page.validation_msg_bot()

    # --------------------------
    # 2. Bot Personalization Test
    # --------------------------
    @allure.feature("Bot Settings")
    @allure.story("Bot Personalization")
    @allure.description("Verify that bot personalization settings can be applied correctly.")
    @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.dependency(depends=["knowledge_base_done"],scope="session")
    @pytest.mark.dependency(depends=["validation_msg_done"], scope="session")
    @pytest.mark.order(25)
    def test_valid_bot_personalization(self, driver):
        bot_settings_page = BotSettingsPage(driver)
        with allure.step("Apply valid bot personalization settings"):
            bot_settings_page.valid_bot_personalization()

    # --------------------------
    # 3. Theme Settings Test
    # --------------------------

    @allure.feature("Bot Settings")
    @allure.story("Theme Settings")
    @allure.description("Verify that theme settings are applied successfully.")
    @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.dependency(depends=["knowledge_base_done"],scope="session")
    @pytest.mark.dependency(depends=["validation_msg_done"], scope="session")
    @pytest.mark.order(26)
    def test_theme_settings(self, driver):
        bot_settings_page = BotSettingsPage(driver)
        with allure.step("Apply theme settings"):
            bot_settings_page.theme_settings()

    # --------------------------
    # 4. General Settings Test
    # --------------------------
    @allure.feature("Bot Settings")
    @allure.story("General Settings")
    @allure.description("Verify general bot settings are applied correctly.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends=["knowledge_base_done"],scope="session")
    @pytest.mark.order(27)
    def test_general_settings(self, driver):
        bot_settings_page = BotSettingsPage(driver)
        with allure.step("Apply general bot settings"):
            bot_settings_page.general_settings()

    # --------------------------
    # 5. Toggle All Settings Test
    # --------------------------
    @allure.feature("Bot Settings")
    @allure.story("Toggle All Settings")
    @allure.description("Verify the 'Toggle All' functionality works for bot settings.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends=["knowledge_base_done"],scope="session")
    @pytest.mark.order(28)
    def test_toggle_all(self, driver):
        bot_settings_page = BotSettingsPage(driver)
        with allure.step("Toggle all bot settings"):
            bot_settings_page.toggle_all()

    # --------------------------
    # 6. Text-to-Speech (TTS) Settings Test
    # --------------------------
    @allure.feature("Bot Settings")
    @allure.story("TTS Settings")
    @allure.description("Verify Text-to-Speech settings work correctly for the bot.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["knowledge_base_done"],scope="session")
    @pytest.mark.order(29)
    def test_tts_settings(self, driver):
        bot_settings_page = BotSettingsPage(driver)
        with allure.step("Configure TTS settings for the bot"):
            bot_settings_page.tts_settings()

    # --------------------------

