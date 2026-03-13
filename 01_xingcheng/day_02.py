# 自学日期：2026年3月13日
# 自学第2天


# 封装年龄计算函数：
def calculate_age(name,birth_year):

    # 这是一个文本盒子，装着你的名字
    my_name = "老王"  # 请把引号里的内容改成你自己的名字或昵称

    # 这是一个数字盒子，装着你的出生年份 (不要加引号！)
    birth_year = 1994  # 请改成你真实的出生年份

    # 定义今年的年份
    current_year = 2026

    # 计算年龄：用今年减去出生年
    age = current_year - birth_year

    # f-string 格式化输出：在花括号里直接写变量名
    return f"你好，{name}！在2026年，你将是 {age} 岁。"
    
#print(calculate_age("老王",1994))

# 交互式调用示例
user_name = input("请输入你的名字：")
# 注意：input() 得到的是字符串，要用 int() 转成数字！
user_birth_year = int(input("请输入你的出生年份："))  

result = calculate_age(user_name, user_birth_year)
print(result)

# 加上成年判断
age = 2026 - user_birth_year
if age >= 18:
    print("你已经是成年人啦！")
else:
    print("还在成长中哦～")