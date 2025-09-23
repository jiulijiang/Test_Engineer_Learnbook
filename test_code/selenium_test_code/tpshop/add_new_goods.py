from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support.select import Select

wd = webdriver.Edge()

wd.get('https://hmshop-test.itheima.net/index.php/Admin/Admin/login')

# 使用显式等待输入用户名
WebDriverWait(wd,10).until(lambda x:x.find_element(By.CSS_SELECTOR,'.input-text[name="username"]')).send_keys('admin')
wd.maximize_window()
# 输入密码
wd.find_element(By.CSS_SELECTOR,'.input-text[name="password"]').send_keys('HM_2025_test')

# 输入验证码
wd.find_element(By.CSS_SELECTOR,'.input-text[id="vertify"]').send_keys('8888')

# 点击登录按钮(使用xpath)
wd.find_element(By.XPATH,'//input[@name="submit"]').click()

sleep(3)

# 点击商城
WebDriverWait(wd,10).until(lambda x:x.find_element(By.CSS_SELECTOR,'[data-param="goods"]')).click()

# 切换到frame
wd.switch_to.frame('workspace')
# 点击添加商品
WebDriverWait(wd,10).until(lambda x:x.find_element(By.XPATH,'//div[2]/a/div')).click()

# 输入商品名称
WebDriverWait(wd,10).until(lambda x:x.find_element(By.CSS_SELECTOR,'[name="goods_name"]')).send_keys('测试商品')

# 商品分类选择
selector_goods = Select(wd.find_element(By.CSS_SELECTOR,'#cat_id'))
selector_goods.select_by_value('31')

sleep(1) # 等待一级分类加载完成,过快会导致二级分类未加载完成
selector_goods_2 = Select(WebDriverWait(wd,10).until(lambda x:x.find_element(By.CSS_SELECTOR,'#cat_id_2')))
selector_goods_2.select_by_value('36')
sleep(1) # 等待二级分类加载完成,过快会导致三级分类未加载完成
selector_goods_3 = Select(WebDriverWait(wd,10).until(lambda x:x.find_element(By.CSS_SELECTOR,'#cat_id_3')))
selector_goods_3.select_by_value('89')


# 商品简介
wd.find_element(By.CSS_SELECTOR,'[name="goods_remark"]').send_keys('这是一个测试商品')


#商品品牌
selector_goods_brand = Select(wd.find_element(By.CSS_SELECTOR,'#brand_id'))
selector_goods_brand.select_by_value('2')

# 商品供应商
selector_goods_supplier = Select(wd.find_element(By.CSS_SELECTOR,'#suppliers_id'))
selector_goods_supplier.select_by_value('2')

# 售价
wd.find_element(By.CSS_SELECTOR,'[name="shop_price"]').send_keys('100')

# 市场价
wd.find_element(By.CSS_SELECTOR,'[name="market_price"]').send_keys('120')

# 成本价
wd.find_element(By.CSS_SELECTOR,'[name="cost_price"]').send_keys('80')

# 佣金
wd.find_element(By.CSS_SELECTOR,'[name="commission"]').send_keys('5')

#商品标签
selector_goods_tag = Select(wd.find_element(By.CSS_SELECTOR,'[name="label_id"]'))
selector_goods_tag.select_by_value('2')

# 重量
wd.find_element(By.CSS_SELECTOR,'[name="weight"]').send_keys('5')

#体积
wd.find_element(By.CSS_SELECTOR,'[name="volume"]').send_keys('1')

# 包邮
wd.find_element(By.CSS_SELECTOR,'#is_free_shipping_label_1').click()

# 库存
wd.find_element(By.CSS_SELECTOR,'[name="store_count"]').send_keys('100')

# 商品关键词
wd.find_element(By.CSS_SELECTOR,'[name="keywords"]').send_keys('测试商品')

# 虚拟销售量
wd.find_element(By.CSS_SELECTOR,'[name="virtual_sales_sum"]').send_keys('888800')

# 虚拟收藏量
wd.find_element(By.CSS_SELECTOR,'[name="virtual_collect_sum"]').send_keys('888800')

# 手动检查遗漏
sleep(3)
# 提交
wd.find_element(By.CSS_SELECTOR,'#submit').click()



wd.quit()
