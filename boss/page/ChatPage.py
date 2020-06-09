from time import sleep

from gongzuo.boss.driver.AndroidClient import AndroidClient
from gongzuo.boss.page.BasePage import BasePage
from gongzuo.boss.utils.utils import logging, getContentFromYamlFile


class ChatPage(BasePage):
    have_sent = "// *[contains( @ text, '已发送给')]"
    DE = "//*[@resource-id='com.hpbr.bosszhipin:id/tv_name' and @instance='2']"
    AutoTester = "//*[@resource-id='com.hpbr.bosszhipin:id/tv_name' and @instance='6']"
    TE = "//*[@resource-id='com.hpbr.bosszhipin:id/tv_name' and @instance='4']"
    page_source = ''


    def send_cv(self):
        # self.driver = AndroidClient.driver
        job_name = ''
        try:
            job_name = self.driver.find_element_by_id("tv_position_name").text
        except:
            logging.debug("没有找到 job_name")
        finally:
            try:
                self.driver.find_element_by_id("tv_exchange_resume").click()
                # 确认发送简历
                self.driver.find_element_by_id("tv_positive").click()

                if '自动化测试工程师' in job_name:
                    self.driver.find_element_by_xpath(self.AutoTester).click()
                elif '测试开发工程师' in job_name:
                    self.driver.find_element_by_xpath(self.DE).click()
                else:
                    self.driver.tap([(210, 1500)], 100)
            except:
                logging.debug("发简历不可用")

            finally:
                self.driver.back()


    def say_hello(self):
        cont1 = "请查收我的简历"
        self.driver.find_element_by_id("et_content").send_keys(cont1)
        self.driver.find_element_by_id("tv_send").click()

    def ifSend_cv(self):
        self.driver = AndroidClient.driver
        hit_black_list = False
        logging.debug("**************page_source的内容是：***************")
        logging.debug(self.driver.page_source)
        page_source = self.driver.page_source
        if self.have_sent in page_source:
            return False
        else:
            black_list = getContentFromYamlFile(self.black_list_path)
            for black in black_list:
                if black in page_source:
                    logging.debug("命中黑名单，不能投递简历")
                    cont2 = "请稍等，我稍后和你联系~"
                    self.driver.find_element_by_id("et_content").send_keys(cont2)
                    self.driver.find_element_by_id("tv_send").click()
                    hit_black_list = True
                    break
        if hit_black_list:
            self.driver.back()
            return False
        else:
            return True

    def autoSendCV(self, category='移动端测试'):
        zidonghua = "//*[@resource-id='com.hpbr.bosszhipin:id/mResumeName' and @instance='5']"
        ceshigongchengshi = "//*[@resource-id='com.hpbr.bosszhipin:id/mResumeName' and @instance='3']"
        ceshikaifa = "//*[@resource-id='com.hpbr.bosszhipin:id/mResumeName' and @instance='3']"
        self.driver = AndroidClient.driver
        self.driver.find_element_by_id("tv_exchange_resume").click()

        if category == '自动化测试':
            self.driver.swipe(500, 1314, 500, 1566, 1500)
            self.driver.find_element_by_xpath(zidonghua).click()
        elif category == '测试开发':
            self.driver.find_element_by_xpath(ceshikaifa).click()
        else:
            self.driver.find_element_by_xpath(ceshigongchengshi).click()
        self.driver.find_element_by_id("mSure").click()


if __name__ == '__main__':
    from gongzuo.boss.page.MessagePage import MessagePage
    from gongzuo.boss.page.MainPage import MainPage
    mainPage = MainPage()
    messPage = MessagePage()
    mainPage.gotoMessagePage()
    messPage.toChatPage()
    chatpage = ChatPage()
    chatpage.page_source = ["外派", "驻场", "渗透", "专家", "电源", "赴", "测试主管"]
    print(chatpage.ifSend_cv())