# CI 持续集成笔记

## 持续集成目的

**快速迭代 保持高质量**

- 持续集成（Continuous integration）
    - 开发人员提交新代码后，立刻构建，部署到「测试环境」，执行测试并反馈
- 持续交付（Continuous delivery）
    - 在持续集成的基础上，将集成后的代码部署到「类生产环境」    
- 持续部署（continuous deployment）
    - 在持续交付的基础上，自动部署到生产环境
 

## 如何更好的契合CI流程 — 持续测试
**需解决的问题：**
1. 自动化测试case执行不靠人工
    - 代码更新自动触发case执行
    - 每日定时自动触发case执行
2. 第一时间发布自动化测试结果
    - 目的：通过持续测试验证代码质量是否符合交付标准


## git 工作流程

常见的代码托管平台：
- Github
    - 国外的基于git实现在线代码托管的仓库（企业版收费）
    - 官网：https://github.com/
- Gitee
    - 码云，是开源中国免费提供（企业版收费）
    - 官网：https://gitee.com/
- Gitlab
    - 类似Github，一般用于企业内部搭建git私服

### Git安装
Git：支持 Linux/Unix、Solaris、Mac和 Windows 平台
安装Git：
- 下载地址：https://git-scm.com/downloads
- 校验是否安装成功： git --version
配置Git：
- 安装完成后，需要在命令行配置用户名和邮箱
    - git config --global user.name "your_name"
    - git config --global user.email "your_email@example.com"

### Git常见操作
1. 克隆 Git 资源作为本地资源
    - git clone <git仓库地址>
2. 如果其他人修改了 Git 资源，需要更新本地资源
    - git pull
3. 提交本地文件前对比Git资源上的文件，解决冲突
    - git diff
4. 提交本地修改到Git仓库
    - git add <file>
    - git commit -m "说明信息"  
    - git push
    - 注意：如果本地分支与远程分支不同名，需要指定远程分支
        - git push <remote> <local-branch>:<remote-branch>




## Jenkins

### Jenkins介绍
- 基于Java开发的一种开源、跨平台的持续集成工具
- 官网：https://www.jenkins.io/

- 作用：
    - 持续自动构建/测试软件项目
    - 监控定时执行的任务
### Jenkins环境搭建
- 安装步骤：
1. 安装JDK
    - 下载地址：https://www.oracle.com/java/technologies/javase-downloads.html
    - 校验是否安装成功： java -version

2. 安装Jenkins
    - 下载地址：https://www.jenkins.io/download/
    - 校验是否安装成功： java -jar jenkins.war --version

### 安装HTML Publisher插件— 显示测试报告

安装步骤：
1. 进入首页，选择'Jenkins'后面的小图标->'系统管理'->'管理插件'
2. 输入搜索关键字，选择要安装的插件，点击‘Install without restart’安装
3. 查看安装进度

### 解决HTML报告样式无法显示问题

为了测试报告样式的美观以及易读，测试报告中会搭配CSS和JS实现自定义的样式或动画效果。

- 问题：
Jenkins中在访问有自定义样式或动画效果的测试报告时，会出现样式无法正常显示的问题。
- 原因：
Jenkins为了避免受到恶意HTML/JS文件的攻击，会默认将安全策略CSP设置为：
`sandbox; default-src 'none'; img-src 'self'; style-src 'self'`
在此配置下，只允许加载：
- Jenkins服务器上托管的CSS文件
- Jenkins服务器上托管的图片文件
- 其他形式的内容都会被禁止：JavaScript、plugins (object/embed)、HTML中的内联样式表和引用的外站CSS文件、
HTML中的内联图片和外站引用的图片文件等等

- 解决方法：
通过修改启动命令来实现：
D:\jenkins>java -Dhudson.model.DirectoryBrowserSupport.CSP= -jar jenkins.war

### 系统设置——邮件配置
公司中发送测试报告邮件时，需要设置一些规范。
例如配置收件人列表（项目经理，测试相关人员，开发相关人员，产品经理等）、项目基本信息等。
Jenkins提供了邮箱报告模板，可以通过配置模块，指定一些邮件固定的信息

- 邮件测试报告模板
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>${ENV, var="JOB_NAME"}-第${BUILD_NUMBER}次构建日志</title>
</head>
<body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4" offset="0">
<div>
<h2>项目信息</h2>
<ul>
<li>项目名称：${PROJECT_NAME}</li>
<li>详细测试报告：<a href="${PROJECT_URL}HTML_20Report/">${PROJECT_URL}HTML_20Report/</a></li>
<li>触发原因：${CAUSE}</li>
<li>项目Url：<a href="${PROJECT_URL}">${PROJECT_URL}</a></li>
</ul>
<hr/>
<h2>构建日志</h2>
<div>${JELLY_SCRIPT,template="html"}</div>
<hr/>
</div>
</body>
</html>
```
### 系统邮箱配置
Jenkins完成系统邮箱配置后，才能够发送邮件
配置内容：
- 配置'系统管理员邮件地址'
- 配置'Extended E-mail Notification'插件
- 配置'邮件通知'


## 自动化测试持续集成实现

### 实现效果

1. 自动化测试case执行不靠人工
    - 代码更新自动触发case执行
    - 每日定时自动触发case执行
2. 第一时间发布自动化测试结果
    - 测试结果通过邮件通知项目相关人员
    - 测试结果通过邮件通知项目相关人员

**核心**：Jenkins job 的源码配置

### 任务配置-源码管理

作用：能够让Jenkins自动从代码服务器上拉取自动化测试脚本代码

配置参数说明：
- Repository URL：项目仓库地址
- Credentials：登录凭证，需添加代码托管平台的登录用户名和密码

### 任务配置-构建触发器

作用：定义一些触发规则，当满足某一个规则时，让Jenkins开始执行自动化测试脚本
常用触发器：
- Build periodically：定时构建
- Poll SCM：轮询构建，定时轮询检查代码是否发生变更，如果发生变更就拉取最新代码并执行构建动作

### 任务配置-构建触发器-日程表介绍【了解】

Jenkins采用了著名的UNIX任务调度工具CRON所使用的配置方式，一般称之为“cron表达式”
基本语法格式：* * * * * ===> 分 时 日 月 星期
- 用5个字段代表5个不同的时间单位，中间用空格分隔
- 每一个位置都可以使用数字表示，还可以使用一些特殊字符
- *：表示匹配该域的任意值，假如在表示分的位置*, 即表示每分钟都会触发事件
示例：
- `0 8 * * *   每天上午8点构建一次`
- `*/1 * * * * 每分钟执行一次`
- `* */1 * * * 每小时执行一次`


### 任务配置-构建

作用：触发自动化测试脚本开始执行的命令
常用构建组件：
- Execute Windows batch command：运行Windows环境下的命令
- Execute shell：运行Linux和Mac环境下的命令

### 任务配置-构建后操作

作用：自动化测试脚本运行完之后要做的操作
常见构建后操作：
- 发布测试报告
- 发送邮件通知



### Allure报告配置

- 在后置操作中添加Allure报告的发布步骤
- 配置Allure报告的发布路径
- 配置Allure报告的发布方式

注意：
- 确保Allure报告的生成路径与配置的发布路径一致
- 注意Jenkins中allure插件的路径配置，确保能够正确找到allure命令
