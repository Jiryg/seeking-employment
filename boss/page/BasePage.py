from gongzuo.boss.driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver = AndroidClient.driver


if __name__=="__main__":
    basepage = BasePage()