# 测试lambda表达式

f = lambda a, b, c: a + b + c
print(f)
print(f(2, 3, 4))

g = [lambda a: a * 2, lambda b: b * 3, lambda c: c * 4]
print(g[0](6), g[1](7), g[2](8))

# 测试eval()函数:将对象转变成表达式执行

s = "print('abcde')"
eval(s)

a = 10
b = 20
c = eval("a + b")
print(c)

dict1 = dict(a=100, b=200)
d = eval("a+b", dict1)
print(d)
