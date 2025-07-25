from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from can_reuesu_code import login

wd = webdriver.Edge()
login.login_byhy(wd, "http://127.0.0.1:8080")
element_medicine_mnue = wd.find_element(By.CSS_SELECTOR,'.sidebar-menu >li:nth-child(3)')
element_medicine_mnue.click()
element_medicine_add = wd.find_element(By.CSS_SELECTOR,'.add-one-area >button')
element_medicine_add.click()
element_medicine_add_name = wd.find_element(By.CSS_SELECTOR,'.add-one-area>div:nth-child(2)>div:nth-child(1) input')
element_medicine_add_name.send_keys("阿司匹林")
element_medicine_add_number = wd.find_element(By.CSS_SELECTOR,'.add-one-area>div:nth-child(2)>div:nth-child(2) input')
element_medicine_add_number.send_keys("10120")
element_medicine_add_description = wd.find_element(By.CSS_SELECTOR,'.add-one-area>div:nth-child(2)>div:nth-child(3) textarea')
element_medicine_add_description.send_keys("阿司匹林的药品描述")
element_medicine_add_creat = wd.find_element(By.CSS_SELECTOR,'.add-one-area div>button:nth-child(1)')
element_medicine_add_creat.click()
element_first_medicine = wd.find_element(By.CSS_SELECTOR,'.search-result-item')
print(element_first_medicine.text)
sleep(2)
wd.quit()