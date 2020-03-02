def print_max(a, b):
    '''打印两个数中较大的'''
    if a > b:
        print(a)
    else:
        print(b)


print_max(10, 20)
print(id(print_max))
print(type(print_max))
help(print_max.__doc__)


# 测试返回值的基本用法

def test01(a, b):
    print("{0},{1},{2}".format(a, b, (a + b)))
    return a + b


c = test01(10, 20) * 10
print(c)


def test02():
    print("yxf")
    print("杨晓锋")
    return
    print("hello")


d = test02()
print(d)


def test03(x, y, z):
    return [x * 10, y * 10, z * 10]


print(test03(1, 2, 3))
