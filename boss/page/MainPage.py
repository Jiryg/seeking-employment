from time import sleep
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from gongzuo.boss.driver.AndroidClient import AndroidClient
from gongzuo.boss.page.BasePage import BasePage
from gongzuo.boss.page.DetailsPageOfJob import DetailsPageOfJob
from gongzuo.boss.page.MessagePage import MessagePage
from gongzuo.boss.utils.utils import logging
from gongzuo.boss.page import App


class MainPage(BasePage):
    mainpage_YAML_path = "D:\\PycharmProjects\\firstDemo\\gongzuo\\boss\\data\\MainPage"
    # def __init__(self):
    #     print("这个执行吗")
    #     # andriodClient = AndroidClient()
    #     self.driver = AndroidClient.restart_app()

    def gotoCategoryOfSelected(self, category='移动端测试'):
        self.driver = AndroidClient.driver
        if category == '移动端测试':
            self.driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/title_container'] //*[@text='移动端测试']").click()
        elif category == "测试开发":
            self.driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/title_container'] //*[@text='测试开发' and @instance='1']").click()
        else:
            self.driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/title_container'] "
                                              "//*[@text='自动化测试' and @instance='2']").click()
        self.logger.info("到所选择的工作类别：{}".format(category))
        # return MainPage()
        # return ProfilePage()

    def gotoDetailsPageOfjob(self):
        self.loadSteps(self.mainpage_YAML_path, "gotoDetailsPageOfjob")
        # sleep(5)
        # png = self.driver.get_screenshot_as_png()
        # with open('\\2.png', 'wb') as f:
        #     f.write(png)


        # return DetailsPageOfJob()

    def gotoMessagePage(self):
        self.driver.find_element_by_id("com.hpbr.bosszhipin:id/iv_tab_3").click()
        # return MessagePage()

if __name__ == '__main__':
    App.App.main()
    main = MainPage()
    main.gotoCategoryOfSelected()
    # main.gotoMessagePage()
    main.gotoDetailsPageOfjob()
