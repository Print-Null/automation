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

print("\n")
print("*******************************************我是分割线*******************************************")
print("\n")


# 测试私有属性和私有方法
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def __work(self):  # 私有方法
        print("我是中国人")


e = Employee("杨晓锋", 33)
print(e.name)
print(dir(e))
print(e._Employee__age)  # 类外调用类的私有属性通过"_类名__属性名"调用
e._Employee__work()  # 类外调用类的私有方法通过"_类名__方法名"调用


