# 从给定目录下查找包含有hello的py文件
import os

file_list = []


# 递归函数，该函数中所有的文件路径全部采用绝对路径，parent_dir：文件所在父目录的绝对路径，file_name表示当前你要处理的文件或者目录
def find_hello(parent_dir, file_name):
    file_abspath = os.path.join(parent_dir, file_name)  # 当前正在处理的文件或者目录的绝对路径
    if os.path.isdir(file_abspath):  # 判断该绝对路径是目录
        for f in os.listdir(file_abspath):  # 进入该绝对路径并列出该目录下的所有文件和目录列表
            find_hello(file_abspath, f)  # 递归调用本身函数直到目录下不再有目录
    else:
        if file_abspath.endswith(".py"):  # 如果是文件判断该文件是以.py结尾的py文件
            if find_and_exist_hello(file_abspath):  # 如果是py文件调用hello的查找方法
                file_list.append(file_abspath)  # 将包含hello的文件保存到列表中


def find_and_exist_hello(py_file):
    flag = False  # 定义一个是否包含有hello的标记变量，默认文件中不包含hello为False
    f = open(py_file, "r", encoding="UTF-8")  # 因为文件名字可能包含中文所有打开文件指定文件编码为UTF-8
    while True:  # 由于是一行一行的读取文件，所以是死循环
        line = f.readline()  # 读取其中一行
        if line == "":  # 文件读取到最后一行，终止循环
            break
        elif "hello" in line:
            flag = True  # 该行中包含有hello则给标记变量flag赋值True并终止循环
            break
    f.close()
    return flag  # 文件中查找到hello返回True，没查找到则返回False


find_hello(r"D:\MyProjects", "python")
print(file_list)
