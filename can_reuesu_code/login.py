from selenium import webdriver
from selenium.webdriver.common.by import By


def login_byhy(wd:webdriver,url: str):
    wd.implicitly_wait(10)
    wd.get(url)
    element_login_username = wd.find_element(By.CSS_SELECTOR,'#username')
    element_login_username.send_keys('byhy')
    element_login_password = wd.find_element(By.CSS_SELECTOR,'#password')
    element_login_password.send_keys('88888888\n')

if __name__ == '__main__':
    wd = webdriver.Edge()
    login_byhy(wd)
    wd.quit()