# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
# 求1000以内的水仙花数（3位数）
import math

# 方法一
flower = []

for i in range(100, 1000):
    a = int(i / 100)
    b = int((i - 100 * a) / 10)
    c = i - 100 * a - 10 * b
    if a * a * a + b * b * b + c * c * c == i:
        flower.append(i)
print(flower)

# 方法二
lists = []
for i in range(101, 1000):
    i = str(i)
    i1, i2, i3 = int(i[0]), int(i[1]), int(i[2])
    if int(i) == int(math.pow(i1, 3) + math.pow(i2, 3) + math.pow(i3, 3)):
        lists.append(i)

print(lists)

"""
写一个函数alphabet_index，该函数参数是1个字符串，
要求该函数返回一个新字符串，里面是 参数字符串中每个字母依次对应的 数字。如果是非字母，则忽略它
字母"a" 和"A" 都对应 1, "b"和"B"都对应2, "c"和"C"对应3， 依次类推
比如:
alphabet_index("Wow, does that work?")
➞ "23 15 23 4 15 5 19 20 8 1 20 23 15 18 11"
"""


def alphabet_index(arg: str):
    bet = dict()
    key_list = [chr(k) for k in range(97, 123)]
    value_list = [v for v in range(1, 27)]
    for k, v in zip(key_list, value_list):
        bet[k] = v
    strs = arg.lower()
    num = []
    for m in strs:
        if m.isalpha() and m in bet.keys():
            num.append(bet[m])
    return num


print(alphabet_index("Wow, does that work?"))
