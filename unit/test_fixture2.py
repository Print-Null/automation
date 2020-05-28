# 1.较高scope范围的fixture（session）在较低scope范围的fixture（function、class）之前实例化【session>package>module>class>function】
# 2.具有相同作用域的fixture遵循测试函数中声明的顺序，并遵循fixture之间的依赖关系【在fixture_A里面依赖的fixture_B优先实例化，然后到fixture_A实例化】
# 3.自动使用（autouse=True）的fixture将在显式使用（传参或装饰器）的fixture之前实例化,在session、package、module之后实例化


import pytest

order = []


@pytest.fixture(scope="session")
def s1():
    order.append("s1")


@pytest.fixture(scope="module")
def m1():
    order.append("m1")


@pytest.fixture(autouse=True)  # autouse=True的fixture只能作用于class和function级别
def all():
    order.append("all")


@pytest.fixture
def f1(f3, a1):
    # 先实例化f3, 再实例化a1, 最后实例化f1
    order.append("f1")
    assert f3 == 123


@pytest.fixture
def f3():
    order.append("f3")
    a = 123
    yield a


@pytest.fixture
def a1():
    order.append("a1")


@pytest.fixture(scope="package")
def f2():
    order.append("f2")


def test_scope(all, s1, m1, f1, f3):
    print(order)


def test_order(f1, m1, f2, s1):
    # m1、f2、s1在f1后，但因为scope范围大，所以会优先实例化
    # assert order == ["s1", "f2", "m1", "f3", "a1", "f1"]
    print(order)
