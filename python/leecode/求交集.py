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
