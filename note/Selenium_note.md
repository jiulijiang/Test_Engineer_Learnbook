# Selenium学习
## 选择元素基本方法
- 根据`id`选择元素
  - 根据规范，`id`不能重复，是唯一的，根据id选择元素是最快的
  - 语法:`element = wd.find_element(By.ID, 'id')
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    
    # 创建 WebDriver 对象
    wd = webdriver.Chrome()
    
    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    wd.get('https://www.byhy.net/cdn2/files/selenium/stock1.html')
    
    # 根据id选择元素，返回的就是该元素对应的WebElement对象
    element = wd.find_element(By.ID, 'kw')
    
    # 通过该 WebElement对象，就可以对页面元素进行操作了
    # 比如输入字符串到 这个 输入框里
    element.send_keys('通讯\n')
    
    input('按回车退出')
    ```
- 根据元素`class`选择元素
  - `class`可以一次性选择多个元素
    - 语法:`elements = wd.find_elements(By.CLASS_NAME, 'class')`
    - 如果找不到元素，`elements`变量的值为空列表
    - 可以利用空列表特性来判断元素是否存在
  - 想要只选择单个元素：
    - 语法:`element = wd.find_element(By.CLASS_NAME, 'class')`
    - 会获取匹配的第一个元素
- `find_element()`和`find_elements()`区别:
  - `find_element()`会返回第一个匹配的元素，如果没有会抛出异常
  - `find_elements()`会返回所有匹配的元素组成的列表，如果没有会返回空列表
  - `find_element()`更适合用来查找唯一元素，`find_elements()`更适合用来查找多个元素
- `text`属性：
  - 使用元素的`text`属性，可以获取元素的文本内容：
  - 语法:`element.text`
    - 例如：`print(element.text)`,这行代码就可以打印`element`元素的文本内容
- 根据`tag`名选元素
  - 和`class`属性一样，`tag`属性值可以有多个，多个用空格隔开
  - 语法:`elements = wd.find_elements(By.TAG_NAME, 'tag')`
- 通过`WebElement`对象选择元素
  - `WebDirver`对象选择的是整个页面，`WebElement`对象选择是某个元素内部，可以先通过id确定外层元素，在对内层元素进行操作
  ```python
  import time
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  
  # 创建 WebDriver 对象
  wd = webdriver.Edge()
  wd.get('https://www.bilibili.com/?spm_id_from=333.337.0.0')
  # 定位外层元素
  element = wd.find_element(By.ID, 'nav-searchform')
  # 定位内层元素
  input_element = element.find_element(By.TAG_NAME, 'input')
  input_element.send_keys('自动化测试\n')
  time.sleep(5)
  input('按回车退出')
  wd.quit()
  ```
  - 如上例子就是先定位bilibili首页的搜索框，再对搜索框进行输入操作
- 等待元素出现
  - `webdriver`对象提供了`implicitly_wait()`方法，设置隐式等待时间，当元素不存在时，会等待一段时间，如果元素存在，则立即返回
  - 语法:`wd.implicitly_wait(10)` 10秒内，如果元素不存在，则每隔0.5秒检查一次，如果元素存在，则立即返回
## 操作元素
- `click()`方法：点击元素，鼠标左键点击
- `send_keys()`方法：输入字符串到元素中
- `clear()`方法：清空元素中的内容
- `element.text`属性：获取元素的文本内容
- `get_attribute()`方法：获取元素的属性值
  - 语法:`element.get_attribute('属性名')`
  - 获取整个元素对应的HTML代码:`element.get_attribute('outerHTML')`
  - 获取元素内部的HTML代码:`element.get_attribute('innerHTML')`
  - 获取输入框内的文字:`element.get_attribute('value')`
  - 有时候元素的文本内容没有展示或者没有完全展示在页面中，这时候用`.text`可能会有问题
    - 解决方法：使用`get_attribute()`方法获取元素的属性值，属性值为`textContent`或`innerText`
## CSS selector 选择元素
- 选择单个元素语法:`element = wd.find_element(By.CSS_SELECTOR, 'CSS_selector参数')`
- 选择多个元素语法:`elements = wd.find_elements(By.CSS_SELECTOR, 'CSS_selector参数')`
- `CSS selector`同样可以根据tag名、id 属性和 class属性 来 选择元素：
  - 例如,选择所有tag名为div的元素:
    - `wd.find_elements(By.CSS_SELECTOR, 'div')`
    - 等价于`wd.find_elements(By.TAG_NAME, 'div')`
  - 根据`id`属性选择元素的语法是在`id`号前加一个`#`
    - 例如,选择id为kw的元素:`wd.find_element(By.CSS_SELECTOR, '#kw')`
    - 等价于`wd.find_element(By.ID, 'kw')`
- 根据`class`属性选择元素的语法是在`class`属性名前加一个`.`
  - 比如要选择所有`class`值为`people`的元素：
    - 可以是`wd.find_elements(By.CLASS_NAME, 'people')`
    - 也可以是`wd.find_elements(By.CSS_SELECTOR, '.people')`
      - `.people`就是代表所有class值为`people`的元素
- 选择**子元素**和**后代元素**
  - 子元素：`CSS selector`选择子元素语法是在选择元素的后面加上`>`
  - 后代元素：`CSS selector`选择后代元素语法是在选择元素的后面加上` `(一个或多个空格)
    - 也可以通过多个`>`，通过选择子元素的子元素来选择后代元素
    - ` `和`>`可以混用
