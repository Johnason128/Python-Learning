# 练习 4：用户登录验证系统（条件判断与 f-string） | Practice 4: User Login Verification System (Conditional Statements and f-string)

## 功能 | Function
- 掌握 Python 的条件判断语句（`if-else`）。 | Master Python conditional statements (`if-else`).
- 学习使用 f-string 进行字符串格式化输出。 | Learn using f-string for string formatting output.
- 实现用户名和密码的验证逻辑。 | Implement username and password verification logic.
- 理解逻辑运算符 `and` 的使用。 | Understand the use of logical operator `and`.

## 代码结构 | Code Structure
```python
# 模拟登陆
user_name = input("请输入用户名")

# 验证用户名和密码
name = "admin"
password = 123456789
user_password = input("请输入密码")

# input输入均为字符串类型，可自行转换数据类型
user_password = int(user_password)

# 为了使用f-string，另外简化代码所以假设用户名唯一
print(f"您输入的用户名：{name == user_name}")
print(f"您输入的密码：{password == user_password}")

if password == user_password and name == user_name:
    print("您好：%s，欢迎使用" % user_name)
else:
    print("请重新输入密码或用户名")