# 闭包两个条件：
# 1.外部函数中有内部函数
# 2.内部函数引用了外部函数的变量

def fun1():
    def fun2():
        print("我是fun2")
        fun1()
    return fun2


a = fun1()  # 将fun1函数的返回值fun2(fun2不带括号表示fun2函数对象本身)赋值给a，此时如果想调用fun2函数则可以通过a()来调用，这就是闭包的主要功能：即在不改变原函数的基础上扩展了原函数的功能
print("fun1调用完成")
print(a())  # 通过a()来调用fun2函数，这里就相当于是fun2()

print("------------------我是分割线------------------")


def fun3(a, b):
    def fun4(x):
        return a * x + b

    return fun4


f = fun3(4, 5)
f1 = f(2)
print(f)
print(f1)
