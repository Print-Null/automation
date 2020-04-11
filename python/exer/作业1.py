# 读取输入的字符串，并计算字符串中各个字符出现的次数
lower_list = [chr(i) for i in range(97, 123)]  # 小写字母列表
upper_list = [chr(i) for i in range(65, 91)]  # 大写字母列表
full_list = lower_list + upper_list
sub_str = input("请输入要统计的字符串:")
for i in full_list:
    if i in sub_str:
        print(str(i) + ':' + str(sub_str.count(i)), end=" ")
print('\n' + '=' * 30)

# 读取用户输入的多个子路径，最后拼装成一个完整的路径
path_list = []
while True:
    operator = input("请输入要进行的操作(输入1表示继续输入，输入2表示退出输入)：")
    if operator == "1":
        sub_list = input("请输入子路径：")
        path_list.append(sub_list)
        continue
    if operator == "2":
        break
print("".join(path_list))





