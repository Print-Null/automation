# 测试break
while True:
    a = input("请输入一个字符(输入Q或q时退出):")
    if a == "Q" or a == "q":
        print("循环结束，退出")
        break
    else:
        print(a)
