from time import sleep
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from gongzuo.boss.driver.AndroidClient import AndroidClient
from gongzuo.boss.page.DetailsPageOfJob import DetailsPageOfJob
from gongzuo.boss.utils.utils import logging

class MainPage(object):
    driver = ''
    def __init__(self):
        print("这个执行吗")
        # andriodClient = AndroidClient()
        self.driver = AndroidClient.restart_app()

    def gotoCategoryOfSelected(self, category='移动端测试'):
        if category == '移动端测试':
            # self.driver.find_element(self, by=By.XPATH, value="//*[@resource-id='com.hpbr.bosszhipin:id/title_container'] //*[@text='移动端测试']").click()
            self.driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/title_container'] //*[@text='移动端测试']").click()
        elif category == "测试开发":
            self.driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/title_container'] //*[@text='测试开发' and @instance='1']").click()
        else:
            self.driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/title_container'] "
                                              "//*[@text='自动化测试' and @instance='2']").click()
        logging.info("到所选择的工作类别：{}".format(category))
        # return MainPage()
        # return ProfilePage()

    def gotoDetailsPageOfjob(self):
        # todo
        sleep(5)
        self.driver.tap([(300, 500)], 500)
        # return DetailsPageOfJob()

    def gotoMessagePage(self):
        self.driver.find_element_by_id("com.hpbr.bosszhipin:id/iv_tab_3").click()

if __name__ == '__main__':
    mainpage = MainPage()
    mainpage.gotoCategoryOfSelected()
    mainpage.gotoDetailsPageOfjob()