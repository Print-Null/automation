'''
有数组名为array:[3,4,7,11,10,9,7,4,5,7,2,8,11,23,45...],如果数组中任意三个数相加是偶数，
将这三个数的组合打印出来，要求这三个数不能有以下情形：
1.索引重复：例如array[1],array[1],array[2]视为重复
2.组合重复：例如array[1],array[2],array[3]和array[3],array[2],array[1]这种视为重复
3.值重复：例如 3,7,7
'''
import random

# def print_digit(a: list):
#     b = {}
#     c = []
#     for i in range(len(a) - 2):
#         for j in range(i + 1, len(a) - 1):
#             for k in range(j + 1, len(a)):
#                 if a[i] != a[j] and a[i] != a[k] and a[j] != a[k] and (a[i] + a[j] + a[k]) % 2 == 0:
#                     if sorted([i, j, k]) not in c:
#                         c.append(sorted([i, j, k]))
#                         d = {(i, j, k): sorted([a[i], a[j], a[k]])}
#                         b.update(d)
#                         # b.append("下标:%s,%s,%s;组合:%s" % (i, j, k, [a[i], a[j], a[k]]))
#     return b  # sorted(b), len(b)
#
#
# print(print_digit([3, 4, 7, 11, 10, 9, 7, 4, 5, 7, 2, 8, 11, 23, 45]))
from collections import Counter


def random_count(arr1, arr2):
    str_list = [len(str(i).split(".")[1]) for i in arr2]
    top = 10 ** max(str_list)
    count_list = [int(i * top) for i in arr2]
    rate_arr = []
    for i in range(1, len(count_list) + 1):
        rate_arr.append(sum(count_list[:i]))
    rand = random.randint(1, top)
    data = None
    for i in range(len(rate_arr)):
        if rand <= rate_arr[i]:
            data = arr1[i]
            break
    return data


p_list = []
for i in range(10000):
    p_list.append(random_count([1, 2, 3, 4], [0.200, 0.300, 0.400, 0.100]))
print(Counter(p_list))
