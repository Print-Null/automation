import pytest


@pytest.fixture(scope="function", params=None, autouse=False, ids=None, name=None)
def fixture():
    print("fixture初始化的参数列表")


@pytest.mark.usefixtures("fixture")
def test_fixture():
    print("fixture调用")


# 调用方式一
@pytest.fixture
def login():
    print("输入账号，密码先登录")


def test_s1(login):  # 如果需要用到fixture的返回值，必须使用这样传参的方式调用fixture
    print("用例 1：登录之后其它动作 111")


def test_s2():  # 不传 login
    print("用例 2：不需要登录，操作 222")


# 调用方式二
@pytest.fixture
def login2():
    print("please输入账号，密码先登录")


@pytest.mark.usefixtures("login2", "login")  # 可以使用多个fixture，先使用的放前面，后使用的放后面
def test_s11():
    print("用例 11：登录之后其它动作 111")


# 调用方式三
@pytest.fixture(autouse=True)  # autouse=True则该文件下的所有测试用例在执行前都要这行该fixture的内容
def login3():
    print("====auto===")


# 不是test开头，加了装饰器也不会执行fixture
@pytest.mark.usefixtures("login2")
def loginss():
    print(123)


@pytest.mark.usefixtures("fixture")  # 在类声明上面加@pytest.mark.usefixtures()，代表这个类里面所有测试用例都会调用该fixture
class TestFixture:
    def test1(self):
        print("第一次调用fixture")

    def test2(self):
        print("第二次调用fixture")

    def test3(self):
        print("第三次调用fixture")
