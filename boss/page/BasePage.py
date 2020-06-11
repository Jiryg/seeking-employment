import logging

from gongzuo.boss.driver.AndroidClient import AndroidClient


class BasePage(object):
    logging.basicConfig()
    _logger = logging.getLogger("gongzuo")
    _logger.setLevel(level=logging.DEBUG)

    def __init__(self):
        self.driver = AndroidClient.driver

    @property
    def logger(self):
        return self._logger

    def getScreenShot(self):
        self.driver.save_screenshot('login.png')

    def findElementAndClick(self, yuansu):
        i = 1
        while i < 3:
            ele = self.driver.find_element_by_xpath(yuansu)
            if ele:
                ele.click()
                break
            else:
                self.driver.swipe(500, 1470, 500, 1692, 1500)
                i = i + 1

if __name__=="__main__":
    basepage = BasePage()