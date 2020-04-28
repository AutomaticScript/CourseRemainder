from src.DataBase.DataBase import DataBase
from src.Exceler.ExcelTry import ExcelTry
from src.MobileAuto.UIAutomator2Try import UIAutomator2Try
from src.WebCrawler.SeleniumTry import SeleniumTry


class Main:

    def __init__(self):
        # 三行分别是小班课, 定制学_有奖, 定制学_无奖
        self.messages = [
            "[温馨提醒]周五就是五一了，小班课尽量提前完成啊，d还没有听～(听完忽略)",
            "本周奖学金打卡已经完成d次，周末就放假了，提前学完5天才可以嗨～",
            "本周定制学已完成d天，一周完成3天打卡就可以拿到助教奖励～"
        ]

        self.selenium_try = SeleniumTry()
        self.excel_try = ExcelTry()
        # self.data_base = DataBase()
        self.ui = UIAutomator2Try()

    def integrate(self):
        # 从网页读取数据
        # self.selenium_try.clicks()

        # 过滤出需要提醒的学生
        self.excel_try.filters()

        # 初始化手机设置
        self.ui.init_device()

        # 小班课提醒
        self.send_to_one_type(self.excel_try.common_notice_list, 1)

        # 定制学有奖学金提醒
        self.send_to_one_type(self.excel_try.custom_with_scholarship_list, 2)

        # 定制学没有奖学金的提醒
        self.send_to_one_type(self.excel_try.custom_no_scholarship_list, 3)

        # 关闭数据库
        # self.data_base.close()

    current_1 = 1000
    current_2 = 1000
    current_3 = 65

    def send_to_one_type(self, student_list, notice_type):
        for student in student_list:
            index = self.show_process(student, student_list)
            if (index >= self.current_1 and notice_type == 1) or \
                    (index >= self.current_2 and notice_type == 2) or \
                    (index >= self.current_3 and notice_type == 3):
                while not self.ui.send_message(student, notice_type, self.messages[notice_type-1]):
                    self.ui.init_device()

    def show_process(self, student, student_list):
        index = 1 + student_list.index(student)
        print('****** 当前进度:' + str(index) + ' / ' + str(len(student_list)))
        return index


if __name__ == "__main__":
    main = Main()
    main.integrate()
