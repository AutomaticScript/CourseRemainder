from src.Exceler.ExcelTry import ExcelTry
from src.MobileAuto.UIAutomator2Try import UIAutomator2Try
from src.WebCrawler.SeleniumTry import SeleniumTry

common_message = \
    ""
custom_message_with_scholarship = \
    "今天周d，本周定制学已经打卡d次，还差d次！"
custom_message_no_scholarship = \
    "一周完成3天打卡，本周已完成d天，可以拿到Alicia整理的本part精华词汇哦，今天就开始吗？"


def foo():
    selenium_try = SeleniumTry()
    selenium_try.clicks()

    excel_try = ExcelTry()
    excel_try.filters()

    ui = UIAutomator2Try()

    # for student in excel_try.common_notice_list:
    #     ui.send_message(student, 1, common_message)

    # for student in excel_try.custom_with_scholarship_list:
    #     print(student.name)
    #     ui.send_message(student, 2, custom_message_with_scholarship)

    # for student in excel_try.custom_no_scholarship_list:
    #     ui.send_message(student, 3, custom_message_no_scholarship)


if __name__ == "__main__":
    foo()
