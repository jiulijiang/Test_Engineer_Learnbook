import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

wd = webdriver.Edge()
wd.get('https://hmshop-test.itheima.net/index.php/Home/Index/index.html')

wd.maximize_window()

# 使用显式等待点击登录按钮
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '.nologin>a')).click()

# 使用显式等待输入用户名
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#username')).send_keys('13600000000')

# 使用显式等待输入密码
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#password')).send_keys('123456')

# 使用显式等待输入验证码
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#verify_code')).send_keys('8888')

# 使用显式等待点击登录按钮
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, 'a[name="sbtbutton"]')).click()

# 使用显式等待悬停账户设置
actions_address = ActionChains(wd)
actions_address.move_to_element(WebDriverWait(wd, 10).until(lambda x: x.find_element(By.XPATH, '//li[2]/div/div[1]'))).perform()
# 使用显式等待点击添加新地址
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.XPATH, '//li[2]/div/div[2]/a[2]')).click()

# 新增地址
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '.co_blue')).click()

# 输入收货人
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, 'input[name="consignee"]')).send_keys('张三')

# 输入手机号
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, 'input[name="mobile"]')).send_keys('13600000000')

# 输入省份
selector_address_province = Select(WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#province')))
selector_address_province.select_by_value('1')

sleep(1)
# 输入城市
selector_address_city = Select(WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#city')))
selector_address_city.select_by_value('2')
sleep(1)
# 输入区县
selector_address_district = Select(WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#district')))
selector_address_district.select_by_value('3')

sleep(1)
# 镇
selector_address_town = Select(WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#twon')))
selector_address_town.select_by_value('4')

# 详细地址
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, 'input[name="address"]')).send_keys('北京市海淀区')

# zipcode
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, 'input[name="zipcode"]')).send_keys('100000')

# 提交
WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, '#address_submit')).click()
wd.refresh()
# 留时间观察结果
sleep(3)