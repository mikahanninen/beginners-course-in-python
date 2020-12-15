""" An example robot. """
from RPA.core.notebook import notebook_print
from RPA.Archive import Archive
from RPA.Browser import Browser
from RPA.Excel.Files import Files
from RPA.HTTP import HTTP
from RPA.PDF import PDF
from RPA.Robocloud.Secrets import Secrets
from pathlib import Path
from time import sleep
import logging
import shutil
import sys

# +
''' variables '''
archive = Archive()
browser = Browser()
excel = Files()
http = HTTP()
pdf = PDF()

output_dir = Path('.') / 'output'
image_dir = output_dir / 'images'
pdf_dir = output_dir / 'pdfs'


# -

def setup_logging():
    fileout = logging.FileHandler(filename='debug.log')
    stdout = logging.StreamHandler(sys.stdout)
    logging.basicConfig(
        level=logging.INFO,
        format="[{%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
        handlers=[
            stdout,
            fileout
        ],
    )


def log_in():
    browser.wait_until_element_is_visible('id:username')
    browser.input_text('id:username', 'maria')
    browser.input_text('id:password', 'thoushallnotpass')
    browser.submit_form()
    browser.wait_until_page_contains_element('id:sales-form')


def download_excel_file():
    http.download('https://robotsparebinindustries.com/SalesData.xlsx', overwrite=True)


def open_page():
    browser.open_available_browser('https://robotsparebinindustries.com/', headless=True)


def close_page():
    browser.close_all_browsers()


def fill_in_one_person(person):
    first_name = person['First Name']
    last_name = person['Last Name']
    name_file = str(first_name + last_name).lower().replace(" ", "_")+".png"

    target_file = str(image_dir / name_file)
    browser.input_text('firstname', person['First Name'])
    browser.input_text('lastname', person['Last Name'])
    browser.input_text('salesresult', person['Sales'])
    browser.select_from_list_by_value('salestarget', str(person['Sales Target']))
    browser.click_button('Submit')
    browser.capture_element_screenshot('//div[@id="sales-results"]//tbody//tr[1]', target_file)


def loop_persons():
    excel.open_workbook('SalesData.xlsx')
    persons = excel.read_worksheet_as_table(header=True)
    excel.close_workbook()
    for person in persons:
        fill_in_one_person(person)


def collect_the_results():
    target_file = str(image_dir / 'sales_summary.png')
    browser.screenshot('css:div.sales-summary', target_file)


def export_sales_as_pdf():
    target_file = str(pdf_dir / 'sales_summary.pdf')
    browser.wait_until_element_is_visible('id:sales-results')
    html = browser.get_element_attribute('id:sales-results', 'outerHTML')
    pdf.html_to_pdf(html, target_file)


def log_out_and_close_browser():
    browser.click_button('Log out')
    browser.close_browser()


def zip_results():
    archive.archive_folder_with_zip(str(output_dir), str(output_dir / 'sales.zip'), recursive=True, exclude='*.zip')


def clear_previous_run():
    try:
        shutil.rmtree(str(image_dir))
    except Exception:
        pass
    try:
        shutil.rmtree(str(pdf_dir))
    except Exception:
        pass


if __name__ == "__main__":
    all_steps_done = False
    try:
        clear_previous_run()
        download_excel_file()
        open_page()
        log_in()
        loop_persons()
        collect_the_results()
        export_sales_as_pdf()
        log_out_and_close_browser()
        zip_results()
        all_steps_done = True
    finally:
        notebook_print(f"Run result: {all_steps_done}")
        close_page()
