class Student:
    name = ''
    class_type = 0
    common_percentage_list = []
    common_notice_vector = [False, False, False, False, False, False, False]
    custom_minute_list = []
    scholarship = False
    accumulate_in_week = 0
    learn_in_today = 0
    remain_in_weak = 0

    def print(self):
        print("### A student info: ###")
        print(self.name)
        print(self.class_type)
        print(self.common_percentage_list)
        print(self.common_notice_vector)
        print(self.custom_minute_list)
        print(self.scholarship)
        print(self.accumulate_in_week)
        print(self.learn_in_today)
        print(self.remain_in_weak)
        print("###      done       ###")
