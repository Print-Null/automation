# 循环结构-while
num = 0
while num <= 10:
    print(num)
    num += 1
print("******************************************")
# 计算1-100之间数字的和
num = 0
sum_all = 0
while num <= 100:
    sum_all += num
    num += 1
print("1-100所有数的累加和:", sum_all)
print("******************************************")
# 循环结构-for
d = {"name": "杨晓锋", "age": 32, "adress": "张家口"}
for x in d:
    print(x)
for x in d.keys():
    print(x)
for x in d.values():
    print(x)
for x in d.items():
    print(x)
print("******************************************")

sum_all = 0  # 1-100的累加总和
sum_add = 0  # 1-100的奇数和
sum_even = 0  # 1-100的偶数和
for x in range(101):
    sum_all += x
    if x % 2 == 0:
        sum_even += x
    else:
        sum_add += x
print("1-100的累加总和为{0}，偶数和为{1}，奇数和为{2}".format(sum_all, sum_even, sum_add))
print("******************************************")