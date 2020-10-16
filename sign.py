import ast
import hashlib


class Sign(object):

    def create_sign(self, parameter, key):
        # # 拿到配置文件中对应环境的key
        # print("\n加密之前的请求参数集合：\n%s" % parameter_new)
        # read_config_object = ReadConfig()
        # redis_object = RedisBase()
        # env = redis_object.get("runenv_py")
        # if env is False:
        #     env = "trunk"
        # else:
        #     env = redis_object.get("runenv_py")
        # key = read_config_object.get_config(env, "key")
        # print("打印获取到的对应环境的key：\n%s" % key)
        if isinstance(parameter, str):
            # 如果参数集合是字符串类型，将需要排序的参数集合转换成字典
            parameter_dict = ast.literal_eval(parameter)
            # 将参数集合的所有key取出来（不包括空值key和sign）
            argument_list = []
            for k, v in parameter_dict.items():
                if v != "" and k != "sign":
                    argument_list.append(k)
            # 将key按ASCII码排序
            argument_list.sort()
            print("要参与加密的参数按ASCII码排序后的列表：\n%s" % argument_list)
            sha_string_list = []
            for i in argument_list:
                sha_string_list.append(i)
                sha_string_list.append("=")
                sha_string_list.append(str(parameter_dict[i]))
                sha_string_list.append("&")
            # 排序后按key=value&key=value...将参数和值拼接成符合要求的字符串
            sha_string = "".join(sha_string_list)
            print("要加密的参数组成字符串：\n%s" % sha_string)
            # 拼接key
            string_sign_temp = sha_string + "key=" + key
            print("拼接key之后的最终加密字符串：\n%s" % string_sign_temp)
            sha256 = hashlib.sha256()
            sha256.update(string_sign_temp.encode("utf-8"))
            # 加密成sha256字符串并将字母都转换成大写的
            sign = sha256.hexdigest().upper()
            print("加密后生成的签名：\n%s" % sign)
            parameter = parameter.replace("sha256", sign)
            return parameter
        elif isinstance(parameter, dict):
            # 将参数集合的所有key取出来（不包括空值key和sign）
            argument_list = []
            for k, v in parameter.items():
                if v != "" and k != "sign":
                    argument_list.append(k)
            # 将key按ASCII码排序
            argument_list.sort()
            print("要参与加密的参数按ASCII码排序后的列表：\n%s" % argument_list)
            sha_string_list = []
            for i in argument_list:
                sha_string_list.append(i)
                sha_string_list.append("=")
                sha_string_list.append(str(parameter[i]))
                sha_string_list.append("&")
            # 排序后按key=value&key=value...将参数和值拼接成符合要求的字符串
            sha_string = "".join(sha_string_list)
            print("要加密的参数组成字符串：\n%s" % sha_string)
            # 拼接key
            string_sign_temp = sha_string + "key=" + key
            print("拼接key之后的最终加密字符串：\n%s" % string_sign_temp)
            sha256 = hashlib.sha256()
            sha256.update(string_sign_temp.encode("utf-8"))
            # 加密成sha256字符串并将字母都转换成大写的
            sign = sha256.hexdigest().upper()
            print("加密后生成的签名：\n%s" % sign)
            parameter = str(parameter).replace(str(parameter["sign"]), sign)
            return ast.literal_eval(parameter)
    # def create_sign(self, parameter, key):
    #     sha_map = {"dstProvinceName": "พระนครศรีอยุธยา",
    #                "expressCategory": 1,
    #                "insureDeclareValue": 12000,
    #                "insured": 1,
    #                "remark": "-",
    #                "srcCityName": "บางคอแหลม",
    #                "srcProvinceName": "กรุงเทพ",
    #                "weight": 500,
    #                "srcDistrictName": "",
    #                "dstDistrictName": "",
    #                "pre": 1,
    #                "length": 22,
    #                "width": 101,
    #                "height": 22,
    #                "sign": "parameter"
    #                }
    #     print(type(sha_map))
    #     key = "905dd2520bbf04b87df22f05db1821d96cedb8ccbd18fa29ca95220c833bbe36"
    #     append_list = []
    #     for k, v in sha_map.items():
    #         if v != "" and k != "sign":
    #             append_list.append(k)
    #     append_list.sort()
    #     list1 = []
    #     for i in append_list:
    #         list1.append(i)
    #         list1.append("=")
    #         list1.append(str(sha_map[i]))
    #         list1.append("&")
    #     stringA = "".join(list1)
    #     string_sign_temp = stringA + "key=" + key
    #     sha256 = hashlib.sha256()
    #     sha256.update(string_sign_temp.encode("utf-8"))
    #     sign = sha256.hexdigest().upper()
    #     print(sign)
    #     sha_map = str(sha_map).replace("parameter", sign)
    #     print(sha_map, type(sha_map))
