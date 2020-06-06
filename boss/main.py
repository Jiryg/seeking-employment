from gongzuo.boss.test_findJob import Test_findJob


class Main(object):
    def main(self, n):
        find_job = Test_findJob()
        for x in range(n):
            find_job.test_Contact_MoblieTest()

if __name__ == '__main__':
    start = Main()
    start.main(3)