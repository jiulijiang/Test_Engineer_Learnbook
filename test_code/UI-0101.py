from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Edge()
wd.implicitly_wait(10)
wd.get("http://127.0.0.1:8080")
element_login_username = wd.find_element(By.CSS_SELECTOR,'#username')
element_login_username.send_keys('byhy')
element_login_password = wd.find_element(By.CSS_SELECTOR,'#password')
element_login_password.send_keys('88888888\n')
elements_menu = wd.find_elements(By.CSS_SELECTOR,'.sidebar-menu > li > a > span')[:3]
print("左侧菜单前三项是：")
for element_menue in elements_menu:
    print(element_menue.text)

wd.quit()