import time
from datetime import date

import uiautomator2 as u2


class UIAutomator2Try:
    d = u2.connect('dd019e6')
    time_delay = 1
    stop = True
    today = date.isoweekday(date.today())

    def send_message(self, student, flag, message):
        # if student.name == "YOYO" and student.class_index == "懂你精品小班-Alicia.Shen 8班-20200422.xlsx":
        #     self.stop = False
        #     return
        # if self.stop:
        #     return

        if flag == 1:
            message = message.replace("d", "XX", 1)
        elif flag == 2:
            if self.today - (student.accumulate_in_week + student.learn_in_today) < 2:
                return
            message = message.replace("d", str(self.today), 1)
            message = message.replace("d", str(student.accumulate_in_week+student.learn_in_today), 1)
            message = message.replace("d", str(5-student.accumulate_in_week-student.learn_in_today), 1)
        elif flag == 3:
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
