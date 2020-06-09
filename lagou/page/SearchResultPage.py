from gongzuo.lagou.page.BasePage import BasePage


class SearchResultPage(BasePage):
    def select(self, keyword):
        self.driver.find_element_by_xpath('//*[contains(text(), "{}")]/../../../..//*[@class="follow__control"]'.format(keyword)).click()
        return self