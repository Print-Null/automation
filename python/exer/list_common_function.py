# Encoding = UTF - 8
print("=" * 50)
print("学生名字管理系统".center(50))
print("输入1：表示添加学生名字")
print("输入2：表示查找学生名字")
print("输入3：表示修改学生名字")
print("输入4：表示删除学生名字")
print("输入5：表示查看所有学生信息")
print("输入6：退出学生名字管理系统")
students = []
while True:
    operator = input("请输入您想要的操作:")
    if operator == "1":
        name = input("请输入要添加的学生名字：")
        age = int(input("请输入要添加的学生年龄："))
        address = input("请输入要添加的学生籍贯：")
        person = {}
        person["name"] = name
        person["age"] = age
        person["address"] = address
        students.append(person)  # append方法往列表的末尾追加元素，strip方法去除空格，lstrip去除左边空格，rstrip去除右边空格
    if operator == "2":
        name = input("请输入要查找的学生名字：")
        for item in students:
            if name in item["name"]:
                print("%s存在，年龄为：%s，籍贯为：%s" % (name, item["age"], item["address"]))
                break
        else:
            print("%s没有找到" % name)
    if operator == "3":
        name = input("请输入要修改的学生名字：")
        age = int(input("请输入要修改的学生年龄："))
        address = input("请输入要修改的学生籍贯：")
        for item in students:
            if item["name"] == name and item["age"] == age and item["address"] == address:
                print("学生存在，可以进行修改")
                changer = input("请输入要修改的信息:(m表示修改学生名字,n表示修改学生年龄,j表示修改学生籍贯,q表示退出修改)")
                if changer == "m":
                    new_name = input("请输入修改后的学生名字：")
                    item["name"] = new_name
                if changer == "n":
                    new_age = int(input("请输入修改后的学生年龄："))
                    item["age"] = new_age
                if changer == "j":
                    new_address = input("请输入修改后的学生籍贯：")
                    item["address"] = new_address
                if changer == "q":
                    break
                break
        else:
            print("找不到要修改的学生")
    if operator == "4":
        name = input("请输入要删除的学生名字：")
        age = int(input("请输入要删除的学生年龄："))
        address = input("请输入要删除的学生籍贯：")
        for item in students:
            if item["name"] == name and item["age"] == age and item["address"] == address:
                students.remove(item)  # remove方法移除列表中的元素，pop方法从列表末尾移除元素
                break
        else:
            print("找不到要删除的学生")
    if operator == "5":
        print("序号\t姓名\t\t年龄\t\t籍贯")
        for i, item in enumerate(students, 1):
            print("%s\t%s\t%s\t\t%s" % (i, item["name"], item["age"], item["address"]))
    if operator == "6":
        break
