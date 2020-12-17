import re
from interface_aotumation.utils.redisbase import RedisBase
import ast
import json
from interface_aotumation.common.readconfig import ReadConfig
from jsonschema import validate
import time
import random
import datetime
import os
import logging
import requests
from interface_aotumation.common.public_def import *


class BaseTestCase(object):
    def __init__(self):
        self.redisObj = RedisBase()
        # self.staffObj = Staff()
        self.readConfigObj = ReadConfig()

    def parameter_parser(self, parameter, headers = [], head = []):
        self.headers = headers
        self.head = head
        if type(parameter) == str:
            var_list = re.findall('\$.*?\$', parameter)
            if var_list:
                for val in var_list:
                    parameter = self.extend_logic(parameter, val)
            if '[def]' in parameter:
                var_list = re.findall('\$.*?\$', parameter)
                _val = var_list[0][6: -1].split("|")
                if _val[0] == "create_sign":
                    sign_data = create_sign(parameter = parameter)
                    parameter = parameter.replace(var_list[0], str(sign_data))
            return parameter
        elif type(parameter) == list:
            p = []
            for v in parameter:
                parame = str(v)
                var_list = re.findall('\$.*?\$', parame)
                for val in var_list:
                    parame = self.extend_logic(parameter, val)
                parame = ast.literal_eval(parame)
                _parame = {}
                for vv in parame:
                    if '[int]' in str(parame[vv]):
                        _parame[vv] = int(parame[vv][5:])
                    else:
                        _parame[vv] = parame[vv]
                p.append(_parame)
            return p
        elif type(parameter) == dict:
            if parameter:
                parameter = str(parameter)
                var_list = re.findall('\$.*?\$', parameter)
                for val in var_list:
                    parameter = self.extend_logic(parameter, val)
                if '[def]' in parameter:
                    var_list = re.findall('\$.*?\$', parameter)
                    _val = var_list[0][6: -1].split("|")
                    if _val[0] == "create_sign":
                        sign_data = create_sign(parameter = parameter)
                        parameter = parameter.replace(var_list[0], str(sign_data))
                parameter = ast.literal_eval(parameter)
                return parameter
            else:
                if '[def]' in parameter:
                    var_list = re.findall('\$.*?\$', parameter)
                    _val = var_list[0][6: -1].split("|")
                    if _val[0] == "create_sign":
                        sign_data = create_sign(parameter = parameter)
                        parameter = parameter.replace(var_list[0], str(sign_data))
                parameter = ast.literal_eval(parameter)
                return parameter
        else:
            parameter = str(parameter)
            var_list = re.findall('\$.*?\$', parameter)
            for val in var_list:
                parameter = self.extend_logic(parameter, val)
            if '[def]' in parameter:
                var_list = re.findall('\$.*?\$', parameter)
                _val = var_list[0][6: -1].split("|")
                if _val[0] == "create_sign":
                    sign_data = create_sign(parameter = parameter)
                    parameter = parameter.replace(var_list[0], str(sign_data))
            parameter = ast.literal_eval(parameter)
            return parameter

    def extend_logic(self, parameter, val):
        try:
            if '[python]' in val:
                eval_code = eval(val[9: -1])
                if type(eval_code) == int:
                    parameter = parameter.replace("'" + val + "'", str(eval_code))
                elif type(eval_code) == str:
                    if eval_code.lower() == 'true':
                        parameter = parameter.replace("'" + val + "'", 'True')
                    elif eval_code.lower() == 'false':
                        parameter = parameter.replace("'" + val + "'", 'False')
                    else:
                        parameter = parameter.replace(val, str(eval_code))
                else:
                    parameter = parameter.replace(val, str(eval_code))
            elif '[config]' in val:
                runenv_py = self.redisObj.get("runenv_py")
                if runenv_py == False:
                    runenv_py = "trunk"
                code = self.readConfigObj.get_config(runenv_py, val[9: -1])
                try:
                    eval_code = eval(code)
                except:
                    parameter = parameter.replace(val, code)
                else:
                    if type(eval_code) in [int, list]:
                        try:
                            _parameter = eval(parameter)
                        except:
                            parameter = parameter.replace(val, str(eval_code))
                        else:
                            if type(_parameter) in [dict, list]:
                                parameter = parameter.replace("'" + val + "'", code)
                            else:
                                parameter = parameter.replace(val, str(eval_code))
                    else:
                        parameter = parameter.replace(val, str(eval_code))
            elif '[db]' in val:
                _val = val[5: -1].split("|")
                staff_id = ""
                if _val[0] == "get_role_staff_id":
                    role_id = eval(_val[1]).get("role_id") if eval(_val[1]).get("role_id") else None
                    state = eval(_val[1]).get("state") if eval(_val[1]).get("state") else None
                    store_id = eval(_val[1]).get("store_id") if eval(_val[1]).get("store_id") else None
                    category = eval(_val[1]).get("category") if eval(_val[1]).get("category") else None
                    limit = eval(_val[1]).get("limit") if eval(_val[1]).get("limit") else None
                    staff_id = self.staffObj.get_role_staff_id(role_id = role_id, state = state,
                                                               store_id = store_id, category = category,
                                                               limit = limit)
                elif _val[0] == "get_role_staff_id_manger":
                    staff_info_id = eval(_val[1]).get("staff_info_id") if eval(_val[1]).get(
                        "staff_info_id") else None
                    staff_id = self.staffObj.get_role_staff_id_manger(staff_info_id = staff_info_id)

                parameter = parameter.replace(val, str(staff_id))
            # elif '[def]' in val:
            #     _val = val[6: -1].split("|")
            #     if _val[0] == "create_sign":
            #         sign_data = create_sign(parameter = parameter)
            #         parameter = parameter.replace(val, str(sign_data))
            else:
                val_a = val
                if self.headers and self.head:
                    _var_list = re.findall('\#.*?\#', val)
                    for _val in _var_list:
                        _res = _val[1: -1]
                        if _res == "headers":
                            val_a = val.replace(_val, str(self.headers.index(self.head)))
                res = self.redisObj.get(val_a[1: -1])
                if res:
                    if '[int]' in res:
                        parameter = parameter.replace(val, int(res[5:]))
                    else:
                        parameter = parameter.replace(val, str(res))
                else:
                    parameter = parameter.replace(val, val)
        except:
            parameter = parameter.replace(val, "")
        return parameter

    def is_json(self, data):
        try:
            json.loads(data)
        except ValueError:
            return False
        return True

    def get_host(self, data):
        # runenv_py = False#self.redisObj.get("runenv_py")
        runenv_py = self.redisObj.get("runenv_py")
        if runenv_py == False:
            runenv_py = "trunk"
        return ReadConfig().get_config(runenv_py, data)

    def validate_jsonschema(self, response_result, schema_file_name):
        curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        path_dir = curpath + "/jsonschema_validate/"
        print(path_dir)
        current_path = path_dir + schema_file_name
        with open(current_path, "r", encoding = 'utf-8') as f:
            shcema = json.load(f)
            res = validate(instance = response_result, schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
            return res

    def fbi_login(self, **kwargs):
        """

        :param kwargs: account,pwd
        :return: bool
        """
        try:
            account = kwargs.get("account") if kwargs.get("account") else None
            pwd = kwargs.get("pwd") if kwargs.get("pwd") else None

            fbi_host = self.get_host("fbi_host_domain")
            url = fbi_host + "/loginuser/login"
            logging.info("fbi_login fbi_url： " + url)
            data = {
                "py_test": "1",
                "account": account,
                "pwd": pwd
            }
            logging.info("fbi_login 请求参数： " + str(data))
            resp = requests.post(url = url, data = data)
            logging.info("fbi_login 返回结果： " + resp.text)
            cookies_dict = requests.utils.dict_from_cookiejar(resp.cookies)
            logging.info("fbi_login fbi_PHPSESSID： " + cookies_dict["PHPSESSID"])
            RedisBase().set('fbi_PHPSESSID', cookies_dict["PHPSESSID"], ex = 6000)
            RedisBase().set('fbi_PHPSESSID_api', "lang=zh-CN;PHPSESSID=" + cookies_dict["PHPSESSID"] + ";", ex = 6000)
            logging.info("success:fbi_login")
            return True
        except:
            logging.info("error:方法fbi_login异常")
            return False
