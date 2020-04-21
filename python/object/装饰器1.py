def outer(fun):
    def wrapper(a, b, c):  # 装饰器：装饰了传入的函数，将传入函数的功能做了扩展
        print("---wrapper---")
        return fun(a, b) + c
        # fun()

    return wrapper


# 加了装饰器的调用
@outer
def fun1(a, b):
    print("---fun1---")
    return a + b


print(fun1(1, 2, 3))


# 不加装饰器的调用
def fun2(a, b):
    print("---fun2---")
    return a + b


f = outer(fun2)
print(f(3, 4, 5))
