# ==========================
# 📅 Day 2: 月度开销计算器
# ==========================

# 1. 定义变量 (给每个开销贴上标签)
# 注意：金额通常带有小数，所以我们使用 float (浮点数)
rent = 2500.0       # 房租
food = 1280.5       # 餐饮费
transport = 350.0   # 交通费
entertainment = 200 # 娱乐费 (即使是整数，也可以和浮点数相加)

# 2. 进行运算 (计算总和)
# Python 会自动处理 int 和 float 的混合运算，结果会是 float
total_expense = rent + food + transport + entertainment

# 3. 输出结果
# 方法 A: 简单的逗号分隔 (print 自动会在逗号间加空格)
print("------ 本月账单明细 ------")
print("房租:", rent)
print("餐饮:", food)
print("交通:", transport)
print("娱乐:", entertainment)
print("------------------------")

# 方法 B: 使用 f-string (格式化字符串，推荐！更美观)
# {variable:.2f} 表示保留两位小数，非常适合显示金额
print(f"💰 本月总开销为: {total_expense:.2f} 元")

# 进阶思考：如果想算出平均每天的开销怎么办？
# 假设一个月 30 天
daily_average = total_expense / 30
print(f"📉 平均每天开销: {daily_average:.2f} 元")