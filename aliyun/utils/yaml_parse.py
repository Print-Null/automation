import yaml
from yaml.scanner import ScannerError
import os
import json
import time
import datetime
import re
import math
from common.public import *
from multiprocessing import Process
from time import sleep
import os
import asyncio


class YamlJsonAttr(dict):
    """定义一个对象数据获取器"""

    def __init__(self, *args, **kwargs):
        super(YamlJsonAttr, self).__init__(*args, **kwargs)

    def __getattr__(self, item):
        value = None
        try:
            value = self[item]
        except Exception:
            pass
        if isinstance(value, dict):
            value = YamlJsonAttr(value)
        return value


class BaseYamlParser(object):
    """yaml文件解析器"""

    def __init__(self, path):
        self.path = os.path.abspath(path)

    @property
    def _reader(self):
        with open(self.path, 'r', encoding = 'utf-8') as f:
            cont = f.read()
        try:
            yaml_content = yaml.safe_load(cont)
            return YamlJsonAttr(yaml_content)
        except ScannerError:
            msg = 'ymal文件{}格式不正确'.format(os.path.abspath(self.path))
            raise False

    @property
    def to_json(self):
        return self._reader


class ConfigParser(BaseYamlParser):
    """配置文件解析器"""

    def __init__(self, yaml_path):
        BaseYamlParser.__init__(self, yaml_path)

    @property
    def case_data(self):
        return self._reader.case_data

    @property
    def case_path(self):
        return self._reader.case_path

    @property
    def test_case(self):
        return self._reader.test_case


