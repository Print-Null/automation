import os
import sys

import yaml

path = r"D:\MyProjects\my_parcels_ka\data"
# old_str = "user"
# new_str = "ka"
# for file in os.listdir(path):
#     file_name = file.split(".")[0]
#     file_type = file.split(".")[-1]
#     if old_str in file_name:
#         file_name = file_name.replace(old_str, new_str)
#     new_file = file_name + "." + file_type
#     os.rename(os.path.join(path, file), os.path.join(path, new_file))

# 批量修改文件编号
add_number = 1
for file in os.listdir(path):
    if os.path.isdir(os.path.join(path, file)):
        for json_file in os.listdir(os.path.join(path, file)):
            if json_file.endswith("json"):
                number_old = int(json_file.split("_", 1)[0])
                old_name = json_file.split("_", 1)[-1]
                number_new = str(number_old + add_number)
                new_name = number_new + "_" + old_name
                os.rename(os.path.join(os.path.join(path, file), json_file),
                          os.path.join(os.path.join(path, file), new_name))
    elif file.endswith("yaml") and not file.startswith("master"):
        number_old = int(file.split("_", 1)[0])
        old_name = file.split("_", 1)[-1]
        number_new = str(number_old + add_number)
        new_name = number_new + "_" + old_name
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
#     if file.startswith("master"):
#         # yaml_file = yaml.load(file)
#         with open(file, "w+", encoding="utf-8") as f:
#             line = f.readline()
#             if isinstance(line,dict):
#                 pass
