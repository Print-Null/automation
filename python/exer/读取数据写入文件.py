# 将一个list[dict]的数据写入到本地txt文件中，格式如下：
# test1,123456
# test2,123456
# test3,123456
lists = [
    {"yoyo1": "111111"},
    {"yoyo2": "222222"},
    {"yoyo3": "333333"},
]

with open("./write.txt", "w+", encoding="utf-8") as f:
    for items in lists:
        print(items)
        for key, value in items.items():
            f.write("{0}:{1}".format(key, value) + "\n")

# a = [1, 2, 3, 4, 5]
# b = ["a", "b", "c", "d", "e"]
# 如何得出c = ["a1", "b2", "c3", "d4", "e5"]
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]
c = []

for i in range(len(a)):
    c.append(b[i] + str(a[i]))
print(c)

"""
写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com），程序识别用户名和公司名后，将用户名和公司名输出到控制台。 
要求： 
1. 校验输入内容是否符合规范（xx@polo.com）, 如是进入下一步，如否则抛出提 示"incorrect email format"。注意必须以.com 结尾 
2. 可以循环“输入--输出判断结果”这整个过程 
3. 按字母 Q（不区分大小写）退出循环，结束程序 
"""

operators = ["a", "i", "m", "q", "b", "c", "d", "e", "f", "g", "h", "j", "k"]
for opera in operators:
    print("输入除q以外的表示继续输入邮箱地址")
    print("输入q表示退出程序")
    operator = input("请输入您想要进行的操作：%s" % opera)
    if operator != "q":
        email = str(input("请输入您的邮箱地址："))
        if email.endswith(".com"):
            address = email.split(".")[0]
            if "@" in address:
                username = address.split("@")[0]
                copname = address.split("@")[1]
                if username != "" and copname != "":
                    print("用户名：{0}，公司名{1}".format(username, copname))
                else:
                    print("incorrect email format")
            else:
                print("incorrect email format")
        else:
            print("incorrect email format")
            continue
    if operator == "q":
        quit()
