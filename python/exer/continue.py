# 测试continue
emp_num = 0
salary_sum = 0
salarys = []
while True:
    s = input("请输入一个正整数(按Q或q时退出):")
    if s == "Q" or s == "q":
        print("录入完成，退出")
        break
    if float(s) < 0:
        continue
    emp_num += 1
    salarys.append(float(s))
    salary_sum += float(s)
print("员工数量:{}".format(emp_num))
print("录入薪资:", salarys)
print("平均薪资:{0}".format(salary_sum / emp_num))

# 测试zip并运行迭代

names = ["张一", "张二", "张三", "张四"]
ages = [19, 20, 21, 22]
jobs = ["老师", "程序员", "公务员"]

for name, age, job in zip(names, ages, jobs):
    print("{0}--{1}--{2}".format(name, age, job))

for i in range(3):
    print("{0}--{1}--{2}".format(names[i], ages[i], jobs[i]))



