# 测试nonlocal、global关键字的用法
# 全局变量是可变类型，不论是函数内还是函数外都可以改变它的引用和值
# 全局变量是不可变类型，不论在函数内还是函数外都不可以改变它的值，如果想修改它的引用，必须用global关键申明这个变量
# 列表和字典是可变类型，数字、字符串、元组是不可变类型

a = 100
b = 55


def outer():
    b = 10
    global a
    a = 200

    def inner():
        nonlocal b  # 此处申明使用外部函数的局部变量b,而不是全局变量b
        global a  # 此处申请表示使用全局变量a
        print("inner b:", b)
        print("inner a:", a)
        b = 20  # 如果不使用nonlocal申明b，此处是无法修改外部函数的局部变量b的值的
        a = 1000
        print(a)
#
#     inner()
#     print("outer b:", b)
#     print("outer a:", a)
#
#
# outer()
# print(b)

# def factorial(n):
#     fac = 1
#     for i in range(1, n+1):
#         fac = fac * i
#         i += 1
#     return fac
#
#
# print(factorial(5))


# def factorial(n):
#     fac = 1
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))
