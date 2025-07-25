from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from can_reuesu_code.login  import login_byhy

wd = webdriver.Edge()
login_byhy(wd, "http://127.0.0.1:8080")
wd.implicitly_wait(5)
mainWindow = wd.current_window_handle
element_footer=wd.find_element(By.XPATH,'//footer/div/a')
wd.execute_script("arguments[0].scrollIntoView({block:'center',inline:'center'})", element_footer)
sleep(1)
element_footer.click()
for handle in wd.window_handles:
    if handle != mainWindow:
        wd.switch_to.window(handle)
wd.implicitly_wait(5)
sleep(1)
wd.set_window_size(1920,1080)
sleep(1)
element_top_text = wd.find_element(By.XPATH,"//ul[@class='md-tabs__list']")
sleep(1)
print(element_top_text.text)
sleep(1)
wd.switch_to.window(mainWindow)
sleep(1)
wd.find_element(By.CSS_SELECTOR,'div.navbar-custom-menu > ul >li:nth-child(2)').click()
sleep(1)
wd.find_element(By.CSS_SELECTOR,'div.pull-right').click()
sleep(1)
wd.quit()