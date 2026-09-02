# 练习 3：用户输入与类型转换（模拟登录） | Practice 3: User Input and Type Conversion (Simulated Login)

## 目标 | Objective
- 掌握 `input()` 函数获取用户输入的方法。 | Master the `input()` function to get user input.
- 理解 `input()` 函数返回值的类型（字符串）。 | Understand the return type of `input()` function (string).
- 使用 `int()` 函数进行类型转换。 | Use `int()` function for type conversion.
- 掌握字符串格式化输出（`%s` 占位符）。 | Master string formatting output (`%s` placeholder).

## 代码示例 | Code Example
```python
# 模拟登陆
user_name = input("请输入用户名")

# 暂时未实现密码验证功能
user_password = input("请输入密码")

# input输入均为字符串类型，可自行转换数据类型
user_password = int(user_password)

print("您好：%s，欢迎使用" % user_name)