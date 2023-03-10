import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from env import DATA_BASE

connect = sqlite3.connect(DATA_BASE, check_same_thread=False)
cursor = connect.cursor()


def load_counters(date: str) -> list:
    cursor.execute(f'SELECT * FROM uploaded_data WHERE verification_date LIKE "%{date}%"')
    fetch = cursor.fetchall()
    return fetch


def make_dict(list_: list) -> dict:
    dict_ = {}
    for item in list_:
        dict_[item[0]] = {
            'ngr': item[2],
            'verification_date': item[9],
            'valid_for': item[11],
            'si_type': item[3],
            'conclusion': item[12],
            'surname': item[23],
            'name': item[24],
            'patronymic': item[25],
        }
    return dict_


def main(dict_: dict) -> tuple:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1280,1024")
    url = 'https://support.fsa.gov.ru/'
    iteration = 0
    errors_count = 0
    for key, value in dict_.items():
        try:
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            sleep(7)
            form = '//*[@id="menu"]/div[12]'
            form_control = driver.find_element(By.XPATH, form)
            form_control.click()
            registry_num = value['ngr']
            splited_verification_date = value['verification_date'].partition(' ')[0].split('-')
            splited_verification_date.reverse()
            verification_date = ''.join(splited_verification_date)
            print(verification_date)
            vaild_for = value['valid_for']
            sitype = value['si_type']
            is_valid = value['conclusion']
            name = value['name']
            surname = value['surname']
            patronymic = value['patronymic']
            sleep(1)
            next_step = '//*[@id="metrology-report"]'
            next_step_control = driver.find_element(By.XPATH, next_step)
            next_step_control.click()
            sleep(1)
            form_choice = '//*[@id="metrologyReportForm"]/div[1]/div/select/option[4]'
            form_choice_control = driver.find_element(By.XPATH, form_choice)
            form_choice_control.click()
            sleep(1)
            akk_num = '//*[@id="metrologyReportForm"]/div[2]/div/div[1]/div/input'
            akk_num_control = driver.find_element(By.XPATH, akk_num)
            akk_num_control.clear()
            akk_num_control.send_keys('320019')
            email = '//*[@id="metrologyReportForm"]/div[3]/div/div/input'
            email_control = driver.find_element(By.XPATH, email)
            email_control.send_keys('alexdyachenko@mail.ru')
            ngr = '//*[@id="measurementsForm"]/div[1]/div/div/input'
            ngr_control = driver.find_element(By.XPATH, ngr)
            ngr_control.send_keys(registry_num)
            date = '//*[@id="measurementsForm"]/div[2]/div/div/input'
            date_control = driver.find_element(By.XPATH, date)
            date_control.clear()
            date_control.send_keys(verification_date)
            valid = '//*[@id="measurementsForm"]/div[3]/div/div/input'
            valid_control = driver.find_element(By.XPATH, valid)
            valid_control.send_keys(vaild_for)
            si_type = '//*[@id="measurementsForm"]/div[4]/div/div/input'
            si_type_control = driver.find_element(By.XPATH, si_type)
            si_type_control.send_keys(sitype)
            conclusion = '//*[@id="measurementsForm"]/div[5]/div/div/input'
            conclusion_control = driver.find_element(By.XPATH, conclusion)
            conclusion_control.send_keys(is_valid)
            f = '//*[@id="measurementsForm"]/div[6]/div[1]/input'
            i = '//*[@id="measurementsForm"]/div[6]/div[2]/input'
            o = '//*[@id="measurementsForm"]/div[6]/div[3]/input'
            driver.find_element(By.XPATH, f).send_keys(surname)
            driver.find_element(By.XPATH, i).send_keys(name)
            driver.find_element(By.XPATH, o).send_keys(patronymic)
            driver.get_screenshot_as_file(f'../screenshots/{iteration}-{verification_date}-{surname}.png')
            submit = '//*[@id="metrology-report-submit"]'
            submit_control = driver.find_element(By.XPATH, submit)
            sleep(2)
            submit_control.click()
            sleep(3)
            driver.close()
            iteration += 1
        except:
            errors_count += 1
            continue
    return iteration, len(dict_), errors_count



