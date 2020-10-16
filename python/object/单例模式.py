# 单例模式一：伪单例模式


class User(object):
    __instance = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_instance(cls, name):
        if not cls.__instance:
            cls.__instance = User(name)
        return cls.__instance


# 之所以叫伪单例模式是因为要想实现单例模式必须调用get_instance方法去实例化对象，而一旦调用init方法去实例化对象则不是单例模式
u1 = User.get_instance("zs")
u2 = User.get_instance("ls")
print(u1.name, u2.name)
print(u1 == u2)
print("u1对象的内存地址：%s，u2对象的内存地址：%s" % (id(u1), id(u2)))


# 单例模式二

class User1(object):
    __instance = False

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


u1 = User1("zs")
u2 = User1("ls")
u3 = User1("ww")
print(u1.name, u2.name, u3.name)
print(u1 == u2)
print("u1对象的内存地址：%s，u2对象的内存地址：%s，u3对象的内存地址：%s" % (id(u1), id(u2), id(u3)))
