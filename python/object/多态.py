# 测试多态

class Man:
    def eat(self):
        print("饿了，吃饭了......")


class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭!")


class India(Man):
    def eat(self):
        print("印度人用右手吃饭!")


class English(Man):
    def eat(self):
        print("英国人用叉子吃饭!")


def manEat(m):
    if isinstance(m, Man):  # isinstance方法用来判断m是不是Man的子集
        m.eat()  # 多态：一个方法的调用，根据对象不同调用不同的方法
    else:
        print("不能吃饭!")


manEat(Chinese())
manEat(English())
manEat(India())
manEat(Man())
manEat(English)

print(Man.__subclasses__())
print(Man.__dict__)
print(Man.__class__)
