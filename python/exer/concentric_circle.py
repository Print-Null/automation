# 绘制同心圆
import turtle

t = turtle.Pen()
t.width(5)
t.speed(15)
my_color = ("red", "blue", "green", "black")

for x in range(10):
    t.penup()
    t.goto(0, -x * 20)
    t.pendown()
    t.color(my_color[x % len(my_color)])
    t.circle(20 + x * 20)

turtle.done()
