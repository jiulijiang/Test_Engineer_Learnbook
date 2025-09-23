from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

wd = webdriver.Edge()
wd.get('https://hmshop-test.itheima.net/index.php/Home/Index/index.html')


# 使用显式等待点击登录按钮
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '.nologin>a')).click()

# 使用显式等待输入用户名
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#username')).send_keys('13600000000')

# 使用显式等待输入密码
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#password')).send_keys('123456')

# 使用显式等待输入验证码
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#verify_code')).send_keys('8888')

# 使用显式等待点击登录按钮
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '.sbtbutton')).click()

sleep(3)
wd.quit()