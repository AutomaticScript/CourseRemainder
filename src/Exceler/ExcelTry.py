from os import listdir
from os.path import isfile, join
from datetime import date

from openpyxl import load_workbook
from src.WebCrawler.SeleniumTry import SeleniumTry
from src.Entity.Student import Student


class ExcelTry:
    x = [
        ['0000000', '1000000', '1100000', '1110000', '0111000', '0011000', '0001000'],
        ['0000100', '0000000', '0100000', '0110000', '0111000', '0011100', '0001100']
    ]
    common_notice_list = []
    custom_with_scholarship_list = []
    custom_no_scholarship_list = []
    student = Student()
    today = date.isoweekday(date.today())

    # today = 2

    def filters(self):
        input_files = [f for f in listdir(SeleniumTry.download_dir)
                       if isfile(join(SeleniumTry.download_dir, f)) and f.endswith('xlsx')
                       ]
        count = 0
        for file_name in input_files:
            if '8班' in file_name:
                continue
            print(file_name)
            workbook = load_workbook(filename=SeleniumTry.download_dir + '/' + file_name)
            sheet = workbook.get_sheet_by_name('学生运营')

            first_row = True
            for row in sheet.rows:
                if first_row:
                    first_row = False
                    continue
                line = [col.value for col in row]
                self.construct_student(line, file_name)
                # self.student.print()
                # if self.student.name == "Yolanda":
                self.judge_student()

            count = count + 1
            # if count > 0:
            #     break
        self.print()

    def has_scholarship(self, state_str):
        if state_str is None:
            return False
        first = int(state_str[0:state_str.find('/')])
        second = int(state_str[state_str.find('/') + 1:len(state_str)])
        if first + 1 == second:
            return True
        else:
            return False

    def change_order(self, a_list, offset):
        return a_list[offset:7] + a_list[0:offset]

    def construct_student(self, line, file_name):
        self.student = Student()
        self.student.name = line[0]
        self.student.class_index = file_name
        if '7班' in file_name or '13班' in file_name:
            self.student.class_type = 0
        else:
            self.student.class_type = 1

        self.student.common_percentage_list = self.change_order(line[5:12], 8 - self.today)
        common_notice_vector = []
        for i in range(7):
            common_notice_vector.append(False)
        self.student.common_notice_vector = common_notice_vector
        self.student.custom_minute_list = self.change_order(line[13:20], 7 - self.today)
        self.student.scholarship = self.has_scholarship(line[27])

    def judge_student(self):
        # 小班课
        notice_vector = self.x[self.student.class_type][self.today - 1]
        count = 0
        append_flag = False
        for flag in notice_vector:
            if flag is '1' and self.student.common_percentage_list[count] < 0.7:
                self.student.common_notice_vector[count] = True
                append_flag = True
                if self.student.name == 'Yolanda':
                    self.student.print()
            count = count + 1
        if append_flag:
            self.common_notice_list.append(self.student)

        # 定制学
        self.student.accumulate_in_week = 0
        for i in range(self.today - 1):
            if self.student.custom_minute_list[i] >= 30.0:
                self.student.accumulate_in_week = self.student.accumulate_in_week + 1
        self.student.learn_in_today = 0
        if self.student.custom_minute_list[self.today - 1] >= 30.0:
            self.student.learn_in_today = 1

        if self.student.scholarship:
            self.student.remain_in_weak = 5 - self.student.accumulate_in_week - self.student.learn_in_today
            if self.student.remain_in_weak <= 8 - self.today - self.student.learn_in_today:
                self.custom_with_scholarship_list.append(self.student)
            else:
                self.student.scholarship = False
                self.custom_no_scholarship_list.append(self.student)
        else:
            self.student.remain_in_weak = 3 - self.student.accumulate_in_week - self.student.learn_in_today
            self.custom_no_scholarship_list.append(self.student)

    def print(self):
        print('### 学生分类情况 ###')
        for student in self.common_notice_list:
            student.print()
        print('--- 定制学情况有奖学金 ----')
        for student in self.custom_with_scholarship_list:
            student.print()
        print('--- 定制学情况没有奖学金 ----')
        for student in self.custom_no_scholarship_list:
            student.print()
        print('###    end     ###')


if __name__ == "__main__":
    excelTry = ExcelTry()
    excelTry.filters()
