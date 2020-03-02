# 多分支结构
a = input("请输入一个数字：")
# if int(a) < 10:
# print(a)
# else:
# print("a是大于10的数字")
print(a if int(a) < 10 else "a是大于10的数字")  # 三元运算表达式（条件为真时的值 if （条件表达式） else 条件为假时的值）

# 单分支结构
b = []
if not b:
    print("空的列表是false")

c = 0
if not c:
    print("0代表false")
