def num(n: int):
    if n == 1 or n == 2:
        return 1
    else:
        return num(n - 1) + num(n - 2)


def num_list(n: int):
    if n > 0:
        num_list = []
        add_num = 0
        for i in range(1, n + 1):
            num_list.append(num(i))
        print(num_list)
        for j in num_list:
            add_num += j
        return num_list[-1], add_num
    else:
        return "please input correct number!"


print(num_list(10))
