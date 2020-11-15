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


