from gongzuo.boss.utils.utils import logging
from gongzuo.boss.driver.AndroidClient import AndroidClient


class MessagePage(object):
    # 极速处理 + 消息数
    mContent = 'mContent'


    def toChatPage(self):
        logging.debug("到聊天页面")
        self.driver = AndroidClient.driver
        self.driver.tap([(261,578)], 100)

    def swipeUpALittle(self):
        self.driver.swipe(600, 1050, 600, 860, 1500)
        logging.debug("上滑操作执行完毕")