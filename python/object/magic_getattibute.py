class Ob(object):
    def __init__(self):
        self.c = 5


class TestA(object):
    def __init__(self):
        self.a = 5

    def __setattr__(self, key, value):
        if key == "a":
            print("调用setattr")
            return object.__setattr__(self, key, value + 50)
        if key == "b":
            print("调用setattr")
            return object.__setattr__(self, key, value - 50)

    def __getattr__(self, item):
        a = Ob()
        print("can not find attribute %s" % item)
        return a.__getattribute__(item)


test_a = TestA()
print(test_a.a)
test_a.a = 100
print(test_a.a)
test_a.b = 200
print(test_a.b)
print(test_a.c)
