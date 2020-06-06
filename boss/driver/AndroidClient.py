from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):
    driver= WebDriver

    @classmethod
    def install_app(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "honor-9"
        caps["appPackage"] = "com.hpbr.bosszhipin"
        caps["appActivity"] = ".module.main.activity.MainActivity"
        caps["automationName"] = "UiAutomator1"
        caps["autoGrantPermissios"] = True
        # caps["noReset"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "honor-9"
        caps["appPackage"] = "com.hpbr.bosszhipin"
        caps["appActivity"] = ".module.main.activity.MainActivity"
        caps["automationName"] = "UiAutomator1"
        caps["autoGrantPermissios"] = True
        caps["noReset"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        cls.driver.implicitly_wait(10)
        return cls.driver
if __name__ == '__main__':
    AndroidClient.restart_app()
