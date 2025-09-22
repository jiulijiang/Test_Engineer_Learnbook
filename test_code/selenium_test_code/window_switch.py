from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
wd = webdriver.Edge()
wd.get("http://121.43.169.97:8848/pageA.html")
wd.implicitly_wait(10)
wd.find_element(By.CSS_SELECTOR,'#username').send_keys("hello")
time.sleep(1)