class CaseCodeTemplate(object):
    """代码模版"""

    def __init__(self, **kwargs):
        self.mode = kwargs.get("mode") if kwargs.get("mode") else None
        self.mode_head_parameter = kwargs.get("mode_head_parameter") if kwargs.get("mode_head_parameter") else 0
        self.test_case_len = kwargs.get("test_case_len") if kwargs.get("test_case_len") else 0
        test_case = kwargs.get("test_case") if kwargs.get("test_case") else 0
        extend_test_case = kwargs.get("extend_test_case") if kwargs.get("extend_test_case") else None

        self.test_name = test_case["test_name"]
        self.class_name = "Test_" + self.test_name
        self.def_name = "test_" + self.test_name
        self.info = test_case["info"]
        self.host = extend_test_case["host"]
        self.http_type = extend_test_case["http_type"]
        self.request_type = extend_test_case["request_type"]
        self.parameter_type = extend_test_case["parameter_type"]
        self.timeout = extend_test_case["timeout"]
        self.address = extend_test_case["address"]
        if self.mode:
            self.case_id = int(test_case["case_id"]) + (int(self.mode_head_parameter) * 10 * int(self.test_case_len))
            _head = {0: extend_test_case["headers"][self.mode_head_parameter]}
            self.headers = _head
        else:
            self.case_id = test_case["case_id"]
            self.headers = extend_test_case["headers"]
        self.success = extend_test_case["success"]
        self.error = extend_test_case["error"]

        self.success_parameter = self.success_check = self.relevance = {}
        if self.success:
            self.success_parameter = self.success["parameter"]
            self.success_check = self.success["check"]
            self.relevance = self.success["relevance"]

        self.error_parameter = self.error_check = {}
        self.error_parameter_index = 0
        if self.error:
            self.error_parameter = self.error["parameter"]
            self.error_check = self.error["check"]

    @property
    def import_code(self):
        data = """
import sys,os
sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0]+"/flash")
import allure
from assertpy import assert_that
import requests
import logging
import ast
import json
import time
import pytest
from common.base import BaseTestCase
from utils.redisbase import RedisBase
from jsonschema import validate
                """
        return data

    @property
    def class_code(self):
        data = """
logging.basicConfig(level=logging.INFO)


@allure.feature('{}')
class {}(object):
""".format(self.info, self.class_name)
        return data

    @property
    def success_def_code(self):
        data = ""
        if self.request_type == 'post':
            data = '''
    @pytest.mark.run(order={})
    def test_{}(self, parameter,headers,address):
        baseTest = BaseTestCase()
    '''.format(self.case_id, self.def_name)
        elif self.request_type == 'get':
            data = '''
    @pytest.mark.run(order={})
    def test_{}(self,headers,address):
        baseTest = BaseTestCase()
    '''.format(self.case_id, self.def_name)
        elif self.request_type == 'patch':
            data = '''
    @pytest.mark.run(order={})
    def test_{}(self, parameter,headers,address):
        baseTest = BaseTestCase()
    '''.format(self.case_id, self.def_name)
        elif self.request_type == 'delete':
            data = '''
    @pytest.mark.run(order={})
    def test_{}(self, parameter,headers,address):
        baseTest = BaseTestCase()
    '''.format(self.case_id, self.def_name)
        return data

    @property
    def error_def_code(self):
        data = ""
        if self.request_type == 'post':
            data = '''
    @pytest.mark.run(order={})
    def test_{}_error_{}(self, parameter,headers,address):
        baseTest = BaseTestCase()
    '''.format(self.case_id, self.def_name, self.error_parameter_index)
        elif self.request_type == 'get':
            data = '''
    @pytest.mark.run(order={})
    def test_{}_error_{}(self,headers,address):
        baseTest = BaseTestCase()
    '''.format(self.case_id, self.def_name, self.error_parameter_index)
        return data

    @property
    def success_parametrize_parameter_code(self):
        data = ""
        if self.request_type.lower() in ["post", "patch", "delete"]:
            if self.success_parameter:
                p = []
                for v in self.success_parameter:
                    p.append(str(self.success_parameter[v]))
                data = '''
    @pytest.mark.parametrize("parameter",{})'''.format(p)

            else:
                data = '''
    @pytest.mark.parametrize("parameter",["{}"])'''

        return data

    def error_parametrize_parameter_code(self, error_parameter_index):
        data = ""
        if self.request_type.lower() == "post":
            if self.error_parameter:
                p = []
                p.append(str(self.error_parameter[error_parameter_index]))
                data = '''
    @pytest.mark.parametrize("parameter",{})'''.format(p)

            else:
                data = '''
    @pytest.mark.parametrize("parameter",["{}"])'''

        return data

    @property
    def parametrize_header_code(self):
        if self.headers:
            p = []
            for v in self.headers:
                p.append(str(self.headers[v]))
            data = '''
    @pytest.mark.parametrize("headers",{})'''.format(p)

        else:
            data = '''
    @pytest.mark.parametrize("headers",["{}"])'''

        return data

    @property
    def parametrize_address_code(self):
        if type(self.address) == str:
            data = """
    @pytest.mark.parametrize("address",['{}'])""".format(self.address)
        else:
            p = []
            for v in self.address:
                p.append(str(self.address[v]))
            data = """
    @pytest.mark.parametrize("address",{})""".format(p)

        return data

    @property
    def body_parameter_code(self):
        data = ""
        if self.request_type.lower() in ["post", "patch", "delete"]:
            if self.success_parameter:
                p = []
                for v in self.success_parameter:
                    p.append(str(self.success_parameter[v]))
                data = '''
        _parameter = {}
        '''.format(p)
            else:
                data = '''
        _parameter = ["{}"]
        '''
        elif self.request_type.lower() == "get":
            data = '''
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        '''
        return data

    @property
    def error_body_parameter_code(self):
        data = ""
        if self.request_type.lower() == "post":
            if self.success_parameter:
                p = []
                for v in self.success_parameter:
                    p.append(str(self.success_parameter[v]))
                data = '''
        parameter_new = baseTest.parameter_parser(parameter)
        if '[int]' in parameter_new:
            parameter = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
        '''.format(p)
            else:
                data = '''
        parameter_new = baseTest.parameter_parser(parameter)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
        '''
        return data

    @property
    def success_body_header_code(self):
        if self.headers:
            p = []
            for v in self.headers:
                p.append(str(self.headers[v]))
            data = '''
        _headers = {}
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        '''.format(p)

            if self.request_type.lower() in ["post", "patch", "delete"]:
                data = data + '''
        parameter_new = baseTest.parameter_parser(parameter, _headers, headers)
        address_new = baseTest.parameter_parser(address, _headers, headers)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
                '''
        else:
            data = '''
        _headers = ["{}"]
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        '''
            if self.request_type.lower() in ["post", "patch", "delete"]:
                data = data + '''
            parameter_new = baseTest.parameter_parser(parameter, _headers, headers)
            address_new = baseTest.parameter_parser(address, _headers, headers)
            if '[int]' in parameter_new:
                parameter_new = ast.literal_eval(parameter_new)
                for key in parameter_new:
                    if '[int]' in str(parameter_new[key]):
                        parameter_new[key] = int(parameter_new[key][5:])
            else:
                parameter_new = ast.literal_eval(parameter_new)
                    '''
        return data

    @property
    def error_body_header_code(self):
        data = '''
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        '''
        return data

    @property
    def success_body_address_code(self):
        if type(self.address) == str:
            data = '''
        _address = ['{}']
        '''.format(self.address)
        else:
            if self.address:
                p = []
                for v in self.address:
                    p.append(str(self.address[v]))
                data = '''
        _address = {}
            '''.format(p)
            else:
                data = '''
        _address = ["{}"]
            '''
        return data

    @property
    def body_url_code(self):
        data = '''
        host = '{}'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)'''.format(self.host)
        return data

    @property
    def body_request_type_code(self):
        data = ""
        if self.request_type.lower() == "post":
            data = '''
        if "application/json" in str(headers).lower():
            resp = requests.post(url = url, json = parameter_new, headers = headers_new, timeout = 120, verify = False)
        else:
            resp = requests.post(url = url, data = parameter_new, headers = headers_new, timeout = 120, verify = False)
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("请求参数日志信息：")
        logging.info(parameter_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        '''.format(self.timeout)
        elif self.request_type.lower() == "get":
            data = '''
        resp = requests.get(url=url, headers=headers_new, verify=False, timeout={})
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        '''.format(self.timeout)
        elif self.request_type.lower() == "patch":
            data = '''
        if "application/json" in str(headers).lower():
            resp = requests.patch(url = url, json = parameter_new, headers = headers_new, timeout = 120, verify = False)
        else:
            resp = requests.patch(url = url, data = parameter_new, headers = headers_new, timeout = 120, verify = False)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        '''.format(self.timeout)
        elif self.request_type.lower() == "delete":
            data = '''
        resp = requests.delete(url=url, data=parameter_new, headers=headers_new, verify=False, timeout={})
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        '''.format(self.timeout)
        return data

    @property
    def body_relevance_code(self):
        data = ""
        for val in self.relevance:
            redis_key = self.test_name
            if self.success_parameter:
                redis_key += "_' + str(_parameter.index(parameter)) + '"
            if self.headers:
                redis_key += "_' + str(_headers.index(headers)) + '"
            if self.address:
                redis_key += "_' + str(_address.index(address)) + '"
            redis_key = redis_key + "_" + val
            redis_code = '''
        RedisBase().set('{}', {}, ex=6000)
        '''.format(redis_key, "resp.json()" + val)
            data += redis_code
        return data

    @property
    def success_assert_check_code(self):
        data = ""
        for v in self.success_check:
            if v == "check_type":
                data += '''
        assert_that(baseTest.is_{}(resp.text)).is_equal_to(True)
        '''.format(self.success_check["check_type"])
            elif v == "expected_code":
                if type(self.success_check["expected_code"]) == str:
                    data += '''
        assert_that(resp.status_code).is_equal_to('{}')
        '''.format(self.success_check["expected_code"])
                else:
                    data += '''
        assert_that(resp.status_code).is_equal_to({})
        '''.format(self.success_check["expected_code"])
            elif v == "code":
                code_key = self.success_check["code_key"] if self.success_check["code_key"] else None
                if code_key:
                    if type(self.success_check["code"]) == str:
                        data += '''
        assert_that(resp.json(){}).is_equal_to('{}')
        '''.format(code_key, self.success_check["code"])
                    else:
                        data += '''
        assert_that(resp.json(){}).is_equal_to({})
        '''.format(code_key, self.success_check["code"])
                else:
                    data += '''
        assert_that(resp.json()["code"]).is_equal_to({})
        '''.format(self.success_check["code"])
            elif v == "msg":
                z_msg = self.success_check["msg"]["z_message"]
                e_msg = self.success_check["msg"]["e_message"]
                t_msg = self.success_check["msg"]["t_message"]
                data_key = self.success_check["msg"]["data_key"]
                data_key_path = self.success_check["msg"]["data_key_path"] if "data_key_path" in self.success_check[
                    "msg"].keys() else None
                headers_language = self.success_check["msg"]["headers_language"]
                if data_key_path:
                    data += '''
        if "zh" in eval(headers)["{}"].lower():
            assert_that(resp.json(){}).is_equal_to("{}")
        elif "th" in eval(headers)["{}"].lower():
            assert_that(resp.json(){}).is_equal_to("{}")
        elif "en" in eval(headers)["{}"].lower():
            assert_that(resp.json(){}).is_equal_to("{}")
        '''.format(headers_language, data_key_path, z_msg,
                   headers_language, data_key_path, t_msg,
                   headers_language, data_key_path, e_msg)
                else:
                    data += '''
        if "zh" in eval(headers)["{}"].lower():
            assert_that(resp.json()["{}"]).is_equal_to("{}")
        elif "th" in eval(headers)["{}"].lower():
            assert_that(resp.json()["{}"]).is_equal_to("{}")
        elif "en" in eval(headers)["{}"].lower():
            assert_that(resp.json()["{}"]).is_equal_to("{}")
        '''.format(headers_language, data_key, z_msg,
                   headers_language, data_key, t_msg,
                   headers_language, data_key, e_msg)
            elif v == "data":
                for vv in self.success_check["data"]:
                    data += '''
        assert_that({}).is_true()
        '''.format(vv)
            elif v == "json_schema":
                data += '''
        logging.info("jsonschema文件path:../data/jsonschema/{}")
        with open("../data/jsonschema/{}", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        '''.format(self.success_check["json_schema"],
                   self.success_check["json_schema"])
        return data

    def error_assert_check_code(self, error_check_index):
        data = ""
        for v in self.error_check[error_check_index]:
            if v == "check_type":
                data += '''
        assert_that(baseTest.is_{}(resp.text)).is_equal_to(True)
        '''.format(self.error_check[error_check_index]["check_type"])
            elif v == "expected_code":
                data += '''
        assert_that(resp.status_code).is_equal_to({})
        '''.format(self.error_check[error_check_index]["expected_code"])
            elif v == "code":
                data += '''
        assert_that(resp.json()["code"]).is_equal_to({})
        '''.format(self.error_check[error_check_index]["code"])
            elif v == "msg":
                z_msg = self.error_check[error_check_index]["msg"]["z_message"]
                e_msg = self.error_check[error_check_index]["msg"]["e_message"]
                t_msg = self.error_check[error_check_index]["msg"]["t_message"]
                data_key = self.error_check[error_check_index]["msg"]["data_key"]
                headers_language = self.error_check[error_check_index]["msg"]["headers_language"]
                data += '''
        if "zh" in headers["{}"].lower():
            assert_that(resp.json()["{}"]).is_equal_to("{}")
        elif "th" in headers["{}"].lower():
            assert_that(resp.json()["{}"]).is_equal_to("{}")
        elif "en" in headers["{}"].lower():
            assert_that(resp.json()["{}"]).is_equal_to("{}")
        '''.format(headers_language, data_key, z_msg,
                   headers_language, data_key, t_msg,
                   headers_language, data_key, e_msg)
            elif v == "data":
                for vv in v["data"]:
                    data += '''
        assert_that({}).is_true()
        '''.format(vv)
            elif v == "json_schema":
                data += '''
        logging.info("jsonschema文件path:{}")
        with open("{}", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        '''.format(self.error_check[error_check_index]["json_schema"],
                   self.error_check[error_check_index]["json_schema"])
        return data


