from RPA.HTTP import HTTP
from RPA.Excel.Files import Files
from RPA.Robocloud.Items import Items
from RPA.FileSystem import FileSystem

""" variables """
http = HTTP()
excel = Files()
workitems = Items()
files = FileSystem()


def download_excel_file():
    http.download("https://robotsparebinindustries.com/SalesData.xlsx", overwrite=True)


def read_data_from_excel():
    excel.open_workbook("SalesData.xlsx")
    persons = excel.read_worksheet_as_table(header=True)
    excel.close_workbook()
    files.remove_file("SalesData.xlsx")
    workitems.load_work_item_from_environment()
    workitems.set_work_item_variable("persons", persons.to_list())
    workitems.save_work_item()


if __name__ == "__main__":
    download_excel_file()
    read_data_from_excel()
