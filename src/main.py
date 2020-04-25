from src.DataBase.DataBase import DataBase
from src.Exceler.ExcelTry import ExcelTry
from src.MobileAuto.UIAutomator2Try import UIAutomator2Try
from src.WebCrawler.SeleniumTry import SeleniumTry


class Main:

    def __init__(self):
        # 三行分别是小班课, 定制学_有奖, 定制学_无奖
        self.messages = [
            "今天周d,明天晚上还有新的小班课,不过小班课d还没学完，今儿都扫尾完成吧~",
            "今天周d，本周奖学金打卡已经完成d次，需要5次才可以鸭，Keep going！",
            "[定制学]本周定制学已完成d天，一周完成3天打卡，就可以拿到Alicia整理的本part精华词汇哦，再坚持一下吧~"
        ]

        self.selenium_try = SeleniumTry()
        self.excel_try = ExcelTry()
        self.data_base = DataBase()
        self.ui = UIAutomator2Try()

    def integrate(self):
        # 从网页读取数据
        self.selenium_try.clicks()

        # 过滤出需要提醒的学生
        self.excel_try.filters()

        # 初始化手机设置
        self.ui.initialize()

        # 小班课提醒
        self.send_to_one_type(self.excel_try.common_notice_list, 1)

        # 定制学有奖学金提醒
        self.send_to_one_type(self.excel_try.custom_with_scholarship_list, 2)

        # 定制学没有奖学金的提醒
        self.send_to_one_type(self.excel_try.custom_no_scholarship_list, 3)

        # 关闭数据库
        self.data_base.close()

    def send_to_one_type(self, student_list, notice_type):
        for student in student_list:
            index = self.show_process(student, student_list)
            if index >= 0:
                while not self.ui.send_message(student, notice_type, self.messages[notice_type-1]):
                    self.ui.initialize()

    def show_process(self, student, student_list):
        index = 1 + student_list.index(student)
        print('****** 当前进度:' + str(index) + ' / ' + str(len(student_list)))
        return index


if __name__ == "__main__":
    main = Main()
    main.integrate()