- 根据属性选择元素
  - `CSS swlector`选择属性的语法是在属性名前加一个`[`，属性名后加一个`]`
  - 例如：选择所有`href`属性值为`https://www.byhy.net/` 的元素：
    - `wd.find_elements(By.CSS_SELECTOR, '[href="https://www.byhy.net/"]')`
  - 也可以只写一个`herf`属性，表示选择所有有`href`属性的元素：
    - `wd.find_elements(By.CSS_SELECTOR, '[href]')`
  - 属性选择可以和标签叠加，例如可以在`herf`前写一个`div`标签，表示选择所有标签名为`div`且带有`href`属性的元素：
    - `wd.find_elements(By.CSS_SELECTOR, 'div[href]')`
  - 属性包含选择,例如选择所有`href`属性值包含`byhy`的元素：
    - `wd.find_elements(By.CSS_SELECTOR, '[href*="byhy"]')`
    - `*`表示属性值包含`byhy`
    - `wd.find_elements(By.CSS_SELECTOR, '[href^="byhy"]')`
    - `^`表示属性值以`byhy`开头`
    - `wd.find_elements(By.CSS_SELECTOR, '[href$="byhy"]')`
    - `$`表示属性值以`byhy`结尾
  - 如果要包含多个属性限制，可以直接在后面加上新的属性限制：
    - `wd.find_elements(By.CSS_SELECTOR, 'div[href*="byhy"][class="people"]')`
    - 如上就表示选择标签名为`div`且`herf`属性值包含`byhy`，并且`class`属性值为`people`的元素
- 验证`CSS selector`
  - 想要验证表达式正不正确可以在页面开发者模式下按`ctrl`+`f`进入搜索界面，把表达式扔进去验证
  - 一般会出现`1 of n`，`n`表示有几个元素可以被当前表达式匹配到，前面的1表示当前匹配到第几个
- 选择语法联合使用
  - 即前面的选择语法可以叠加使用以便更精准的找到对应元素
    - 例如：`wd.find_elements(By.CSS_SELECTOR, 'div.people > span[href*="byhy"]')`
    - 如上例子意思是寻找`span`标签且属性`href`的值包括`byhy`,并且是`div`标签且`class`属性为`people`的子元素的元素
  - 组选择
    - 想要同时筛选多种条件的元素进入同一个列表，不同条件用`,`隔开
      - 例如:`wd.find_elements(By.CSS_SELECTOR, 'div.people, div.animal ')`
      - 表示寻找`div`标签且`class`属性为`people`或者`class`属性为`animal`的元素
      - 注意不存在如下写法:
        - `wd.find_elements(By.CSS_SELECTOR, 'div > .people, .animal')`
        - 该写法表示分别匹配 `div` 下的 `.people` 和任意位置的 `.animal`，而不是 `div` 下的 `.people` 或 `.animal`
        - 如下图：
        ```mermaid
        graph LR
          A[CSS selector] --> B[div]
          B --> C[class]
          C --> D[people]
          A --> F[class]
          F --> G[animal]
        ```
  - 按次序选择子节点
    - 想要选择的元素是**父元素的第n个子节点**时：
      - 使用`nth-child(n)`
      - 比如选择`span`标签的第3个子节点：
      - `wd.find_elements(By.CSS_SELECTOR, 'span:nth-child(3)')`
      - 如果不加限制，直接写`:nth-child(3)`，表示选择位置为第二个的所有元素
    - 想要选择的元素是**父元素的倒数第n个子节点**时：
      - 使用`nth-last-child(n)`
      - 比如选择`span`标签的第3个子节点：
      - `wd.find_elements(By.CSS_SELECTOR, 'span:nth-last-child(3)')`
    - 想要选择的元素是**选择父元素下第 n 个特定类型的子节点**时：
      - 使用`nth-of-type(n)`
      - 比如选择`span`标签的第3个子节点：
      - `wd.find_elements(By.CSS_SELECTOR, 'span:nth-of-type(3)')`
      - 注意与`nth-child(n)`的区别:
        - `span:nth-child(3)` :意思是选择`span`标签元素的第3个子节点
        - `span:nth-of-type(3)` :意思是选择`span`标签元素的第3个元素
    - 想要选择的元素是**选择父元素下第 n 个特定类型的倒数第 n 个子节点**时：
      - 使用`nth-last-of-type(n)`
    - 奇数节点和偶数节点
      - 如果要选择的是父元素的 偶数节点，使用 `nth-child(even)` 
        - `even`:表示偶数节点
      - 如果要选择的是父元素的 奇数节点，使用 `nth-child(odd)`
        - `odd`:表示奇数节点
- 兄弟节点选择
  - 相邻兄弟节点选择
    - 使用`+`可以选择指定元素身后第一个符合条件的兄弟元素
    - 例子:`h2 + p`:选择紧跟`h2`标签后面第一个`p`元素
    ```html
    <div class="container">
      <h2>标题</h2>
      <p>段落1（被选中）</p> <!-- 紧接在 h2 后 -->
      <p>段落2</p>
      <div>分隔块</div>
      <p>段落3</p>
    </div>
    ```
  - 通用兄弟节点选择
    - 使用`~`可以选择后续所有满足条件的兄弟节点
    - 例子:`h2 ~ p`:选择所有紧跟在`h2`标签后面的`p`元素
    ```html
    <div class="container">
      <h3>小标题</h3>
      <p>说明文字（被选中）</p>
      <div>信息块</div>
      <p>补充内容（被选中）</p>
      <p>备注（被选中）</p>
    </div>
    ```