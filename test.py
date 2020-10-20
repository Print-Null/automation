# import os
# import ruamel.yaml
# import yaml
# from sign import Sign
#
#
# # path = r"D:\MyProjects\my_parcels_ka\data"
# # for file in os.listdir(path):
# #     if file.startswith("master"):
# #         file_path = os.path.join(path, file)
# #         print(file)
# #         # with open(file_path, "r", encoding="utf-8") as f:
# #         #     load_master = ruamel.yaml.safe_load(f)
# #         #     for line in load_master["test_case"]:
# #         #         line["case_id"] += 1
# #         # with open(file_path, "w+", encoding="utf-8") as outfile:
# #         #     ruamel.yaml.safe_dump(load_master, outfile, default_flow_style=False, allow_unicode=True)
# #         with open(file_path, "r", encoding="utf-8") as f:
# #             #load_master = yaml.safe_load(f)
# #             for line in f.readlines():
# #                 if "case_id" in line:
# #                     load_line = yaml.safe_load(line)
# #                     load_line["case_id"] += 1
# #         with open(file_path, "w+", encoding="utf-8") as outfile:
# #             yaml.safe_dump(load_line, outfile, default_flow_style=False, allow_unicode=True)
# #             # if "case_id" in line:
# #             #     # print(line)
# #             #     print(line)
# #             #     dict_line = yaml.safe_load(line)
# #             #     dict_line["case_id"] = dict_line["case_id"] + 1
# #             #     line = f.write(yaml.dump(dict_line))
# #             #     print(line)
# #             # print(dict_line)
# #             # for key, value in dict_line.items():
# #             #     # print(key, type(key))
# #             #     # print(value, type(value))
# #             #     new_value = str(value + 1)
# #             #     # print(line, type(line))
# #             #     print(new_value)
# #             # line = line.replace(str(value), str(value + 1))
# #             # print(line)
with open(r"E:\MyProjects\master_my_parcels.yaml", "w+", encoding="utf-8") as f:
    f.write("this is a test write")
    line = f.readlines()
    print(type(line), line)
    for i in line:
        print(i)


def fun(m):
    def fun1(n):
        return m * n

    return fun1


a = fun(5)
print(a(6))
