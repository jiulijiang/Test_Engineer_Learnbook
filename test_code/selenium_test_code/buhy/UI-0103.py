from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from can_reuesu_code import login
import time
wd = webdriver.Edge()
login.login_byhy(wd, "http://127.0.0.1:8080")
element_button = wd.find_element(By.CSS_SELECTOR, ".content >div.add-one-area > button")
element_button.click()

element_customer_name = wd.find_element(By.CSS_SELECTOR, ".content >div.add-one-area >div:nth-child(2) >div:nth-child(1) input")
element_customer_name.send_keys("南京中医院")

element_customer_phone = wd.find_element(By.CSS_SELECTOR, ".content >div.add-one-area >div:nth-child(2) >div:nth-child(2) input")
element_customer_phone.send_keys("13888888888")

element_customer_address = wd.find_element(By.CSS_SELECTOR, ".content >div.add-one-area >div:nth-child(2) >div:nth-child(3)>textarea")
element_customer_address.send_keys("江苏省南京市江宁路")

element_add_button = wd.find_element(By.CSS_SELECTOR, ".content >div.add-one-area  > div> button:nth-child(1)")
element_add_button.click()

element_change_button = wd.find_element(By.CSS_SELECTOR, ".content > div:nth-child(3) label:nth-child(1)")
element_change_button.click()

element_customer_name = wd.find_element(By.CSS_SELECTOR, ".content > div:nth-child(3) div[style='margin-top: 1em;']:nth-child(1) input")
element_customer_name.clear()

element_customer_name.send_keys("南京省中医院")
element_change_button.click()

element_custom_message = wd.find_element(By.CSS_SELECTOR, ".content > div:nth-child(3)")
print(element_custom_message.text)

wd.quit()