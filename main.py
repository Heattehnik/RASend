from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
# from functions import load_counters

# result = load_counters('2023-02-18')
url = 'https://support.fsa.gov.ru/'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
sleep(3)
form = '//*[@id="menu"]/div[12]'
form_control = driver.find_element(By.XPATH, form)
form_control.click()
sleep (2)
next_step = '//*[@id="metrology-report"]'
next_step_control = driver.find_element(By.XPATH, next_step)
next_step_control.click()
sleep(2)
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
ngr_control.send_keys('16078-13')
date = '//*[@id="measurementsForm"]/div[2]/div/div/input'
date_control = driver.find_element(By.XPATH, date)
date_control.clear()
date_control.send_keys('12022023')
valid = '//*[@id="measurementsForm"]/div[3]/div/div/input'
valid_control = driver.find_element(By.XPATH, valid)
valid_control.send_keys('6')
si_type = '//*[@id="measurementsForm"]/div[4]/div/div/input'
si_type_control = driver.find_element(By.XPATH, si_type)
si_type_control.send_keys('СГВ-15')
conclusion = '//*[@id="measurementsForm"]/div[5]/div/div/input'
conclusion_control = driver.find_element(By.XPATH, conclusion
                                         )
conclusion_control.send_keys('годен')
f = '//*[@id="measurementsForm"]/div[6]/div[1]/input'
i = '//*[@id="measurementsForm"]/div[6]/div[2]/input'
o = '//*[@id="measurementsForm"]/div[6]/div[3]/input'
driver.find_element(By.XPATH, f).send_keys('Пономарёв')
driver.find_element(By.XPATH, i).send_keys('Никита')
driver.find_element(By.XPATH, o).send_keys('Михайлович')


sleep(5)
driver.close()





# for i in result:
#     print(i['verification_date'], i['mit_number'], i['result_docnum'])
# print(len(result))






# 'valid_date'



