from gongzuo.boss.driver.AndroidClient import AndroidClient
from gongzuo.boss.utils.utils import logging


class ChatPage(object):
    have_sent = "// *[contains( @ text, '已发送给')]"
    DE = "//*[@resource-id='com.hpbr.bosszhipin:id/tv_name' and @instance='2']"
    AutoTester = "//*[@resource-id='com.hpbr.bosszhipin:id/tv_name' and @instance='6']"
    TE = "//*[@resource-id='com.hpbr.bosszhipin:id/tv_name' and @instance='4']"


    def send_cv(self):
        self.driver = AndroidClient.driver
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
            black_list = ["外派", "驻场", "渗透", "专家", "电源", "赴", "测试主管"]
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