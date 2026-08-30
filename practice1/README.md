# 练习 1：Python 基础语法、变量与数据类型 | Practice 1: Python Basic Syntax, Variables, and Data Types

## 目标 | Objective
- 掌握 Python 的基础输出 `print()` 函数。 | Master the basic `print()` function in Python.
- 学习变量的定义、赋值与动态更新。 | Learn variable definition, assignment, and dynamic updating.
- 理解基本数据类型（整数、浮点数、字符串）及类型转换。 | Understand basic data types (int, float, string) and type conversion.
- 掌握字符串的拼接方法。 | Master string concatenation methods.

## 代码示例 | Code Example
```python
print("Hello World!")

# 定义一个变量，记录钱包余额 | Define a variable to record wallet balance
money = 50

# 通过print语句，输出变量记录的内容 | Output the content recorded by the variable
print("钱包还有：", money)

money = money - 10
print("买了一个冰淇淋花费10元，还剩：", money, "元")

# 打印变量的数据类型 | Print the data type of the variable
print(type(money))

# 将数字类型转换成浮点数 | Convert number type to float
num_str = float(11)
print(num_str)

# 字符串字面量和字符串变量拼接 | Concatenate string literals and string variables
name = "杰克"
address = "美国纽约"
print("我是" + name + "，我在" + address)