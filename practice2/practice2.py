# 模拟股价计算,以下数据纯虚构
name = "DeepSleep"  # 公司名称
stock_price = 19.99 # 当前股价
stock_code = "003032"  #股票代码
stock_price_daily_growth_factor = 1.2 # 股票增长系数
growth_days = 7 # 增长天数

print("公司：%s, 股票代码：%s, 当前股价：%.2f" % (name ,stock_code ,stock_price))
print("每日增长系数是：%.2f,经过%d天的增长,股价达到了：%.2f" % (stock_price_daily_growth_factor ,growth_days ,(stock_price * (stock_price_daily_growth_factor ** growth_days))))