from time import sleep
import pytest
from gongzuo.boss.page.App import App
from gongzuo.boss.page.ChatPage import ChatPage
from gongzuo.boss.page.MainPage import logging
from appium.webdriver.webdriver import WebDriver
from gongzuo.boss.driver.AndroidClient import AndroidClient
from gongzuo.boss.page.MainPage import MainPage
from gongzuo.boss.page.DetailsPageOfJob import DetailsPageOfJob
from gongzuo.boss.page.MessagePage import MessagePage
from gongzuo.boss.utils.utils import Utils


class Test_findJob(object):
    driver=WebDriver
    def setup_class(self):
        App.main()

    def teardown_class(self):
        logging.debug("**************类执行结束***************")

    @pytest.mark.parametrize("nums", [50])
    def test_Contact_MoblieTest(self, nums):
        detailpage = DetailsPageOfJob()
        mainpage = MainPage()
        chatpage = ChatPage()

        # uti = Utils()
        mainpage.gotoCategoryOfSelected()
        for x in range(nums):
            logging.debug("***********************跟第 %s 个打招呼***********************", x)
            mainpage.gotoDetailsPageOfjob()
            sleep(1)
            if detailpage.ifChatRightly():
                detailpage.contactRightly()
            # uti.swipeUpOneCard()
        # detailpage = DetailsPageOfJob()
        # detailpage.contactRightly()
        logging.debug("执行完毕")
        # ContactRightly()

    @pytest.mark.parametrize("nums", [3])
    def test_chat_and_send_cv(self, nums):
        self.driver = AndroidClient.driver
        mainpage = MainPage()
        messagepage = MessagePage()
        chatpage = ChatPage()
        # uti = Utils()
        mainpage.gotoMessagePage()
        for x in range(nums):
            logging.debug("***********************跟第 %s 个沟通***********************", x)
            sleep(1)
            messagepage.toChatPage()
            if chatpage.ifSend_cv() == True:
                # chatpage.say_hello()
                chatpage.send_cv()
            sleep(1)
            messagepage.swipeUpALittle()
            # uti.swipeUpOneCard()
        # detailpage = DetailsPageOfJob()
        # detailpage.contactRightly()
        logging.debug("执行完毕")


if __name__ == '__main__':
    n = 10
    find_job = Test_findJob()
    find_job.test_Contact_MoblieTest(n)