class CaseYamlParser(ConfigParser):
    """测试用例数据解析器"""

    def __init__(self, path, **kwargs):
        self.root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app//")
        self.yaml_path = os.path.join(self.root_path, path)
        self.mode = True if kwargs.get("mode") else False
        self.mode_head_parameter = kwargs.get("mode_head_parameter") if kwargs.get("mode_head_parameter") else 0

        BaseYamlParser.__init__(self, self.yaml_path)

    def extend(self, extend_path):
        extend_yaml_path = os.path.join(self.root_path, self.case_data, extend_path)
        return BaseYamlParser(extend_yaml_path).to_json

    def create_filev1(self, test_case):
        start_time = time.perf_counter()
        for v in test_case:
            code_msg = ""
            extend = self.extend(v["extend"])
            # print(extend)
            code_obj = CaseCodeTemplate(test_case = v, extend_test_case = extend, mode = self.mode,
                                        mode_head_parameter = self.mode_head_parameter,
                                        test_case_len = len(self.test_case))
            import_code = code_obj.import_code
            class_code = code_obj.class_code
            parametrize_header_code = code_obj.parametrize_header_code
            parametrize_address_code = code_obj.parametrize_address_code
            body_parameter_code = code_obj.body_parameter_code
            body_url_code = code_obj.body_url_code
            body_request_type_code = code_obj.body_request_type_code
            if extend["success"]:
                success_def_code = code_obj.success_def_code
                success_parametrize_parameter_code = code_obj.success_parametrize_parameter_code
                body_relevance_code = code_obj.body_relevance_code
                assert_success_check_code = code_obj.success_assert_check_code
                success_body_header_code = code_obj.success_body_header_code
                success_body_address_code = code_obj.success_body_address_code

                code_msg += "" \
                            + import_code \
                            + class_code \
                            + success_parametrize_parameter_code \
                            + parametrize_header_code \
                            + parametrize_address_code \
                            + success_def_code \
                            + body_parameter_code \
                            + success_body_header_code \
                            + success_body_address_code \
                            + body_url_code \
                            + body_request_type_code \
                            + body_relevance_code \
                            + assert_success_check_code
            if extend["error"]:
                for vv in extend["error"]["parameter"]:
                    code_obj.error_parameter_index = vv
                    error_def_code = code_obj.error_def_code
                    error_parametrize_parameter_code = code_obj.error_parametrize_parameter_code(vv)
                    error_body_parameter_code = code_obj.error_body_parameter_code
                    error_assert_check_code = code_obj.error_assert_check_code(vv)
                    error_body_header_code = code_obj.error_body_header_code
                    code_msg += "" \
                                + error_parametrize_parameter_code \
                                + parametrize_header_code \
                                + parametrize_address_code \
                                + error_def_code \
                                + error_body_parameter_code \
                                + error_body_header_code \
                                + body_url_code \
                                + body_request_type_code \
                                + error_assert_check_code
            file_name = "test_" + str(code_obj.case_id) + "_" + str(code_obj.test_name) + "_cache_test.py"
            file_path = self.root_path + "/" + self.case_path + file_name
            f = open(file_path, "w+", encoding = "utf-8")
            f.truncate()
            f.write(code_msg)
            f.close()
            print(file_path, "successfully created")
            stop_time = time.perf_counter()
            cost = stop_time - start_time
            print("共创建文件：", len(test_case), ";共耗时：", cost)

    def remove_file(self, path, key):
        """删除目录下指定的文件"""
        files = os.listdir(path)  # 导入该目录下所有文件名

        for f in files:
            if key in f:
                if os.path.exists(path + f):  # 如果文件存在
                    # 删除文件，可使用以下两种方法。
                    os.remove(path + f)
                    # os.unlink(path)

    def run(self, **kwargs):
        if self.mode == False:
            self.remove_file(self.root_path + "/" + self.case_path, "_cache_test")

        start_time = time.perf_counter()
        test_case = self.test_case
        test_case_len = len(test_case)
        i = 0
        _a = []
        _b = []
        _c = []
        while i < test_case_len:
            if i < math.ceil(test_case_len / 3):
                _a.append(test_case[i])
            elif i >= math.ceil(test_case_len / 3) and i < (
                    math.ceil(test_case_len / 3) + math.ceil(test_case_len / 3)):
                _b.append(test_case[i])
            else:
                _c.append(test_case[i])
            i = i + 1
        a = Process(target = self.create_filev1, args = (_a,))
        a.start()
        b = Process(target = self.create_filev1, args = (_b,))
        b.start()
        c = Process(target = self.create_filev1, args = (_c,))
        c.start()
        stop_time = time.perf_counter()
        cost = stop_time - start_time
        print("共创建文件：", len(test_case), ";共耗时：", cost)


if __name__ == '__main__':
    start_time = time.perf_counter()
    CaseYamlParser("backyard/overtime_car/data/overtime_car_bilateral.yaml").run()
    # CaseYamlParser("flash_identification/indentification/data/indentification.yaml").run()
    # CaseYamlParser("official_website/shipping/data/shipping.yaml", mode_head_parameter = 0, mode = True).run()
    # CaseYamlParser("app/me/data/master_me.yaml").run()
    # CaseYamlParser("Kit\my_public_funds\data\master_my_public_funds_lists.yaml").run()
    # CaseYamlParser("Kit\search\data\master_search.yaml").run()
    # CaseYamlParser("Kit\change_order_printing\data\master_change_order_printing.yaml").run()
    # CaseYamlParser("Kit\package_operation\data\master_package_operation.yaml").run()
    # CaseYamlParser("Kit\headless_upload\data\master_headless_upload.yaml").run()
    # CaseYamlParser("Kit\warehousing_operation\data\master_warehousing_operation.yaml").run()
    # CaseYamlParser("Kit\Storekeeper\data\kit.yaml").run()
    # CaseYamlParser("flash_identification/indentification/data_new/indentification.yaml").run()
