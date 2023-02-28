from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from functions import load_counters

result = load_counters('2023-02-18')

for i in result:
    print(i['verification_date'], i['mit_number'], i['result_docnum'])
print(len(result))






# 'valid_date'



