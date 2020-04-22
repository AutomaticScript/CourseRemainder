import time
from datetime import date

import uiautomator2 as u2


class UIAutomator2Try:
    d = u2.connect('dd019e6')
    time_delay = 1
    stop = True
    today = date.isoweekday(date.today())

    def send_message(self, student, flag, message):
        # 默默　12138 汪永姣18789552017 叮当喵～～  丿乀人生 唐丽芬 我要瘦瘦瘦 Aaron Bumblebee
        # 娟子　wp HUI 8... Tina 猫
        if "Bumblebee" in student.name:
            self.stop = False
            return
        if self.stop:
            return

        if flag == 1:
            message = message.replace("d", "XX", 1)
        elif flag == 2:
            if self.today - (student.accumulate_in_week + student.learn_in_today) < 2:
                return
            message = message.replace("d", str(self.today), 1)
            message = message.replace("d", str(student.accumulate_in_week+student.learn_in_today), 1)
            message = message.replace("d", str(5-student.accumulate_in_week-student.learn_in_today), 1)
        elif flag == 3:
            if student.accumulate_in_week + student.learn_in_today >= 3:
                return
            message = message.replace("d", str(student.accumulate_in_week+student.learn_in_today), 1)

        self.d.app_start("com.tencent.mm", stop=True)
        self.time_delay_in()
        self.d.click(564, 75)
        self.time_delay_in()

        # find by name
        self.d.send_keys(student.name)
        self.time_delay_in()
        self.d.click(122, 214)
        self.time_delay_in()
        self.d.xpath("//*[@resource-id=\"com.tencent.mm:id/fx6\"]").click()
        self.time_delay_in()

        # template
        self.d.send_keys(message)
        self.time_delay_in()
        self.d.xpath("//*[@resource-id=\"com.tencent.mm:id/amb\"]").click()
        self.time_delay_in()
        self.d.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()
        self.time_delay_in()
        self.d.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()
        self.time_delay_in()
        self.d.xpath("//*[@resource-id=\"com.android.systemui:id/back\"]").click()
        self.time_delay_in()
        
    def time_delay_in(self):
        time.sleep(self.time_delay)


if __name__ == "__main__":
    ui = UIAutomator2Try()
    ui.send_message()
