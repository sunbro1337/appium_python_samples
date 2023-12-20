import time

import pytest
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import helpers


current_capabilities = helpers.android_capabilities
current_capabilities['deviceName'] = "emulator-5554"
current_capabilities['appPackage'] = "com.android.settings"
current_capabilities['appActivity'] = ".Settings"
current_capabilities['noReset'] = True


@pytest.fixture()
@allure.title("Setup appium webdriver")
def setup_appium_webdriver():
    driver = helpers.setup_appium_webdriver(
        capabilities=current_capabilities
    )
    return driver


class TestBattery:
    @allure.title("test_find_battery_element")
    @allure.description("test_find_battery_element")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_enter_battery_element(self, setup_appium_webdriver):
        element = setup_appium_webdriver.find_element(
            by=AppiumBy.XPATH,
            value='//*[@text="Battery"]'
        )
        element.click()

    @allure.title("test_navigate_up")
    @allure.description("test_navigate_up")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_up(self, setup_appium_webdriver):
        label_visible = False
        while not label_visible: #TODO turn into helper or decorator and add a timeout checks and reports
            label = setup_appium_webdriver.find_element(
                by=AppiumBy.XPATH,
                value='//*[@content-desc="Battery"]'
            )
            if label:
                label_visible = True
        element = setup_appium_webdriver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID,
            value="Navigate up"
        )
        element.click()


