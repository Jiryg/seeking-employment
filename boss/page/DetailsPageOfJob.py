from time import sleep
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from gongzuo.boss.driver.AndroidClient import AndroidClient
from gongzuo.boss.page.BasePage import BasePage
from gongzuo.boss.page.ChatPage import ChatPage
from gongzuo.boss.utils.utils import Utils, getContentFromYamlFile
from gongzuo.boss.utils.utils import logging


class DetailsPageOfJob(BasePage):
    driver: WebDriver
    _tv_job_salary = (By.ID, "tv_job_salary")
    _tv_job_name = (By.ID, "tv_job_name")
    _chat_rightly = (By.ID, "btn_chat")
    _btn_continue_chat = (By.ID, "btn_continue_chat")
    _tv_description = (By.ID, "tv_description")
    # 详情页公司名及招聘者身份
    _tv_boss_title = "tv_boss_title"
    stateOfsendCV = "ll_exchange_resume"
    _black_list_path = "D:\\PycharmProjects\\firstDemo\\gongzuo\\boss\\data\\black_list_of_jobs"
    _black_list = ''

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
        chatpage = ChatPage()

        if uti.salaryIsTooHighOrTooLow() == False:
            self.driver.find_element_by_id("btn_chat").click()
            flag = True
        if flag == True:
            sleep(1)
            # todo 提前发简历
            prper = self.driver.find_element_by_id(self.stateOfsendCV).is_enabled()
            if prper:
                chatpage.autoSendCV()
            self.driver.back()
        sleep(1)
        self.driver.back()
        sleep(1)
        uti.swipeUpOneCard()

    def ifChatRightly(self):
        self.driver = AndroidClient.driver
        hit_black_list = False
        logging.debug("**************page_source的内容是：***************")
        logging.debug(self.driver.page_source)
        page_source = self.driver.page_source

        self._black_list = getContentFromYamlFile(self._black_list_path)
        logging.debug(self._black_list)
        for black in self._black_list:
            if black in page_source:
                logging.debug("命中黑名单，不能投递简历")
                # todo 不感兴趣
                hit_black_list = True
                break
        if hit_black_list:
            self.driver.back()
            return False
        else:
            return True

    def hasChated(self):
        button = self.driver.find_element_by_id("btn_chat").text
        if "继续沟通" == button:
            logging.debug("已经沟通过了")
            self.driver.back()
            return False
        else:
            return True