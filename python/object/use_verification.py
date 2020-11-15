def verification(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


print(verification(6))


def verify(n):
    if n == 1:
        return 1
    else:
        return n * verify(n - 1)


print(verify(6))


