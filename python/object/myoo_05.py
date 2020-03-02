# 测试浅复制、深复制

import copy


class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


class CPU:
    def calculate(self):
        print("计算你个鬼啊...")
        print("CPU对象：", self)


class Screen:
    def show(self):
        print("显示一个美丽的画面，亮瞎你的钛合金狗眼...")
        print("Screen对象：", self)


# 测试变量赋值
c1 = CPU()
c2 = c1
print("测试变量赋值......")
print(c1)
print(c2)

# 测试浅复制(浅复制只复制对象本身，而不复制对象的属性和子对象)
s1 = Screen()
m1 = MobilePhone(c1, s1)
m2 = copy.copy(m1)
print("测试浅复制......")
print(m1, m1.cpu, m1.screen)
print(m2, m2.cpu, m2.screen)

# 测试深复制(深复制不光复制对象，也复制对象的属性和子对象)
m3 = copy.deepcopy(m1)
print("测试深复制......")
print(m1, m1.cpu, m1.screen)
print(m3, m3.cpu, m3.screen)
