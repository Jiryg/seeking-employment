from time import sleep

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from gongzuo.boss.driver.AndroidClient import AndroidClient
from gongzuo.boss.utils.utils import Utils
from gongzuo.boss.utils.utils import logging


class DetailsPageOfJob(object):
    driver: WebDriver
    _tv_job_salary = (By.ID, "tv_job_salary")
    _tv_job_name = (By.ID, "tv_job_name")
    _chat_rightly = (By.ID, "btn_chat")
    _btn_continue_chat = (By.ID, "btn_continue_chat")
    _tv_description = (By.ID, "tv_description")

    # def setup_method(self):
    #     self.driver = AndroidClient.driver
    #     return self.driver
    #
    # def teardown_method(self):
    #     self.driver.back()
    # driver = AndroidClient.driver

    def contactRightly(self):
        flag = False
        flag_black = True
        self.driver = AndroidClient.driver
        uti = Utils()

        job_name = self.driver.find_element_by_id("tv_job_name").text
        logging.debug("判断工作名称是否符合要求")
        black_list = ["驻场", "渗透", "专家", "电源", "赴", "外派", "测试主管"]
        for black in black_list:
            if black in job_name:
                flag_black = False
                break
        # if "驻场" in job_name : 渗透 专家电源  or "赴" in job_name or "外派" in job_name or "测试主管" in job_name

        if flag_black == True and uti.hasNotContacted() and uti.salaryIsTooHigh() == False:
        # self.driver.find_element_by_id("btn_chat").click()
            self.driver.find_element_by_id("btn_chat").click()
            flag = True
        if flag == True:
            sleep(1)
            self.driver.back()
        sleep(1)
        self.driver.back()
        sleep(1)
        uti.swipeUpOneCard()

