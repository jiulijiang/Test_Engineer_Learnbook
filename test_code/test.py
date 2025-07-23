from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象
wd = webdriver.Edge()
wd.implicitly_wait(10)
wd.get('https://www.byhy.net/cdn2/files/selenium/shuihu.html')
element = wd.find_element(By.CSS_SELECTOR,'#container > #layer1')
text = element.find_elements(By.CSS_SELECTOR,'div.item')
for i in text:
    print(i.text)
input('按回车退出')
wd.quit()