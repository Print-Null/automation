for x in range(1, 10):
    for y in range(1, x + 1):
        print("{0}*{1}={2}".format(y, x, x * y), end="\t")
    print()

i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (j, i, i * j), end="\t")
        j += 1
    print()
    i += 1

'''
sum = 0
for i in range(1, 101):
    sum += i
print("1-100的和为：%d" % sum)

sum1 = 0
oushu = 0
jishu = 0
i = 1
while i <= 100:
    sum1 += i
    if i % 2 == 0:
        oushu += i
    else:
        jishu += i
    i += 1
print("1-100的和为：%d" % sum1)
print("1-100偶数和为：%d" % oushu)
print("1-100奇数和为：%d" % jishu)
'''