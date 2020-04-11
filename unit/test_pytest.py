"""
class Persion():
    def __init__(self,name,score,weight):
        self.name = name
        self.score = score
        self.weight = weight


student = Persion('yxf', 100, 170)
#print(student)
#print(Persion)
#student.name = 'yxf'
#student.score = 100
print(student.name)
print(student.score)

"""


class Persion():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        sum = self.x + self.y
        return sum

    def square(self):
        squr = pow(self.x, 3) + pow(self.y, 3)
        return squr

    def add_square(self):
        c = self.add() + self.square()
        return c


student = Persion(2, 3)
print(student.add())
print(student.square())
print("--------我是可爱的分割线--------")
print(student.add_square())


class Persion():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, z=16):
        sum = self.x + self.y + z
        return sum

    def square(self):
        sqr = pow(self.x, 3) + pow(self.y, 3)
        return sqr

    def add_square(self, z):
        c = self.add() + self.square() + z
        return c


student = Persion(3, 4)
print(student.add())
print(student.square())
print("--------我是可爱的分割线--------")
print(student.add_square(16))
