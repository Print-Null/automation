color = ["白色", "蓝色", "红色", "蓝色", "红色", "红色", "白色", "蓝色", "白色", "红色", "白色", "蓝色", "白色", "蓝色", "红色"]
red_color = []
white_color = []
blue_color = []
for i in color:
    if i == "红色":
        red_color.append(i)
    elif i == "白色":
        white_color.append(i)
    elif i == "蓝色":
        blue_color.append(i)
print("排序后:%s" % (red_color + white_color + blue_color))
print(len(color))
print("*******************************我是分割线*******************************")

for x in range(len(color) - 1):
    for y in range(len(color) - x - 1):
        if color[y] == "蓝色":
            color[y], color[y + 1] = color[y + 1], color[y]
        for z in range(len(color) - x - y - 1):
            if color[z] == "白色":
                color[z], color[z + 1] = color[z + 1], color[z]
print(color)

color1 = ["白色", "红色", "白色", "白色", "红色", "白色"]

for i in range(len(color1) - 1):
    for j in range(len(color1) - i - 1):
        if color1[j] == "白色":
            color1[j], color1[j + 1] = color1[j + 1], color1[j]
print(color1)

bubble = [7, 1, 4, 6, 8, 2, 9, 3, 5]
for i in range(len(bubble) - 1):
    for j in range(len(bubble) - i - 1):
        if bubble[j] > bubble[j+1]:
            bubble[j], bubble[j+1] = bubble[j+1], bubble[j]
print(bubble)
