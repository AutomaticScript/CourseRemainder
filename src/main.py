from datetime import datetime

from src.Exceler.ExcelTry import ExcelTry
from src.MobileAuto.UIAutomator2Try import UIAutomator2Try
from src.WebCrawler.SeleniumTry import SeleniumTry

common_message = \
    "[小班课]今天周d，小班课d还没学完，学习贵在持之以恒，加油！"
custom_message_with_scholarship = \
    "[定制学]今天周d，本周定制学已经打卡d次，加油还差d次即可达到本周的奖学金要求！"
custom_message_no_scholarship = \
    "[定制学]一周完成3天打卡，本周定制学已完成d天，可以拿到Alicia整理的本part精华词汇哦，今天就开始吗？"


def foo():
    # selenium_try = SeleniumTry()
    # selenium_try.clicks()

    excel_try = ExcelTry()
    excel_try.filters()

    ui = UIAutomator2Try()
    ui.initialize()

    for student in excel_try.common_notice_list:
        student.print()
        time_stamp = datetime.now()
        print('当前时间:' + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))
        index = 1+excel_try.common_notice_list.index(student)
        print('当前进度:' + str(1+excel_try.common_notice_list.index(student))
              + ' / ' + str(len(excel_try.common_notice_list)))
        if index >= 256:
            ui.send_message(student, 1, common_message)
        print()

    # for student in excel_try.custom_with_scholarship_list:
    #     student.print()
    #     ui.send_message(student, 2, custom_message_with_scholarship)
    #
    # for student in excel_try.custom_no_scholarship_list:
    #     student.print()
    #     ui.send_message(student, 3, custom_message_no_scholarship)


if __name__ == "__main__":
    foo()
