import datetime

print(datetime.datetime.now(), '1')


class Golem:
    print(datetime.datetime.now(), '2')

    def __init__(self, name=None):
        print(datetime.datetime.now(), '3')
        self.name = name
        print(datetime.datetime.now(), '4')
        self.built_year = datetime.date.today().year
        print(datetime.datetime.now(), '5')

    def say_hi(self):
        print(datetime.datetime.now(), '6')
        print('Hi!')
        print(datetime.datetime.now(), '7')


print(datetime.datetime.now(), '8')
g = Golem('Clay')
print(datetime.datetime.now(), '9')
g.name
print(datetime.datetime.now(), '10')
g.built_year
print(datetime.datetime.now(), '11')
g.say_hi
print(datetime.datetime.now(), '12')
g.say_hi()
print(datetime.datetime.now(), '13')
