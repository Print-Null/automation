class Student:
    company = "SXT"  # 类属性

    def __init__(self, name, score):
        self.name = name    # 实例属性
        self.score = score

    def say_score(self):  # 实例方法
        print("{}的分数是：{}".format(self.name, self.score))

    @classmethod  # 类方法需要用classmethod申明
    def printCompany(cls):
        '''类方法的第一个参数必须是cls，如同实例方法（类中所有没有用classmethod申请的方法）的第一个参数必须是self一样
           self:实例对象本身，cls：类对象本身'''

        print(cls.company)
        # print(self.name)  会报错，类方法中不能调用实例方法和实例参数


s1 = Student("杨晓锋", 90)
s1.say_score()
s1.age = 30
s1.salary = 3000
print(id(s1))
print(type(s1))
print(s1.salary)

Student.printCompany()
s1.company = "YXF"
print(s1.company)
s1.printCompany()

print(dir(s1))  # 打印s1对象的所有对象
print(s1.__dict__)  # 打印s1对象的所有字典


class Man:
    pass


print(isinstance(s1, Student))  # s1是不是Student类的对象，是输出True，不是输出False
print(isinstance(s1, Man))
print(isinstance(Student, type))  # 所有的类都是type类的对象
print(Student.mro())
