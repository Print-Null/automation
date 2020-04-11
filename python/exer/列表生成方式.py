# 测试推导式


# 列表推导式
y = [x * 2 for x in range(50) if x % 5 == 0]
print(y)

y = []
for x in range(1, 50):
    if x % 5 == 0:
        y.append(x * 2)
print(y)

cell = [(m, n) for m in range(1, 10) for n in range(1, 10)]
print(cell)

for m in range(1, 10):
    for n in range(1, 10):
        print((m, n))

# 字典推导式
my_text = "i love you,i love sxt,i love gaocaixia"
char_count = {c: my_text.count(c) for c in my_text}
print(char_count)

# 集合推导式
b = {x for x in range(100) if x % 5 == 0}
print(b)

# 生成器推导式(生成元组)
gnt = (x for x in range(4))
print(tuple(gnt))
for x in gnt:  # gnt是生成器对象，生成器是可迭代的对象，只能使用一次
    print(x, end=",")
print(tuple(gnt))
