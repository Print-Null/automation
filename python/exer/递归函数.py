# 测试递归函数的基本原理

# 计算阶乘


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(result)


# 嵌套函数（内部函数）

def f1():
    print("f1")

    def f2():
        print("f2")

    f2()


f1()


# 斐波拉契数列

def get_num(n):
    if n == 1 or n == 2:
        return 1
    else:
        return get_num(n - 1) + get_num(n - 2)


sum = []
for i in range(1, 20):
    sum.append(get_num(i))
print("斐波拉契数列：%s" % sum)
