
import pytest
import allure

from pages.integrations import IntegrationsPage

@allure.suite("Bot Onboarding")
@allure.sub_suite("Integrations")
@pytest.mark.usefixtures("driver")
class TestIntegrationsPage:

    # --------------------------
    # 1. Direct Link Test
    # --------------------------
    @allure.feature("Integrations")
    @allure.story("Direct Link")
    @allure.description("Verify that the direct link functionality works correctly in integrations module.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.order(30)
    def test_direct_link(self, driver):
        integration_page=IntegrationsPage(driver)
        with allure.step("Execute direct link function and verify behavior"):
         integration_page.integration_module()
