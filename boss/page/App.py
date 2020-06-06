from gongzuo.boss.driver.AndroidClient import AndroidClient
from gongzuo.boss.page import MainPage


class App(object):
    @classmethod
    def main(cls):
        AndroidClient.restart_app()
        # return MainPage.MainPage()

if __name__ == '__main__':
    App.main()
    print("App()的 main() 执行完毕")