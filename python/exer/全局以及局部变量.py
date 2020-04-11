# 测试nonlocal、global关键字的用法

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

    inner()
    print("outer b:", b)
    print("outer a:", a)


outer()
print(b)
