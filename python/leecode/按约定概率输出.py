import random
from collections import Counter


def p_random(arr1, arr2):
    assert len(arr1) == len(arr2), "Length does not match."
    assert sum(arr2) == 1, "Total rate is not 1."

    sup_list = [len(str(i).split(".")[-1]) for i in arr2]
    # print("sup_list:%s" % sup_list)
    top = 10 ** max(sup_list)
    # print("top=%s" % top)
    new_rate = [int(i * top) for i in arr2]
    # print("new_rate:%s" % new_rate)
    rate_arr = []
    for i in range(1, len(new_rate) + 1):
        rate_arr.append(sum(new_rate[:i]))
    # print("rate_arr:%s" % rate_arr)
    rand = random.randint(1, top)
    data = None
    for i in range(len(rate_arr)):
        if rand <= rate_arr[i]:
            data = arr1[i]
            break
    # print("data:%s" % data)
    return data


plist = []
# for i in range(10000):
#     plist.append(p_random([1, 5, 7, 11, 12], [0.2, 0.2, 0.2, 0.2, 0.2]))
# print(Counter(plist))
for i in range(10000):
    plist.append(
        p_random([random.randint(3000, 4000), random.randint(4000, 6000), random.randint(6000, 10000)],
                 [0.5, 0.3, 0.2]))
# print(Counter(plist), type(Counter(plist)[1]), len(Counter(plist)))
sum1 = 0
sum2 = 0
sum3 = 0
counter = {}
for k, v in Counter(plist).items():
    if 3000 <= k < 4000:
        sum1 += v
    if 4000 <= k < 6000:
        sum2 += v
    if k >= 6000:
        sum3 += v
counter.update({"3000-4000": sum1, "4000-6000": sum2, "6000以上": sum3})
print(counter)