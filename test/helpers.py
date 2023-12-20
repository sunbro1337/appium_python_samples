from appium import webdriver
from appium.options.android import UiAutomator2Options


appium_server_url = 'http://localhost:4723'


android_capabilities = {
    'platformName': 'android',
    'automationName': 'uiautomator2',
    'deviceName': "",
    'appPackage': "",
    'appActivity': "",
    'language': 'en',
    'locale': 'US',
}


def setup_appium_webdriver(capabilities):
    driver = webdriver.Remote(
        appium_server_url,
        options=UiAutomator2Options().load_capabilities(capabilities)
    )
    return driver
