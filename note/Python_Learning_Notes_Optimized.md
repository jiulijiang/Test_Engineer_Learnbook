# Python学习笔记（优化版）

## 目录
1. [Python基础知识](#python基础知识)
   - [变量与数据类型](#变量与数据类型)
   - [字符串操作](#字符串操作)
   - [数据输入](#数据输入)
2. [控制流](#控制流)
   - [判断语句](#判断语句)
   - [循环语句](#循环语句)
3. [函数](#函数)
   - [函数基础](#函数基础)
   - [函数进阶](#函数进阶)
   - [匿名函数](#匿名函数)
4. [数据容器](#数据容器)
   - [列表](#列表)
   - [元组](#元组)
   - [字符串](#字符串)
   - [集合](#集合)
   - [字典](#字典)
5. [文件操作](#文件操作)
   - [文件编码](#文件编码)
   - [文件读取](#文件读取)
   - [文件写入](#文件写入)
   - [追加写入](#追加写入)
6. [异常处理](#异常处理)
   - [异常基础](#异常基础)
   - [捕获异常](#捕获异常)
   - [抛出异常](#抛出异常)
7. [模块与包](#模块与包)
   - [模块基础](#模块基础)
   - [自定义模块](#自定义模块)
   - [Python包](#python包)
   - [第三方包](#第三方包)
8. [JSON数据格式](#json数据格式)
9. [数据可视化：pyecharts](#数据可视化pyecharts)
10. [面向对象编程](#面向对象编程)
    - [类与对象基础](#类与对象基础)
    - [常用内置方法](#常用内置方法)
    - [封装](#封装)
    - [继承](#继承)
    - [复写](#复写)
    - [类型注解](#类型注解)
    - [多态](#多态)
    - [抽象类](#抽象类)
11. [Python高阶技巧](#python高阶技巧)
    - [闭包](#闭包)
    - [装饰器](#装饰器)
    - [设计模式](#设计模式)
    - [多线程编程](#多线程编程)
    - [Socket网络编程](#socket网络编程)
    - [正则表达式](#正则表达式)
    - [递归](#递归)

---

## Python基础知识

### 变量与数据类型
- **变量定义**：变量是用来存储数据的容器
- **数据类型**：
  - 数值型：整数(int)、浮点数(float)、复数(complex)
  - 布尔型：True、False
  - 字符串型：str
  - 列表：list
  - 元组：tuple
  - 集合：set
  - 字典：dict
- **数据类型转换**：
  - `int()`：转换为整数
  - `float()`：转换为浮点数
  - `str()`：转换为字符串
  - `bool()`：转换为布尔值
- **标识符**：变量名、函数名等的命名规则
  - 只能包含字母、数字、下划线
  - 不能以数字开头
  - 不能使用Python关键字
  - 区分大小写

### 字符串操作
- **字符串定义**：使用单引号、双引号或三引号
- **字符串格式化**：
  - `%` 格式化：`print("我的名字是%s，年龄是%d" % (name, age))`
  - `format()` 方法：`print("我的名字是{}，年龄是{}".format(name, age))`
  - f-string：`print(f"我的名字是{name}，年龄是{age}")`
- **字符串常见操作**：
  - 索引：`str[index]`
  - 切片：`str[start:end:step]`
  - 长度：`len(str)`
  - 查找：`str.find(sub)`
  - 替换：`str.replace(old, new)`
  - 分割：`str.split(sep)`
  - 连接：`str.join(iterable)`

### 数据输入
- **input()函数**：用于接收用户输入
  - `input("提示信息")`：返回用户输入的字符串
  - 如需数值类型，需进行类型转换：`int(input("请输入一个数字："))`

## 控制流

### 判断语句
- **布尔类型**：用于表示真(True)或假(False)
- **if语句**：
  ```python
  if 条件1:
      # 条件1为真时执行的代码
  elif 条件2:
      # 条件1为假，条件2为真时执行的代码
  else:
      # 所有条件都为假时执行的代码
  ```
- **嵌套判断**：if语句内部可以再包含if语句

### 循环语句
- **while循环**：
  ```python
  while 条件:
      # 条件为真时重复执行的代码
  ```
- **for循环**：
  ```python
  for 变量 in 可迭代对象:
      # 对可迭代对象中的每个元素执行的代码
  ```
- **range()函数**：生成一个整数序列
  - `range(start, end, step)`
- **嵌套循环**：循环内部可以再包含循环
- **变量作用域**：局部变量和全局变量
- **continue语句**：跳过当前循环的剩余部分，继续下一次循环
- **break语句**：跳出当前循环

## 函数

### 函数基础
- **函数定义**：
  ```python
  def 函数名(参数列表):
      # 函数体
      return 返回值
  ```
- **函数调用**：`函数名(参数列表)`
- **参数传递**：位置参数、关键字参数
- **返回值**：使用`return`语句返回结果，可以返回多个值（作为元组）
- **说明文档**：使用三引号在函数开头添加说明文档
  ```python
  def 函数名(参数列表):
      """函数说明文档"""
      # 函数体
  ```
- **嵌套调用**：函数内部可以调用其他函数
- **作用域**：局部作用域和全局作用域
  - `global`关键字：在函数内部修改全局变量

### 函数进阶
- **多返回值**：函数可以返回多个值，以元组形式返回
- **位置参数**：按照参数定义的顺序传递参数
- **关键字参数**：通过参数名指定参数值
- **缺省参数**：在函数定义时给参数指定默认值
- **不定长参数**：
  - `*args`：接收任意数量的位置参数，以元组形式存储
  - `**kwargs`：接收任意数量的关键字参数，以字典形式存储

### 匿名函数
- **lambda函数**：用于创建小型匿名函数
  - 语法：`lambda 参数列表: 表达式`
  - 示例：`lambda x, y: x + y`
- **函数作为参数传递**：函数可以作为参数传递给其他函数

## 数据容器

### 列表
- **列表定义**：`list1 = [元素1, 元素2, ...]`
- **列表操作**：
  - 索引：`list1[index]`
  - 切片：`list1[start:end:step]`
  - 添加：`list1.append(元素)`、`list1.insert(位置, 元素)`
  - 删除：`list1.remove(元素)`、`list1.pop(位置)`
  - 修改：`list1[位置] = 新值`
  - 长度：`len(list1)`
  - 查找：`元素 in list1`、`list1.index(元素)`
  - 计数：`list1.count(元素)`
  - 排序：`list1.sort()`、`list1.sort(reverse=True)`
- **列表遍历**：
  ```python
  # 方法1：直接遍历元素
  for item in list1:
      print(item)
  
  # 方法2：通过索引遍历
  for i in range(len(list1)):
      print(list1[i])
  
  # 方法3：同时获取索引和元素
  for i, item in enumerate(list1):
      print(i, item)
  ```

### 元组
- **元组定义**：`tuple1 = (元素1, 元素2, ...)`
- **特点**：不可修改的序列
- **元组操作**：索引、切片、长度、查找、计数（与列表类似）
- **元组遍历**：与列表相同

### 字符串
- **字符串定义**：`str1 = "字符串内容"`
- **特点**：不可修改的字符序列
- **字符串操作**：索引、切片、长度、查找、替换、分割、连接（与列表类似）
- **字符串遍历**：与列表相同

### 集合
- **集合定义**：`set1 = {元素1, 元素2, ...}` 或 `set1 = set(可迭代对象)`
- **特点**：无序、不重复的元素集合
- **集合操作**：
  - 添加：`set1.add(元素)`、`set1.update(可迭代对象)`
  - 删除：`set1.remove(元素)`、`set1.discard(元素)`
  - 交集：`set1 & set2` 或 `set1.intersection(set2)`
  - 并集：`set1 | set2` 或 `set1.union(set2)`
  - 差集：`set1 - set2` 或 `set1.difference(set2)`
  - 对称差集：`set1 ^ set2` 或 `set1.symmetric_difference(set2)`
- **集合遍历**：与列表相同

### 字典
- **字典定义**：`dict1 = {键1: 值1, 键2: 值2, ...}` 或 `dict1 = dict(可迭代对象)`
- **特点**：键值对的无序集合，键必须唯一
- **字典操作**：
  - 访问：`dict1[键]` 或 `dict1.get(键, 默认值)`
  - 添加/修改：`dict1[键] = 值`
  - 删除：`del dict1[键]`、`dict1.pop(键)`
  - 键列表：`dict1.keys()`
  - 值列表：`dict1.values()`
  - 键值对列表：`dict1.items()`
  - 长度：`len(dict1)`
  - 检查键是否存在：`键 in dict1`
- **字典遍历**：
  ```python
  # 方法1：遍历键
  for key in dict1:
      print(key, dict1[key])
  
  # 方法2：遍历键值对
  for key, value in dict1.items():
      print(key, value)
  
  # 方法3：遍历值
  for value in dict1.values():
      print(value)
  ```

## 文件操作

### 文件编码
- **编码技术**：翻译的规则，记录了如何将内容翻译成二进制，以及如何将二进制翻译成内容
- **常见编码**：UTF-8、GBK、GB2312等
- **UTF-8编码**：目前全球通用的编码，除非有特殊需求，一般都使用UTF-8编码

### 文件读取
- **文件类型**：文本、视频、音频、图片、可执行文件等
- **打开文件**：
  ```python
  文件对象 = open("file_name", "mode", "encoding")
  ```
  - file_name：文件名(可以包含路径)
  - mode：文件打开方式: r(只读)、w(只写)、a(追加)
  - encoding：文件编码
- **读取方法**：
  - `文件对象.read(num)`：读取指定字节数，不传参则读取所有内容
  - `文件对象.readlines()`：读取文件内容，返回列表，每一行作为一个元素
  - `文件对象.readline()`：读取一行内容
  - `for line in 文件对象`：循环读取每一行内容
- **关闭文件**：`文件对象.close()`，不关闭文件会导致文件被持续占用
- **with语句**：自动关闭文件对象
  ```python
  with open("文件名", "模式", "encoding") as 文件对象:
      # 文件操作
  ```

### 文件写入
- **写入文件**：`文件对象.write(内容)`
- **创建文件**：如果文件不存在，则创建文件
- **覆盖内容**：w模式下会覆盖文件原本内容
- **刷新缓冲区**：`文件对象.flush()`，将内容真正写入文件
- **注意**：`.close()`方法包含`flush()`功能

### 追加写入
- **追加模式**：`open("文件名", "a", "encoding")`
- **追加内容**：不会覆盖文件原本内容，会在文件末尾追加内容

## 异常处理

### 异常基础
- **异常**：当检测到一个错误时，Python解释器无法继续执行，出现错误提示
- **捕获异常**：提前预设某处存在异常，做好准备，当异常出现时，进行相应的处理

### 捕获异常
- **捕获常规异常**：
  ```python
  try:
      可能发生异常的代码
  except:
      处理异常的代码
  ```
- **捕获指定异常**：
  ```python
  try:
      可能发生异常的代码
  except 异常类型 as 异常变量名:
      处理异常的代码
  ```
- **捕获多个异常**：
  ```python
  try:
      可能发生异常的代码
  except (异常类型1, 异常类型2) as 异常变量名:
      处理异常的代码
  ```
- **捕获所有异常**：
  ```python
  try:
      可能发生异常的代码
  except Exception as 异常变量名:
      处理异常的代码
  ```
- **else模块**：没有出现异常时执行的代码
  ```python
  try:
      可能发生异常的代码
  except:
      处理异常的代码
  else:
      无异常时执行的代码
  ```
- **finally模块**：无论是否发生异常，都会执行的代码
  ```python
  try:
      可能发生异常的代码
  except:
      处理异常的代码
  finally:
      无论如何都会执行的代码
  ```
- **异常的传递性**：异常在调用中会传递，可以在调用链的任意位置捕获异常

### 抛出异常
- **抛出异常**：`raise 异常类型(异常信息)`
- **作用**：抛出异常后，程序会立即停止运行，并将异常信息打印出来
- **使用场景**：可以在`except`块、`else`块或`finally`块中抛出异常

## 模块与包

### 模块基础
- **模块**：一个模块就是一个py文件，模块名就是文件名，包含类、函数、变量等
- **导入模块**：
  ```python
  # 导入整个模块
  import 模块名
  
  # 导入模块中的特定内容
  from 模块名 import 类名/函数名/变量名
  
  # 导入模块中的所有内容
  from 模块名 import *
  
  # 导入并指定别名
  import 模块名 as 别名
  from 模块名 import 类名/函数名/变量名 as 别名
  ```
- **使用模块**：`模块名.模块内容` 或直接使用导入的内容

### 自定义模块
- **`__name__`变量**：当模块被直接运行时，`__name__`变量的值为`__main__`；当模块被导入时，`__name__`变量的值为模块名
  ```python
  if __name__ == '__main__':
      # 模块的测试代码
      pass
  ```
- **`__all__`变量**：用于定义模块中可以被导入的内容
  ```python
  __all__ = ['func1', 'func2']
  ```
  使用`from 模块名 import *`时，只会导入`__all__`中列出的内容

### Python包
- **包的定义**：包是一个包含多个模块的文件夹，必须包含一个`__init__.py`文件
- **`__init__.py`文件**：包的初始化文件，导入包时会被执行
- **包的导入**：
  ```python
  # 导入包中的模块
  import 包名.模块名
  from 包名 import 模块名
  
  # 导入包中的模块内容
  from 包名.模块名 import 类名/函数名/变量名
  ```
- **包的层级**：支持多层包结构，如`import 包1.包2.模块名`

### 第三方包
- **pip工具**：用于安装和管理第三方包
- **安装包**：`pip install 包名`
- **卸载包**：`pip uninstall 包名`
- **查看已安装的包**：`pip list`
- **更新包**：`pip install --upgrade 包名`
- **国内镜像**：可以通过配置国内镜像加速下载
  ```python
  pip install -i https://mirrors.aliyun.com/pypi/simple/ 包名
  ```

## JSON数据格式

- **JSON定义**：JavaScript Object Notation，一种轻量级的数据交换格式
- **主要功能**：在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互
- **JSON基本格式**：
  ```json
  {
      "name": "张三",
      "age": 18,
      "is_student": true,
      "courses": ["数学", "英语", "物理"],
      "address": {
          "city": "北京",
          "zip_code": "100000"
      }
  }
  ```
- **Python与JSON转换**：
  - Python对象转JSON字符串：`json.dumps(data)`，有中文时设置`ensure_ascii=False`
  - JSON字符串转Python对象：`json.loads(data)`

## 数据可视化：pyecharts

- **pyecharts**：一个用于生成图表的Python库，支持多种图表类型
- **安装**：`pip install pyecharts`
- **构建基础折线图**：
  ```python
  # 导包
  from pyecharts.charts import Line
  # 创建Line对象
  line = Line()
  # 添加x轴数据
  line.add_xaxis(["1月", "2月", "3月", "4月", "5月"])
  # 添加y轴数据
  line.add_yaxis("销售额", [120, 200, 150, 80, 70])
  # 生成图表
  line.render("line_chart.html")
  ```
- **全局配置项**：使用`set_global_opts`方法设置
  ```python
  line.set_global_opts(
      title="销售数据",  # 图表标题
      xaxis_title="月份",  # x轴标题
      yaxis_title="销售额",  # y轴标题
      toolbox_opts={  # 工具栏
          "show": True,
          "feature": {
              "saveAsImage": {}
          }
      }
  )
  ```

## 面向对象编程

### 类与对象基础
- **对象**：对现实世界中事物的抽象，具有属性和方法
- **类的定义**：类是对象的蓝图，通过类可以创建多个对象
  ```python
  class ClassName:
      # 类的属性
      name = ""
      
      # 类的方法
      def run(self):
          print("对象正在运行")
  ```
- **实例化**：通过类创建对象的过程
  ```python
  obj = ClassName()
  ```
- **构造方法**：`__init__`方法，用于初始化对象属性
  ```python
  class Clock:
      def __init__(self, id=None, price=None):
          self.id = id  # 对象属性
          self.price = price  # 对象属性
  
      def ring(self):
          print("叮铃铃...")
  
  # 实例化并初始化
  clock1 = Clock(id=1, price=100)
  ```

### 常用内置方法
- **`__str__`方法**：返回对象的字符串表示，用于打印对象
  ```python
  class Student:
      def __init__(self, name, age):
          self.name = name
          self.age = age
          
      def __str__(self):
          return f"姓名：{self.name}，年龄：{self.age}"
  
  stu1 = Student("张三", 18)
  print(stu1)  # 输出：姓名：张三，年龄：18
  ```
- **`__lt__`方法**：用于比较两个对象的大小（小于、大于）
  ```python
  def __lt__(self, other):
      return self.age < other.age
  ```
- **`__le__`方法**：用于比较两个对象的大小（小于等于、大于等于）
  ```python
  def __le__(self, other):
      return self.age <= other.age
  ```
- **`__eq__`方法**：用于比较两个对象是否相等
  ```python
  def __eq__(self, other):
      return self.age == other.age
  ```

### 封装
- **封装**：把数据（属性）和操作（方法）封装在一起，隐藏内部实现细节，只提供对外的接口
- **私有成员**：以双下划线开头的属性和方法，外部无法直接访问
  ```python
  class Phone:
      __current_voltage = None  # 私有属性
      
      def __keep_single_core(self):  # 私有方法
          print("保持单核运行")
      
      def call_by_5g(self):
          if self.__current_voltage >= 5:
              print("5G通话")
          else:
              self.__keep_single_core()  # 内部可以访问私有方法
              print("电量不充足，使用单核运行")
  ```

### 继承
- **继承**：类与类之间的关系，子类继承了父类的属性和方法，并可以添加新的属性和方法
- **单继承**：
  ```python
  class 子类名(父类名):
      # 类内容体
  ```
- **多继承**：
  ```python
  class 子类名(父类1, 父类2, ...):
      # 类内容体
  ```
- **pass关键字**：当类没有任何内容或不想补充新内容时使用
  ```python
  class 子类名(父类1, 父类2, ...):
      pass
  ```
- **多继承属性查找**：当不同父类有同名属性时，按照从左到右的顺序查找

### 复写
- **复写**：子类重新定义父类的方法，修改或扩展父类的功能
- **复写方法**：直接在子类中定义与父类同名的属性或方法
- **调用父类成员**：
  - `父类名.成员变量/成员方法(self)`
  - `super().成员变量/成员方法名()`

### 类型注解
- **类型注解**：方便静态类型检查工具和IDE提供数据类型提示
- **基础语法**：`变量名: 数据类型 = 值`
  ```python
  age: int = 18
  name: str = "张三"
  is_student: bool = True
  ```
- **容器类型注解**：`变量名: 容器类型[元素类型] = 值`
  ```python
  from typing import List, Dict, Tuple
  
  numbers: List[int] = [1, 2, 3]
  person: Dict[str, any] = {"name": "张三", "age": 18}
  coordinates: Tuple[float, float] = (1.0, 2.0)
  ```
- **注释中的类型注解**：`变量名 = 值  # type: 数据类型`
- **函数类型注解**：
  ```python
  def add(a: int, b: int) -> int:
      return a + b
  ```
- **Union类型注解**：表示一个变量可以是多个类型中的一个
  ```python
  from typing import Union
  
  my_list: List[Union[int, str]] = [1, "hello"]
  ```

### 多态
- **多态**：完成某个行为时，使用不同的对象会得到不同的状态
- **实例展示**：
  ```python
  class Animal:
      def make_sound(self):
          pass
          
  class Dog(Animal):
      def make_sound(self):
          print("汪汪汪")
          
  class Cat(Animal):
      def make_sound(self):
          print("喵喵喵")
          
  def animal_sound(animal: Animal):
      animal.make_sound()
      
  dog = Dog()
  cat = Cat()
  animal_sound(dog)  # 输出：汪汪汪
  animal_sound(cat)  # 输出：喵喵喵
  ```
- **多态的本质**：以父类做定义声明，以子类做具体实现，获得统一行为，不同状态

### 抽象类
- **抽象类**：含有抽象方法的类
- **抽象方法**：方法体是空实现(`pass`)的方法
- **使用场景**：定义一组接口，子类必须实现这些接口，保证子类具有统一的行为
- **示例**：
  ```python
  class Animal:
      def make_sound(self):
          pass  # 抽象方法
  
  class Dog(Animal):
      def make_sound(self):
          print("汪汪汪")  # 具体实现
  ```

## Python高阶技巧

### 闭包
- **闭包定义**：在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数
- **简单闭包示例**：
  ```python
  def outer_func(a):
      def inner_func(b):
          return a + b
      return inner_func
  
  closure = outer_func(10)
  print(closure(5))  # 输出：15
  ```
- **nonlocal关键字**：用于声明一个变量为非局部变量，在嵌套函数中修改非局部变量
- **ATM程序示例**：
  ```python
  def fun_ATM_outer():
      money = 100000
      
      def atm_menu():
          while True:
              print("-----------主菜单-----------")
              print("用户你好，欢迎来到ATM机，请输入操作")
              print("1.查询余额")
              print("2.取款")
              print("3.存款")
              print("4.退出")
              print("请输入你的选择：")
              choice = int(input())
              if choice == 1:
                  atm_enquiry()
              elif choice == 2:
                  atm_out()
              elif choice == 3:
                  atm_in()
              elif choice == 4:
                  print("感谢使用ATM机，再见")
                  break
              else:
                  print("请输入正确的选择!")
      
      def atm_enquiry():
          print(f"您的余额是{money}")
      
      def atm_in():
          nonlocal money
          money += int(input("请输入存款金额："))
          print(f"存款成功！您的余额为{money}")
      
      def atm_out():
          nonlocal money
          out_money = int(input("请输入取款金额："))
          if out_money > money:
              print("取款失败！您的余额不足")
          else:
              money -= out_money
              print(f"取款成功！您的余额为{money}")
      
      return atm_menu
  ```
- **闭包的优缺点**：
  - 优点：无需定义全局变量即可实现通过函数持续访问、修改某个变量的值；变量位于外部函数内，难以被错误调用修改
  - 缺点：内部函数持续引用外部函数的值，可能导致这部分内存不被释放

### 装饰器
- **装饰器定义**：一种闭包，在不破坏目标函数原有代码和功能的前提下，给目标函数添加新的功能
- **装饰器一般写法**：
  ```python
  def outer(func):
      def inner():
          print("这是装饰器")
          func()
          print("这是装饰器")
      return inner
  
  def sleep():
      print("睡觉")
  
  func = outer(sleep)
  func()  # 输出：这是装饰器 
  # 睡觉 
  # 这是装饰器
  ```
- **装饰器语法糖**：
  ```python
  def outer(func):
      def inner():
          print("这是装饰器")
          func()
          print("这是装饰器")
      return inner
  
  @outer  # 语法糖，相当于 sleep = outer(sleep)
  def sleep():
      print("睡觉")
  
  sleep()  # 输出：这是装饰器 
  # 睡觉 
  # 这是装饰器
  ```

### 设计模式
- **设计模式**：解决特定问题的通用解决方案，提供可重用的代码结构和方法
- **常见设计模式**：单例模式、工厂模式、观察者模式、策略模式等
- **单例模式**：
  - **定义**：保证一个类只有一个实例，并提供一个全局访问点
  - **适用场景**：配置管理器、日志记录器等需要唯一实例的场景
  - **优点**：确保全局只有一个实例，节省资源；提供全局访问点，方便管理和使用
- **工厂模式**：
  - **定义**：提供一个创建对象的接口，但不暴露对象创建的具体实现
  - **适用场景**：需要创建的对象类型较多，或需要根据不同条件创建不同类型的对象
  - **示例**：
    ```python
    class Person:
        pass
        
    class Student(Person):
        pass
        
    class Teacher(Person):
        pass
        
    class Worker(Person):
        pass
        
    class Factory:
        def get_person(self, type):
            if type == 's':
                return Student()
            elif type == 't':
                return Teacher()
            else:
                return Worker()
    
    factory = Factory()
    stu = factory.get_person('s')  # 创建学生对象
    tea = factory.get_person('t')  # 创建教师对象
    wor = factory.get_person('w')  # 创建工人对象
    ```
  - **优点**：大批量创建对象时有统一入口，易于维护；发生修改时只需修改工厂类

### 多线程编程
- **进程**：运行在系统上的程序，分配进程id方便系统管理
- **线程**：归属于进程的最小工作单位，一个进程可以开启多个线程
- **并行执行**：同一时间做不同的工作，进程之间是并行的，线程也可以并行执行
- **threading模块**：Python提供的支持多线程编程的模块
  ```python
  import threading
  
  # 创建线程
  thread = threading.Thread(target=函数名, args=(参数1, 参数2, ...))
  
  # 启动线程
  thread.start()
  ```

### Socket网络编程
- **Socket通信**：用于不同设备之间的网络通信
- **服务端编程步骤**：
  1. **创建Socket对象**：`socket_server = socket.socket()`
  2. **绑定IP地址和端口号**：`socket_server.bind(host, port)`
  3. **监听连接请求**：`socket_server.listen(backlog)`
  4. **接收客户端连接**：`conn, addr = socket_server.accept()`
  5. **接收数据**：`data = conn.recv(bufsize).decode("utf-8")`
  6. **发送数据**：`conn.send(msg.encode("utf-8"))`
  7. **关闭连接**：`conn.close(); socket_server.close()`
- **客户端编程步骤**：
  1. **创建Socket对象**：`socket_client = socket.socket()`
  2. **连接服务端**：`socket_client.connect((host, port))`
  3. **发送数据**：`socket_client.send(msg.encode("utf-8"))`
  4. **接收数据**：`data = socket_client.recv(bufsize).decode("utf-8")`
  5. **关闭连接**：`socket_client.close()`

### 正则表达式
- **正则表达式**：使用单个字符串来描述匹配某个句法规则的字符串
- **re模块**：Python中用于正则表达式操作的模块
- **常用方法**：
  - `re.match(pattern, string)`：从字符串开头匹配，返回匹配对象或None
  - `re.search(pattern, string)`：搜索整个字符串，返回第一个匹配或None
  - `re.findall(pattern, string)`：匹配整个字符串，返回所有匹配的列表
- **元字符**：
  - **单字符匹配**：
    - `.`：匹配任意字符（除换行符）
    - `[]`：匹配括号内的任意字符
    - `[^]`：匹配除括号内字符外的任意字符
    - `\d`：匹配数字（等价于[0-9]）
    - `\D`：匹配非数字
    - `\s`：匹配空白字符
    - `\S`：匹配非空白字符
    - `\w`：匹配单词字符（[a-zA-Z0-9_]）
    - `\W`：匹配非单词字符
  - **数量匹配**：
    - `*`：匹配0个或多个
    - `+`：匹配1个或多个
    - `?`：匹配0个或1个
    - `{n}`：匹配n个
    - `{n,}`：匹配n个或多个
    - `{n,m}`：匹配n到m个
  - **边界匹配**：
    - `^`：匹配字符串开头
    - `$`：匹配字符串结尾
    - `\b`：匹配单词边界
    - `\B`：匹配非单词边界
  - **分组匹配**：
    - `()`：分组匹配
    - `|`：或操作符

### 递归
- **递归定义**：函数直接调用自身的特殊编程写法
  ```python
  def fun():
      if ...:  # 终止条件
          fun()  # 递归调用
      return ...
  ```
- **使用场景**：解决一些复杂问题，如寻找文件、树形结构遍历、汉诺塔问题、斐波那契数列等
- **注意事项**：
  - 必须有明确的终止条件，否则容易变成无限递归
  - 确保返回值的传递，确保从最内层返回到最外层

---

**完结撒花**！基础Python学习到此结束。