# 解决数据驱动在run的时候用例名称中文显示成ascii码
def pytest_collection_modifyitems(items):
    # 测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
