from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class LoginUtil:
    """
    登录工具类，提供后台管理系统和前台用户登录的可重用方法
    """
    
    @staticmethod
    def admin_login(driver=None, username='admin', password='HM_2025_test', verify_code='8888', maximize=True):
        """
        后台管理系统登录方法
        
        Args:
            driver: 可选的WebDriver实例，如果不提供则创建新的Edge实例
            username: 管理员用户名，默认为'admin'
            password: 管理员密码，默认为'HM_2025_test'
            verify_code: 验证码，默认为'8888'
            maximize: 是否最大化窗口，默认为True
            
        Returns:
            WebDriver: 登录后的WebDriver实例
        """
        # 如果没有提供driver，则创建新的Edge实例
        if driver is None:
            driver = webdriver.Edge()
            driver.get('https://hmshop-test.itheima.net/index.php/Admin/Admin/login')
        else:
            # 如果提供了driver，则导航到登录页面
            driver.get('https://hmshop-test.itheima.net/index.php/Admin/Admin/login')
        
        # 是否最大化窗口
        if maximize:
            driver.maximize_window()
            
        # 使用显式等待输入用户名
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, '.input-text[name="username"]')
        ).send_keys(username)
        
        # 输入密码
        driver.find_element(By.CSS_SELECTOR, '.input-text[name="password"]').send_keys(password)
        
        # 输入验证码
        driver.find_element(By.CSS_SELECTOR, '.input-text[id="vertify"]').send_keys(verify_code)
        
        # 点击登录按钮(使用xpath)
        driver.find_element(By.XPATH, '//input[@name="submit"]').click()
        
        # 等待登录成功后页面加载
        sleep(3)
        
        return driver
        
    @staticmethod
    def user_login(driver=None, username='13600000000', password='123456', verify_code='8888', maximize=True):
        """
        前台用户登录方法
        
        Args:
            driver: 可选的WebDriver实例，如果不提供则创建新的Edge实例
            username: 用户手机号，默认为'13600000000'
            password: 用户密码，默认为'123456'
            verify_code: 验证码，默认为'8888'
            maximize: 是否最大化窗口，默认为True
            
        Returns:
            WebDriver: 登录后的WebDriver实例
        """
        # 如果没有提供driver，则创建新的Edge实例
        if driver is None:
            driver = webdriver.Edge()
            driver.get('https://hmshop-test.itheima.net/index.php/Home/Index/index.html')
        else:
            # 如果提供了driver，则导航到首页
            driver.get('https://hmshop-test.itheima.net/index.php/Home/Index/index.html')
        
        # 是否最大化窗口
        if maximize:
            driver.maximize_window()
            
        # 使用显式等待点击登录按钮
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, '.nologin>a')
        ).click()
        
        # 使用显式等待输入用户名
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, '#username')
        ).send_keys(username)
        
        # 使用显式等待输入密码
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, '#password')
        ).send_keys(password)
        
        # 使用显式等待输入验证码
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, '#verify_code')
        ).send_keys(verify_code)
        
        # 使用显式等待点击登录按钮
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, 'a[name="sbtbutton"]')
        ).click()
        
        # 等待登录成功后页面加载
        sleep(2)
        
        return driver