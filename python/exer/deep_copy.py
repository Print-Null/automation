# 测试浅拷贝、深拷贝

import copy


def Copy():
    '''测试浅拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.copy(a)

    print("a:", a)
    print("b:", b)

    b.append(30)
    b[2].append(7)

    print("浅拷贝.......................")
    print("a:", a)
    print("b:", b)


def DeepCopy():
    '''测试深拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)

    print("a:", a)
    print("b:", b)

    b.append(30)
    b[2].append(7)

    print("深拷贝.......................")
    print("a:", a)
    print("b:", b)


Copy()
print("***************我是分割线******************")
DeepCopy()
print(DeepCopy.__doc__)