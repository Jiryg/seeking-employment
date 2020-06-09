from time import sleep
from gongzuo.lagou.page.BasePage import BasePage
from gongzuo.lagou.page.DetailPage import DetailPage
from gongzuo.lagou.page.SearchResultPage import SearchResultPage


class MainPage(BasePage):
    def search(self, keyword):
        self.driver.find_element_by_css_selector('[placeholder=搜索]').send_keys(keyword)
        sleep(2)
        self.driver.find_element_by_css_selector('.iconfont_iconfont_9UW.search').click()
        return SearchResultPage(self.driver)

    def gotoDetail(self):
        self.driver.find_element_by_css_selector('.con_list_item first_row default_list[data-index="3"]').click()
        return DetailPage(self.driver)