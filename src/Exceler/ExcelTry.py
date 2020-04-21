from os import listdir
from os.path import isfile, join

from openpyxl import load_workbook
from src.WebCrawler.SeleniumTry import SeleniumTry


class ExcelTry:

    def filters(self):
        # TODO: find students need to be noticed
        input_files = [f for f in listdir(SeleniumTry.download_dir)
                       if isfile(join(SeleniumTry.download_dir, f))
                       ]
        for file_name in input_files:
            workbook = load_workbook(filename=SeleniumTry.download_dir + '/' + file_name)
            print(file_name)
            sheet = workbook.get_sheet_by_name('学生运营')
            print(sheet.cell(row=1, column=1).value)
            print(sheet.cell(row=2, column=1).value)


if __name__ == "__main__":
    excelTry = ExcelTry()
    excelTry.filters()
