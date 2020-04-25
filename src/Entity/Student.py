class Student:
    name = ''
    class_index = ''
    class_type = 0
    common_percentage_list = []
    common_notice_vector = []
    custom_minute_list = []
    scholarship = False
    accumulate_in_week = 0
    learn_in_today = 0
    remain_in_weak = 0

    def print(self, flag):
        print()
        print("###### 学生信息")
        print("###### 姓名: " + self.name)
        print("###### 班级: " + self.class_index)

        if self.class_type == 0:
            print("###### 班级类型: A")
        else:
            print("###### 班级类型: B")

        if flag == 1:
            print("###### 小班课(周一到周日): " + ', '.join(str(e) for e in self.common_percentage_list))
            print("###### 小班课是否需要提醒: " + ', '.join(str(e) for e in self.common_notice_vector))
        else:
            print("###### 定制学(周一到周日): " + ', '.join(str(e) for e in self.custom_minute_list))
            print("###### 是否有奖学金: " + str(self.scholarship))
            print("###### 本周累计已学天数(不含今天): " + str(self.accumulate_in_week))
            print("###### 今天是否学习: " + str(self.learn_in_today))
            print("###### 还剩几天获得奖学金/助教奖励: " + str(self.remain_in_weak))

        print("###### \n")

