from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from can_reuesu_code import login
import time
wd = webdriver.Edge()
login.login_byhy(wd, "http://127.0.0.1:8080")
element_button = wd.find_element(By.CSS_SELECTOR, ".content >div.add-one-area > button")
element_button.click()
sleep(1)
element_customer_name = wd.find_element(By.CSS_SELECTOR, ".content >div.add-one-area >div:nth-child(2) >div:nth-child(1) input")
element_customer_name.send_keys("南京中医院")
sleep(1)
element_customer_phone = wd.find_element(By.CSS_SELECTOR, ".content >div.add-one-area >div:nth-child(2) >div:nth-child(2) input")
element_customer_phone.send_keys("13888888888")
sleep(1)
element_customer_address = wd.find_element(By.CSS_SELECTOR, ".content >div.add-one-area >div:nth-child(2) >div:nth-child(3)>textarea")
element_customer_address.send_keys("江苏省南京市江宁路")
sleep(1)
element_add_button = wd.find_element(By.CSS_SELECTOR, ".content >div.add-one-area  > div> button:nth-child(1)")
element_add_button.click()
sleep(1)
element_custom_message = wd.find_element(By.CSS_SELECTOR, ".content > div:nth-child(3)")
print(element_custom_message.text)
sleep(1)
wd.quit()