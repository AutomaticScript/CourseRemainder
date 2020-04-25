import subprocess
from datetime import datetime

import sqlite3

from src.DataBase.DataBase import DataBase
from src.Exceler.ExcelTry import ExcelTry
from src.MobileAuto.UIAutomator2Try import UIAutomator2Try
from src.WebCrawler.SeleniumTry import SeleniumTry

common_message = \
    "今天周d,明天晚上还有新的小班课,不过小班课d还没学完，今儿都扫尾完成吧~"
custom_message_with_scholarship = \
    "[定制学]今天周d，本周定制学已经打卡d次，加油！"
custom_message_no_scholarship = \
    "[定制学]本周定制学已完成d天，一周完成3天打卡，就可以拿到Alicia整理的本part精华词汇哦，再坚持一下吧~"




def foo():
    # 从网页读取数据
    # selenium_try = SeleniumTry()
    # selenium_try.clicks()

    # 过滤出需要提醒的学生
    excel_try = ExcelTry()
    excel_try.filters()

    # 初始化手机设置
    # ui = UIAutomator2Try()
    # ui.initialize()

    # DB init
    dataBase = DataBase()

    # 小班课提醒
    # for student in excel_try.common_notice_list:
    #     print_log(student)
    #     index = 1+excel_try.common_notice_list.index(student)
    #     print('****** 当前进度:' + str(1+excel_try.common_notice_list.index(student))
    #           + ' / ' + str(len(excel_try.common_notice_list)))
    #     if index >= 0:
    #         flag = ui.send_message(student, 1, common_message)
    #         while not flag:
    #             ui.initialize()
    #             flag = ui.send_message(student, 1, common_message)

    # 定制学有奖学金提醒
    # for student in excel_try.custom_with_scholarship_list:
    #     print_log(student)
    #     index = 1 + excel_try.custom_with_scholarship_list.index(student)
    #     print('****** 当前进度:' + str(1 + excel_try.custom_with_scholarship_list.index(student))
    #           + ' / ' + str(len(excel_try.custom_with_scholarship_list)))
    #     if index >= 0:
    #         flag = ui.send_message(student, 2, custom_message_with_scholarship)
    #         while not flag:
    #             ui.initialize()
    #             flag = ui.send_message(student, 2, custom_message_with_scholarship)

    # 定制学没有奖学金的提醒
    # for student in excel_try.custom_no_scholarship_list:
    #     print_log(student)
    #     index = 1 + excel_try.custom_no_scholarship_list.index(student)
    #     print('****** 当前进度:' + str(1 + excel_try.custom_no_scholarship_list.index(student))
    #           + ' / ' + str(len(excel_try.custom_no_scholarship_list)))
    #     if index >= 0:
    #         flag = ui.send_message(student, 3, custom_message_no_scholarship)
    #         while not flag:
    #             ui.initialize()
    #             flag = ui.send_message(student, 3, custom_message_no_scholarship)

    dataBase.conn.close()


def print_log(student):
    student.print()
    time_stamp = datetime.now()
    print('****** 当前时间:' + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))


if __name__ == "__main__":
    foo()
