from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import csv

def get_data_csv(major, semester):
    DRIVER_PATH = '/Users/shugefan/Desktop/Flask Into/backend/chromedriver'
    GT_WEBSITE_PATH = "https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_dyn_sched"
    driver = webdriver.Chrome(DRIVER_PATH)

    driver.get(GT_WEBSITE_PATH)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text(semester)

    csv_file = open('./result.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Class', 'Section', 'Type'])

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Submit'][@type='submit']"))
    )

    element.click()

    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text(major)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Class Search'][@type='submit']"))
    )

    element.click()

    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "datadisplaytable"))
    )

    items = element.find_elements_by_class_name("ddtitle")
    types = element.find_elements_by_class_name("dddefault")
    type_list = []
    for single_type in types:
        if len(single_type.text) > 80:
            type_list.append(single_type)
    i = 0
    for item in items:
        info = item.text.split(' - ')
        class_name = info[2]
        section = info[3]
        info = type_list[i].text
        info2 = info.split('Schedule Type')
        temp = info2[1]
        info3 = temp.split('Method')
        instruType = info3[0].replace('\n', '') + "Method"
        if len(instruType) > 60 or str(instruType).find("Instructional") == -1:
            instruType = "Not specified at this time"
        i += 1
        csv_writer.writerow([class_name, section, instruType])

    driver.close()