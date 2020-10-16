def different(num1: list, num2: list):
    diff = []
    for i in num1:
        for j in num2:
            if i == j and i not in diff:
                diff.append(i)
                break
    print(diff)


different([1, 2, 3, 2, 3], [2, 3])
different([2, 4, 5, 9, 4, 2], [2, 2, 4, 4, 4])


def different(num1: list, num2: list):
    a = iter(set(num1))
    print(a)
    b = iter(set(num2))
    print(b)
    for i in b:
        if i in a:
            yield i
        else:
            continue
    # print(list(different()))


print(list(different([1, 2, 3, 2, 3], [2, 3])))
print(list(different([2, 4, 5, 9, 4, 2], [2, 2, 4, 4, 4, 8])))
