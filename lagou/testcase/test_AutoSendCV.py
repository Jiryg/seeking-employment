import json
import logging
from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver import DesiredCapabilities
from gongzuo.lagou.page.MainPage import MainPage
from gongzuo.lagou.testcase.BaseTestCase import BaseTestCase


class Test_AutoSendCV(BaseTestCase):
    # logging.basicConfig()
    # log = logging.getLogger("hahaha")
    # log.setLevel(logging.DEBUG)

    def setup_class(self):
        self.url = "https://xueqiu.com/"
        self.job_list = ["测试工程师"]
        # self.url = "https://www.lagou.com/jobs/list_{}/p-city_2?&cl=false&fromSearch=true&labelWords=&suginput=".format(self.job_list[0])
        # options = webdriver.ChromeOptions()
        # self.driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.driver.get(url=self.url)
        self.main = MainPage(self.driver)
    def setup_method(self):
        pass

    def teardown_method(self):
        # 向下滚动500像素
        # window.scrollBy(0,500)
        # js = "return window.scrollBy(0,500)"
        # self.driver.execut_script(js)
        pass

    @pytest.mark.repeat(10)
    def test_send_CV(self):
        # self.main.gotoDetail()
        sleep(5)
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.driver.execut_script(js)


    def test_xueqiu(self):
        self.main.search('阿里巴巴').select('BABA')
        self.logger.debug("*************执行完毕**************")




    def test_basic(self):
        script = "return JSON.stringify(window.performance.timing)"
        self.driver.maximize_window()
        raw = self.driver.execute_script(script)
        sleep(2)
        self.driver.minimize_window()
        content = json.dumps(json.loads(raw), indent=2)
        print(content)


    def teardown_class(self):
        sleep(10)
        self.driver.quit()