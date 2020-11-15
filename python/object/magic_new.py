# 测试__new__
class TestA:
    def __init__(self):
        print("TestA start init......")

    def __new__(cls, *args, **kwargs):
        print("create a TestA instance[%s]" % cls)
        return object.__new__(cls)


TestA()


class TestB:
    def __init__(self):
        print("TestB start init......")

    def __new__(cls, *args, **kwargs):
        print("create a TestB instance[%s]" % cls)
        return "abc"


TestB()


class Obj(object):
    def __init__(self):
        print("this is another object called")


class TestC:
    def __init__(self):
        print("TestC start init")

    def __new__(cls, *args, **kwargs):
        print("create a TestC instance[%s]" % cls)
        test_new = Obj()
        return test_new


TestC()
