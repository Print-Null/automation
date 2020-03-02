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
