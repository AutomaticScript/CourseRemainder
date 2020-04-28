import time
from datetime import date, datetime

import uiautomator2 as u2

from src.Exceler.ExcelTry import ExcelTry


class UIAutomator2Try:

    def __init__(self):
        self.index = 0
        self.device = u2.connect('dd019e6')
        self.time_delay = 0.3  # unit is second
        self.today = date.isoweekday(date.today())

    def send_message(self, stu, flag, message):
        try:
            if self.find_no_friend(stu):
                print("****** 此人非好友")
                return True

            # message = message.replace("d", str(self.today), 1)
            if flag == 1:
                message = self.update_message_1(message, stu)
            elif flag == 2:
                if self.today - (stu.accumulate_in_week + stu.learn_in_today) < 2 \
                        or stu.accumulate_in_week + stu.learn_in_today >= 5:
                    return True
                message = self.update_message_2(message, stu)
            elif flag == 3:
                if stu.accumulate_in_week + stu.learn_in_today >= 3:
                    return True
                message = self.update_message_3(message, stu)

            self.core_send_steps(flag, message, stu)
            return True

        except Exception:
            print("****** 发送消息失败, 准备自动重试")
            # print(Exception)
            return False

    def core_send_steps(self, flag, message, stu):
        global keys
        self.print_log(stu, flag)
        # click the initial search button
        self.device.xpath('//*[@resource-id="com.tencent.mm:id/dhg"]/android.widget.ImageView[1]').click()
        # send student name to search bar
        # self.time_delay_in()

        keys = str(stu.class_index) + ' ' + stu.name
        self.device.send_keys(keys)
        self.time_delay_in()
        self.time_delay_in()

        # FIXME: click the right one
        self.device.click(122, 214)
        # click the text bar
        self.device.xpath("//*[@resource-id=\"com.tencent.mm:id/fx6\"]").click()
        # send customized message
        self.device.send_keys(message)
        # click send message button
        self.device.xpath("//*[@resource-id=\"com.tencent.mm:id/amb\"]").click()
        # self.device.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()
        # self.device.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()
        print("****** 发送消息成功! ")

        for i in range(3):
            self.device.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()

    def update_message_3(self, message, stu):
        message = message.replace("d", str(stu.accumulate_in_week + stu.learn_in_today), 1)
        return message

    def update_message_2(self, message, stu):
        message = message.replace("d", str(stu.accumulate_in_week + stu.learn_in_today), 1)
        message = message.replace("d", str(5 - stu.accumulate_in_week - stu.learn_in_today), 1)
        return message

    def update_message_1(self, message, stu):
        notice_days = ''
        for i in range(7):
            if stu.common_notice_vector[i]:
                if notice_days != '':
                    notice_days = notice_days + ', '
                if i < self.today:
                    notice_days = notice_days + '本周' + str(i + 1)
                elif i > self.today:
                    notice_days = notice_days + '上周' + str(i + 1)
        message = message.replace("d", notice_days, 1)
        return message

    def time_delay_in(self):
        time.sleep(self.time_delay)

    no_friends = [
        "一代人", "汪永姣18789552017",
        "吴平娣", "wen", "Tina", "丿乀人生", "唐丽芬", "我要瘦瘦瘦", "Aaron", "雯", "Emily", "。",
    ]

    def find_no_friend(self, stu):
        for failed in self.no_friends:
            if failed == stu.name or "默默" in failed:  # strange emoji
                return True
        return False

    def init_device(self):
        self.device.app_start("com.tencent.mm", stop=True)
        self.time_delay_in()
        for i in range(3):
            self.device.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()
        self.device.app_start("com.tencent.mm", stop=True)
        self.time_delay_in()

    def print_log(self, stu, flag):
        stu.print(flag)
        time_stamp = datetime.now()
        print('****** 当前时间:' + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))


if __name__ == "__main__":
    ui = UIAutomator2Try()
    ui.init_device()
    excel_try = ExcelTry()
    excel_try.filters()
    for student in excel_try.students:
        index = 1 + excel_try.students.index(student)
        print('\n****** 当前进度:' + str(index) + ' / ' + str(len(excel_try.students)))
        if index >= ui.index:
            ui.core_send_steps(flag=1, message="test", stu=student)
