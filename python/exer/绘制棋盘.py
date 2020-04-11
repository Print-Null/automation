# 绘制棋盘

import turtle

width = 20
num = 18
t = turtle.Pen()
t.speed(10)
x1 = [(-360, 360), (-360 + width * num, 360)]
y1 = [(-360, 360), (-360, 360 - width * num)]

for i in range(19):
    t.penup()
    t.goto(x1[0][0], x1[0][1] - i * 20)
    t.pendown()
    t.goto(x1[1][0], x1[1][1] - i * 20)

for i in range(19):
    t.penup()
    t.goto(y1[0][0] + i * 20, y1[0][1])
    t.pendown()
    t.goto(y1[1][0] + i * 20, y1[1][1])

turtle.done()



