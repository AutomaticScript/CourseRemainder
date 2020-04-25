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

    d = u2.connect('dd019e6')
    time_delay = 0.3
    stop = True
    today = date.isoweekday(date.today())

    def send_message(self, student, flag, message):
        try:
            if self.fail_or_duplicate(student):
                return True

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
                if self.today - (student.accumulate_in_week + student.learn_in_today) < 2 \
                        or student.accumulate_in_week + student.learn_in_today >= 5:
                    print("****** 此人表现优秀, 无需提醒")
                    return True
                else:
                    print("****** 此人需要提醒")
                message = message.replace("d", str(self.today), 1)
                message = message.replace("d", str(student.accumulate_in_week + student.learn_in_today), 1)
                message = message.replace("d", str(5 - student.accumulate_in_week - student.learn_in_today), 1)
            elif flag == 3:
                if student.accumulate_in_week + student.learn_in_today >= 3:
                    return True
                message = message.replace("d", str(student.accumulate_in_week + student.learn_in_today), 1)

            # self.d.app_start("com.tencent.mm", stop=True)
            # self.time_delay_in()

            # click search button
            self.d.xpath('//*[@resource-id="com.tencent.mm:id/dhg"]/android.widget.ImageView[1]').click()
            # self.d.xpath("//*[@resource-id=\"com.tencent.mm:id/f0f\"]").click()  # can be replaced with xpath

            # send name
            self.time_delay_in()
            self.d.send_keys(student.name)
            self.time_delay_in()
            self.time_delay_in()

            # click the first item
            self.d.click(122, 214)  # can be replaced with xpath

            # click the text pane
            self.d.xpath("//*[@resource-id=\"com.tencent.mm:id/fx6\"]").click()

            # send notice message
            # self.time_delay_in()
            # self.d.send_keys(message)
            # self.time_delay_in()

            # click send button
            # self.d.xpath("//*[@resource-id=\"com.tencent.mm:id/amb\"]").click()
            print("****** 此人已经提醒了")

            for i in range(3):
                self.d.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()
            return True
        except Exception:
            print("****** 脚本执行失败")
            return False

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
