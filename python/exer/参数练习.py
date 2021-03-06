# 测试参数

def fun1(a, b, c, d):
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))


fun1(10, 20, 30, 40)  # 位置参数：和位置相对应
fun1(c=50, b=20, a=100, d=10)  # 强制命名参数：不按位置对应必须强制命名


def fun2(a, b, c=60, d=100):  # 默认值参数：带有默认值得参数必须放在没有默认值得参数后边，否则无法识别
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))


fun2(1, 2)
fun2(1, 2, 10)
fun2(5, 6, 30, 40)


def fun3(a, b, *c, **d):  # *c代表元组,**d代表字典,字典参数必须在元组参数后边
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))


fun3(1, 2, 3, 4, 5, name="yxf", age=18)


def fun4(*a, b, c, **d):  # 当元组或者字典参数在前面时，后边的其他参数必须强制命名
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))


fun4(2, 3, 4, name="杨晓锋", age=20)   # 会报错，因为a是元组参数，此处会把2,3,4都赋给参数a，那么参数b和c则没有指定值，所以会报错
fun4(2, b=3, c=4, name="杨晓锋", age=20)
