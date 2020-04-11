a = input("请输入要转换的字符串：")
ascii = []
if len(a) > 1:
    for i in a:
        ascii.append(str(ord(i)))  # ascii码转字符串用chr函数，字符串转ascii码用ord函数
print("".join(ascii))
