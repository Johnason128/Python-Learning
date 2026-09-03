# 模拟登陆
user_name = input("请输入用户名")

# 验证用户名和密码
name = "admin"
password = 123456789
user_password = input("请输入密码")

# input输入均为字符串类型，可自行转换数据类型
user_password = int(user_password)

# 为了使用f-string,另外简化代码所以假设用户名唯一
print(f"您输入的用户名：{name == user_name}")
print(f"您输入的密码:{password == user_password}")

if password == user_password and name == user_name:
    print("您好：%s, 欢迎使用" % user_name)
else:
    print("请重新输入密码或用户名")
