# with open(r"C:\Users\Administrator\Downloads\prometheus.yml", "r") as f:
#     print(f.read())
#     f.read(5)  # 读取文件的前5个字符
#     f.tell()  # 打印当前的光标位置
#     f.seek(0, 0)  # 将光标移动到开头（第二个参数：0表示文件开头，1表示当前位置，2表示文件末尾）
#     f.close()

# 复制文件
source_file = r"C:\Users\Administrator\Downloads\prometheus.yml"
target_file = "copy-" + source_file[source_file.rfind("\\") + 1:]
print("目标文件名字：%s" % target_file)
# 打开文件
source_f = open(source_file, "rb")
target_f = open(target_file, "wb")
# 读取源文件内容
content = source_f.read()
# 将读取的源文件内容写入目标文件
target_f.write(content)
# 关闭源文件和目标文件
source_f.close()
target_f.close()


