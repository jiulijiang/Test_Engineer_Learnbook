# Test_Engineer_Learnbook

## 📚 仓库简介

这是一个专注于个人学习测试技术知识的记录仓库，汇集了软件测试领域的核心知识、实用技能和学习笔记。本仓库旨在系统记录个人测试能力从基础到进阶的全面提升过程，作为个人成长的知识沉淀。

## 📁 目录结构

```
├── README.md                  # 项目说明文档
├── note/                      # 学习笔记目录
│   ├── App_test.md            # App测试笔记
│   ├── Appium_note.md         # Appium自动化测试笔记
│   ├── Interface_Test_note.md # 接口测试笔记
│   ├── Linux-learn.md         # Linux学习笔记
│   ├── OOP_Pytest_Detailed_Notes.md # 面向对象与Pytest详细笔记
│   ├── Performance Testing.md # 性能测试笔记
│   ├── Python_Learning_Notes_Optimized.md # 优化后的Python学习笔记
│   ├── Python_learn_note.md   # Python基础知识笔记
│   ├── SQL_note.md            # SQL学习笔记
│   ├── Selenium_note.md       # Selenium自动化测试笔记
│   ├── Software_test_theory_note.md # 软件测试理论笔记
│   ├── image/                 # 笔记中使用的图片资源
│   └── img/                   # 笔记中使用的图片资源（与image目录功能重复）
└── test_excel/                # 测试数据文件（Excel格式）
```

## 🔍 主要内容

### 1. 测试理论基础

- **软件测试概述**：软件定义、测试目的、主流技能要求
- **测试分类**：按阶段划分（单元测试、集成测试、系统测试、验收测试）、按代码可见度划分（黑盒测试、白盒测试、灰盒测试）
- **质量模型**：功能性、性能、兼容性、易用性、安全性、可靠性、可维护性、可移植性
- **测试流程**：需求评审、测试计划设计、测试用例设计、测试用例执行、缺陷管理、测试报告

### 2. 测试用例设计

- **测试用例八要素**：用例编号、用例标题、模块/项目、优先级、前置条件、测试步骤、测试数据、预期结果
- **测试用例设计方法**：
  - 等价类划分法：适用于批量数据测试场景
  - 边界值分析法：针对边界范围的测试场景
  - 判断表法：处理复杂逻辑组合
  - 场景法(流程图)：模拟用户实际操作流程
  - 错误推断法：基于经验预测可能的错误

### 3. 编程语言学习

- **Python基础**：变量、数据类型、控制流、函数、数据容器、异常处理、文件操作、模块与包、面向对象编程、高阶技巧等
- **SQL**：数据库操作和查询语言，支持数据测试和分析
- **Linux**：Linux系统基础命令和操作，包括目录结构、文件操作、权限管理等

### 4. 自动化测试

- **Selenium**：Web自动化测试框架学习笔记
  - 元素定位方法（ID、Class、CSS Selector等）
  - 元素操作（点击、输入、获取文本等）
  - 等待机制（隐式等待、显式等待）
- **Appium**：移动端自动化测试框架学习笔记
- **接口测试**：接口测试方法、工具和实践经验总结
- **Pytest**：Python测试框架的详细学习笔记

### 5. 高级测试技术

- **性能测试**：性能测试概念、工具使用、场景设计和结果分析
- **App测试**：移动端应用测试方法、工具和实践经验
- **测试数据管理**：多种测试场景的数据文件，存储在Excel格式中
  - 包含登录、注册、消息、百度等不同测试场景的测试数据

## 🚀 如何使用

### 查看学习笔记

- 直接打开`note`目录下的Markdown文件进行学习
- 笔记内容包含丰富的图片资源，使学习内容更加直观易懂

### 利用测试数据

- `test_excel`目录下提供了多种测试场景的数据文件
- 这些数据可以辅助理解测试用例设计和数据驱动测试的概念

## 📝 学习路径建议

1. **基础阶段**：
   - 学习软件测试基础理论（Software_test_theory_note.md）
   - 掌握Python编程语言基础（Python_learn_note.md 或 Python_Learning_Notes_Optimized.md）
   - 学习Linux基础命令（Linux-learn.md）
   - 熟悉SQL基础（SQL_note.md）

2. **进阶阶段**：
   - 学习Selenium自动化测试（Selenium_note.md）
   - 学习接口测试（Interface_Test_note.md）
   - 掌握测试用例设计方法

3. **实践阶段**：
   - 结合测试数据文件（test_excel/目录）进行测试用例设计实践
   - 尝试使用Selenium进行简单的Web自动化测试

4. **提升阶段**：
   - 学习性能测试（Performance Testing.md）
   - 学习App测试（App_test.md）和Appium自动化（Appium_note.md）
   - 掌握Pytest测试框架（OOP_Pytest_Detailed_Notes.md）

## 🛠️ 开发工具推荐

- **IDE**：PyCharm、VSCode
- **浏览器**：Chrome、Edge
- **测试框架**：Selenium、Pytest、Appium
- **数据管理**：Excel、数据库
- **版本控制**：Git
- **测试管理工具**：Jira、TestLink

## 📅 更新记录

- **仓库定位优化**：专注于个人学习测试技术的知识整理，不再存储测试练手代码
- **代码迁移**：测试练手代码已迁移至其他专门仓库
- **新增内容**：
  - Appium_note.md（Appium自动化测试笔记）
  - Interface_Test_note.md（接口测试笔记）
  - OOP_Pytest_Detailed_Notes.md（面向对象与Pytest详细笔记）
- **结构优化**：持续优化学习笔记结构，内容更加系统化

---

**祝您学习愉快，测试技能不断提升，早日成为优秀的测试工程师！** 🎉