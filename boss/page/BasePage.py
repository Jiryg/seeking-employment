import logging
import math
import os

import yaml
from PIL import Image
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By

from gongzuo.boss.driver.AndroidClient import AndroidClient


class BasePage(object):
    logging.basicConfig()
    _logger = logging.getLogger("gongzuo")
    _logger.setLevel(level=logging.DEBUG)

    # PATH = lambda p: os.path.abspath(p)
    PATH = "D:\\PycharmProjects\\firstDemo\\gongzuo\\boss\\output"
    TEMP_FILE = PATH + "\\temp_screen.png"

    def __init__(self):
        self.driver = AndroidClient.driver

    @property
    def logger(self):
        return self._logger

    def getScreenShot(self, element):
        self.TEMP_FILE = 'login.png'
        self.driver.save_screenshot(self.TEMP_FILE)
        location = element.location
        size = element.size
        box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])

        # 截取图片
        image = Image.open(self.TEMP_FILE)
        newImage = image.crop(box)
        newImage.save(self.TEMP_FILE)

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

    def get_screenshot_by_element(self, element):
        # 先截取整个屏幕，存储至系统临时目录下
        self.driver.save_screenshot('foo.png')
        # self.driver.get_screenshot_as_file(self.TEMP_FILE)

        # 获取元素bounds
        location = element.location
        size = element.size
        box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])

        # 截取图片
        image = Image.open(self.TEMP_FILE)
        newImage = image.crop(box)
        newImage.save(self.TEMP_FILE)

        return self

    # def compare(pic1, pic2):
    #     '''
    #     :param pic1: 图片1路径
    #     :param pic2: 图片2路径
    #     :return: 返回对比的结果
    #     '''
    #     image1 = Image.open(pic1)
    #     image2 = Image.open(pic2)
    #
    #     histogram1 = image1.histogram()
    #     histogram2 = image2.histogram()
    #
    #     differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
    #
    #     print
    #     differ
    #     return differ
    #
    # compare(r'D:\Ptest\Testcase\11.jpg', r'D:\Ptest\Testcase\22.jpg')

    # def find(self, kv) -> WebElement:
    #     #todo: 处理各类弹框
    #     return self.find(*kv)

    def find(self, by, value):
        element: WebElement
        # todo 加一些重复查找的逻辑
        element = self.driver.find_element(by, value)
        return element

    def loadSteps(self, file_path, function_name, **kwargs):
        file = open(file_path, 'r', encoding="UTF-8")
        content = yaml.load(file)
        method = content[function_name]

        for step in method:
            step: dict

            element_platform = {"by": step['by'], "locator": step['locator']}
            element: WebElement = self.find(by=element_platform['by'], value=element_platform['locator'])
            action = str(step['action']).lower()

            # 根据 action 来做不同的操作
            if action == "click":
                element.click()
            elif action == "sendkeys":
                text = str(step['text'])
                element.send_keys(text)
            else:
                print("UNKNOW COMMAND {}".format(step))

if __name__=="__main__":
    basepage = BasePage()