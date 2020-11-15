# 测试重写object的__str__()

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 定义了__str__方法的类，并且该方法返回值是一个字符串，实例直接可以打印，否则直接打印实例会报错
        return "名字是：{0}".format(self.name)


print(Person("YXF"))


class Person1:
    def __init__(self, name):
        self.name = name


print(Person1("gcx"))


# 测试可调用方法__call__()
class SalaryAccount:
    def __call__(self, salary):
        print("算工资了...")
        yearSalary = salary * 12
        daySalary = salary // 22.5
        houreSalary = daySalary // 8
        return dict(yearSalary=yearSalary, monthSalary=salary, daySalary=daySalary, houreSalary=houreSalary)


s = SalaryAccount()
print(s(15000))  # 实例方法可以通过方法名+()来调用，实例也可以通过实例名+()来调用，只不过调用实例需要定义实例的__call__方法，调用实例默认调用实例的__call__方法
