from time import sleep
import yaml
from appium.webdriver.webdriver import WebDriver

from gongzuo.boss.driver.AndroidClient import AndroidClient
import logging

from gongzuo.boss.page.BasePage import BasePage


class Utils(BasePage):
    # driver: WebDriver
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s",
                        datefmt='%Y-%m-%d  %H:%M:%S %a'
                        )
    # driver = AndroidClient.driver
    # def __init__(self):
    #     self.driver = AndroidClient.restart_app()

    def swipe_downToUp(self):
        self.size = self.driver.get_window_size()
        print(self.size)
        self.x_start = self.size["width"] // 2
        self.y_start = self.size["height"] // 5 * 4
        self.x_end = self.size["width"] // 2
        self.y_end = self.size["height"] // 5 * 2
        sleep(5)
        logging.debug("开始执行上滑操作")
        self.driver.swipe(self.x_start, self.y_start, self.x_end, self.y_end, 1500)
        logging.debug("上滑操作执行完毕")

    def swipeUpOneCard(self):
        self.driver = AndroidClient.driver
        self.size = self.driver.get_window_size()
        print(self.size)
        self.x_start = self.size["width"] // 2
        self.y_start = 1325
        self.x_end = self.size["width"] // 2
        self.y_end = 888
        logging.debug("开始执行上滑操作")
        self.driver.swipe(self.x_start, self.y_start, self.x_end, self.y_end, 1500)
        logging.debug("上滑操作执行完毕")


    # 这个方法有问题
    def find(self, con):
        self.element = AndroidClient.driver.find_element(con[0], con[1])
        return self.element

    def hasNotContacted(self):
        self.driver = AndroidClient.driver
        logging.debug(self.driver.find_element_by_id("btn_chat").text)

        content = self.driver.find_element_by_id("btn_chat").text
        if "立即沟通" in content:
        # if "立即沟通" == AndroidClient.driver.find_element_by_id("btn_chat").text:
            return True
        else:
            return False

    def salaryIsTooHigh(self):
        self.driver = AndroidClient.driver
        logging.debug(self.driver.find_element_by_id("tv_job_salary").text)

        content = self.driver.find_element_by_id("tv_job_salary").text
        salary = int(content.split('-')[1][:2])
        if salary > 30:
            # if "立即沟通" == AndroidClient.driver.find_element_by_id("btn_chat").text:
            return True
        else:
            return False


def getContentFromYamlFile(filepath) -> list:
    file = open(filepath, 'r', encoding='utf-8')
    content = yaml.safe_load(file)
    return content


if __name__ == '__main__':
    from gongzuo.boss.page.App import App
    utils = Utils()
    # utils.swipe_downToUp()
    # utils.swipeUpOneCard()
    driver = AndroidClient.driver
    App.main()
    # driver.get_window_size()
    size = driver.get_window_rect()
    print(size)

if __name__ == '__main__':
    black_list_path = "gongzuo\\boss\\data\\black_list_of_jobs"
    getContentFromYamlFile(black_list_path)