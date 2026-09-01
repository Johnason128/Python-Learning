# 练习 2：变量定义与字符串格式化（模拟股价计算） | Practice 2: Variable Definition and String Formatting (Simulated Stock Price Calculation)

## 目标 | Objective
- 掌握 Python 中不同数据类型（字符串、浮点数、整数）的变量定义与命名规范。 | Master variable definition and naming conventions for different data types (string, float, int) in Python.
- 熟练使用 `%` 操作符进行字符串格式化输出（`%s`, `%d`, `%.2f`）。 | Proficiently use the `%` operator for string formatting output.
- 理解并应用 Python 中的幂运算符 (`**`) 进行连续增长/复利计算。 | Understand and apply the exponentiation operator (`**`) for continuous growth/compound interest calculations.

## 代码示例 | Code Example
```python
# 模拟股价计算,以下数据纯虚构
name = "DeepSleep"  # 公司名称
stock_price = 19.99 # 当前股价
stock_code = "003032"  # 股票代码
stock_price_daily_growth_factor = 1.2 # 股票增长系数
growth_days = 7 # 增长天数

# 使用 %s (字符串) 和 %.2f (保留两位小数的浮点数) 格式化输出
print("公司：%s, 股票代码：%s, 当前股价：%.2f" % (name, stock_code, stock_price))

# 使用 %d (整数)、%.2f 和幂运算 (**) 计算并输出最终股价
print("每日增长系数是：%.2f, 经过%d天的增长, 股价达到了：%.2f" % 
      (stock_price_daily_growth_factor, growth_days, (stock_price * (stock_price_daily_growth_factor ** growth_days))))