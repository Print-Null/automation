# 测试多分支结构

score = input("请输入分数")
grade = ""
if int(score) < 60:
    grade = "不及格"
elif int(score) < 80:
    grade = "及格"
elif int(score) < 90:
    grade = "良好"
else:
    grade = "优秀"
print("分数是{0},等级是{1}".format(score, grade)) #字符串格式化
