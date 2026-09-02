# 模拟登陆
user_name = input("请输入用户名")

# 暂时未实现密码验证功能
user_password = input("请输入密码")

# input输入均为字符串类型，可自行转换数据类型
user_password = int(user_password)

print("您好：%s, 欢迎使用" % user_name)