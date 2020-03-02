# 测试嵌套循环
for x in range(5):
    for y in range(5):
        print(x, end="\t")
    print()
print("***************************************")

# 打印九九乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print("{0}*{1}={2}".format(x, y, (x * y)), end="\t")
    print()
print("***************************************")
t1 = {"name": "高小一", "age": 18, "salary": 30000, "city": "北京"}
t2 = {"name": "高小二", "age": 19, "salary": 20000, "city": "上海"}
t3 = {"name": "高小三", "age": 20, "salary": 10000, "city": "深圳"}
list1 = [t1, t2, t3]
for x in list1:
    if x.get("salary") > 15000:
        print(x)
