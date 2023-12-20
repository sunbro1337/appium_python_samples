import pytest
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

appium_server_url = 'http://localhost:4723'


@pytest.fixture()
@allure.title("Setup appium capabilities")
def setup_appium_capabilities():
    capabilities = {
        'platformName': 'android',
        'automationName': 'uiautomator2',
        'deviceName': "emulator-5554",
        'appPackage': "com.android.settings",
        'appActivity': ".Settings",
        'language': 'en',
        'locale': 'US',
    }
    return capabilities


@pytest.fixture()
@allure.title("Setup appium webdriver")
def setup_appium_webdriver(setup_appium_capabilities):
    driver = webdriver.Remote(
        appium_server_url,
        options=UiAutomator2Options().load_capabilities(setup_appium_capabilities)
    )
    return driver


@allure.title("test_find_battery_element")
@allure.description("test_find_battery_element")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_battery_element(setup_appium_webdriver):
    element = setup_appium_webdriver.find_element(
        by=AppiumBy.XPATH,
        value='//*[@text="Battery"]'
    )
    assert element.click() is None

