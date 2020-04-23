import time
from datetime import date

import uiautomator2 as u2


class UIAutomator2Try:
    fail_name = [
        '12138',  # 搜索排第一的是公众号
        '汪永姣18789552017',  # 未知
        '叮当喵～～',  # 未知
        '丿乀人生',  # 未知
        '唐丽芬',  # 未知
        '我要瘦瘦瘦',  # 未知
        'Aaron',  # 未知
        'Bumblebee',  # 未知
        '一代人'  # 第一个弹出的是群: B8-2组
        'O',  # 第一个弹出的是群: 南京opt....
        '默默',  # 名字有未知字符,找不到此人
        'Allison',  # 弹出公众号
        '风间澈',  # 查无此人
        'Name7',  # 查无此人
        '18816741613',  # 查无此人
        '广',  # 查无此人
        '慕子',  # 弹出公众号
        '甘甘 甜树体育',   # 第一个弹出的是群:
        'Chloe 🍒苗苗🍒',  # 弹出公众号
        '詹韵',    # 第一个弹出的是群:
    ]
    duplicate_name = [
        '娟子',  # 未知
        'wp',  # 未知
        'HUI',  # 未知
        '8...',  # 未知
        'Tina',  # 未知
        '猫',  # 未知
        'Anna',  #
        '燕',
        '甜',
        '迷路',
        'Candy',
        '雯',
    ]

    d = u2.connect('dd019e6')
    time_delay = 1
    stop = True
    today = date.isoweekday(date.today())

    def send_message(self, student, flag, message):

        if self.fail_or_duplicate(student):
            return

        if flag == 1:
            notice_days = ''
            for i in range(7):
                if student.common_notice_vector[i]:
                    if notice_days != '':
                        notice_days = notice_days + ', '
                    if i < self.today:
                        notice_days = notice_days + '本周' + str(i + 1)
                    elif i > self.today:
                        notice_days = notice_days + '上周' + str(i + 1)
            message = message.replace("d", str(self.today), 1)
            message = message.replace("d", notice_days, 1)
        elif flag == 2:
            if self.today - (student.accumulate_in_week + student.learn_in_today) < 2:
                return
            message = message.replace("d", str(self.today), 1)
            message = message.replace("d", str(student.accumulate_in_week + student.learn_in_today), 1)
            message = message.replace("d", str(5 - student.accumulate_in_week - student.learn_in_today), 1)
        elif flag == 3:
            if student.accumulate_in_week + student.learn_in_today >= 3:
                return
            message = message.replace("d", str(student.accumulate_in_week + student.learn_in_today), 1)

        # self.d.app_start("com.tencent.mm", stop=True)
        # self.time_delay_in()

        # click search button
        self.d.xpath("//*[@resource-id=\"com.tencent.mm:id/f0f\"]").click()  # can be replaced with xpath

        # send name
        self.time_delay_in()
        self.d.send_keys(student.name)
        self.time_delay_in()

        # click the first item
        self.d.click(122, 214)  # can be replaced with xpath

        # click the text pane
        self.d.xpath("//*[@resource-id=\"com.tencent.mm:id/fx6\"]").click()

        # send notice message
        self.time_delay_in()
        self.d.send_keys(message)
        self.time_delay_in()

        # click send button
        self.d.xpath("//*[@resource-id=\"com.tencent.mm:id/amb\"]").click()

        for i in range(3):
            self.d.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()
            self.time_delay_in()

    def time_delay_in(self):
        time.sleep(self.time_delay)

    def fail_or_duplicate(self, student):
        for failed in self.fail_name:
            if failed in student.name:
                return True
        for duplicated in self.duplicate_name:
            if duplicated in student.name:
                return True
        return False

    def initialize(self):
        self.d.app_start("com.tencent.mm", stop=True)
        for i in range(3):
            self.d.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()
            self.time_delay_in()
        self.d.app_start("com.tencent.mm", stop=True)
        self.time_delay_in()


if __name__ == "__main__":
    ui = UIAutomator2Try()
    ui.send_message()
