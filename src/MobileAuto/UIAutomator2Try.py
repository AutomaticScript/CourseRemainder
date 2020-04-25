import time
from datetime import date, datetime

import uiautomator2 as u2

from src.Entity.Student import Student
from src.Exceler.ExcelTry import ExcelTry


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
        '一代人',  # 第一个弹出的是群: B8-2组
        'O',  # 第一个弹出的是群: 南京opt....
        '默默',  # 名字有未知字符,找不到此人
        'Allison',  # 弹出公众号
        '风间澈',  # 查无此人
        'Name7',  # 查无此人
        '18816741613',  # 查无此人
        '广',  # 查无此人
        '慕子',  # 弹出公众号
        '甘甘 甜树体育',  # 第一个弹出的是群:
        'Chloe 🍒苗苗🍒',  # 弹出公众号
        '肥仔',  #
        '十二',  # 没查到这个人
        '淳',  # 删了我
        '.',  # 删了我
        '吴平娣',  # 没好友
        'wen',  # 没好友
        'Emily',  # 没好友
        # 2020-04-24
        '兔只🤣',  # 没好友
        '喇木',  # 没好友, 7班
        '萌萌萌😘😘😘',  # 公众号
        'SLydia',  # 身体不好
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
        '。',
        # 2020-04-24
        '浩',  # 11班, 3个重复
        '樂',  # 9班, 弹出的是'12 康乐'
        'huihui',  # 9班, 弹出的是'12 慧慧'
        '夕林语',  # 6班,不知为何给他发了两遍,已撤回
        '夕',
        'Bella',  # 7班,貌似也是两个人,不过我发送了
        'Sun',  # 7班和13班会重复
        '我',  # 我 和 我们
    ]

    def __init__(self):
        self.device = u2.connect('dd019e6')
        self.time_delay = 0.3  # unit is second
        self.today = date.isoweekday(date.today())

    def send_message(self, student, flag, message):
        try:
            if self.fail_or_duplicate(student):
                print("****** 此人找不到/重名")
                return True

            message = message.replace("d", str(self.today), 1)
            if flag == 1:
                message = self.update_message_1(message, student)
            elif flag == 2:
                if self.today - (student.accumulate_in_week + student.learn_in_today) < 2 \
                        or student.accumulate_in_week + student.learn_in_today >= 5:
                    return True
                message = self.update_message_2(message, student)
            elif flag == 3:
                if student.accumulate_in_week + student.learn_in_today >= 3:
                    return True
                message = self.update_message_3(message, student)

            self.core_send_steps(flag, message, student)
            return True

        except Exception:
            print("****** 发送消息失败, 准备自动重试")
            # print(Exception)
            return False

    def core_send_steps(self, flag, message, stu):
        self.print_log(stu, flag)
        # click the initial search button
        self.device.xpath('//*[@resource-id="com.tencent.mm:id/dhg"]/android.widget.ImageView[1]').click()
        # send student name to search bar
        # self.time_delay_in()
        self.device.send_keys(stu.name)
        self.time_delay_in()
        self.time_delay_in()
        # FIXME: click the right one
        # self.device.click(122, 214)
        # click the text bar
        # self.device.xpath("//*[@resource-id=\"com.tencent.mm:id/fx6\"]").click()
        # send customized message
        # self.device.send_keys(message)
        # click send message button
        # self.device.xpath("//*[@resource-id=\"com.tencent.mm:id/amb\"]").click()
        self.device.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()
        print("****** 发送消息成功! ")

        # for i in range(3):
            # return 3 times
            # self.device.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()

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

    def fail_or_duplicate(self, stu):
        ret_flag = False
        for failed in self.fail_name:
            if failed in stu.name:
                ret_flag = True
                break
        for duplicated in self.duplicate_name:
            if duplicated in stu.name:
                ret_flag = True
                break
        if ret_flag:
            print("dump")
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
        print('****** 当前进度:' + str(index) + ' / ' + str(len(excel_try.students)))
        ui.core_send_steps(flag=1, message="test", stu=student)
