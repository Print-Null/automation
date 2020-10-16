import sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0] + "/flash")

import allure
from assertpy import assert_that
import requests
import logging
import ast
import json
import time
import pytest
import configparser
from common.base import BaseTestCase
from utils.redisbase import RedisBase
from jsonschema import validate
from common.readconfig import ReadConfig

logging.basicConfig(level=logging.INFO)
cf = configparser.ConfigParser()


@allure.feature('kit-重置数据')
class Test_kit_auth_new_device_login(object):

    @pytest.mark.run(order=0)
    def test_restet_datas(self):
        print("开始执行用例重置账号操作")
        redisObj = RedisBase()
        readConfigObj = ReadConfig()
        env = redisObj.get("runenv_py")
        if env == False or env == "trunk":
            env = "trunk"
        elif env == "training":
            env = "training"
        print("当前环境是：{0}".format(env))
        # 超级管理员
        super_administrator_login = readConfigObj.get_config(env, "ms_houtai_login_user")
        super_administrator_pwd = readConfigObj.get_config(env, "ms_houtai_login_pwd")

        ## 揽件网点经理
        p_outlet_manager_login = readConfigObj.get_config(env, "p_outlet_manager_login")
        # 疑难件提交网点经理
        c_outlet_manager_login = readConfigObj.get_config(env, "c_outlet_manager_login")

        # 网点出纳
        finance_pwd = readConfigObj.get_config(env, "finance_pwd")

        # ms-host地址
        ms_host = readConfigObj.get_config(env, "ms_host")

        # 寄件人手机号
        send_phone = readConfigObj.get_config(env, "send_phone")
        # 寄件人姓名
        send_name = readConfigObj.get_config(env, "send_name")
        # 寄件人编码
        send_id = readConfigObj.get_config(env, "send_id")

        # 10000登录ms
        url_login = "{0}ms/api/auth/signin".format(ms_host)
        data_login = {"login": "{0}".format(super_administrator_login),
                      "password": "{0}".format(super_administrator_pwd)}
        headers_login = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN"}
        res_login = requests.post(url=url_login, json=data_login, headers=headers_login, verify=False)
        print("10000登录ms的结果是：{0}".format(res_login.json()))
        # ms环境下10000登录以后的headers
        headers = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN",
                   "X-MS-SESSION-ID": res_login.json()["data"]["session_id"]}

        if env == "trunk":

            # 快递员
            RedisBase().set('my_public_funds_courier_login', 22750, ex=10800)
            # 仓管员
            RedisBase().set('warehouse_keeper_login', 22751, ex=10800)
            # 财务出纳
            RedisBase().set('finance_login', 22753, ex=10800)

            # 从redis里读取快递员id
            my_public_funds_courier_login = RedisBase().get('my_public_funds_courier_login')
            warehouse_keeper_login = RedisBase().get('warehouse_keeper_login')
            finance_login = RedisBase().get('finance_login')

            print("{0}环境快递员{1}存入redis成功".format(env, my_public_funds_courier_login))
            print("{0}环境仓管员{1}存入redis成功".format(env, warehouse_keeper_login))
            print("{0}环境财务出纳{1}存入redis成功".format(env, finance_login))

            # 测试数据
            test_data = [
                {"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, my_public_funds_courier_login),
                 "data": {"id": '{0}'.format(my_public_funds_courier_login), "company_name": "", "name": "yr-快递员",
                          "organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302",
                          "organization_type": 1, "department_id": "", "department_name": "", "positions_text": "快递员",
                          "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007048",
                          "mobile_company": "6352635263", "email": "", "state": 1, "state_text": "在职",
                          "hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "", "job_title_name": "",
                          "vehicle": 1, "vehicle_text": "Van", "formal": 1, "formal_text": "编制",
                          "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],
                          "state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},
                                         {"code": 3, "text": "停职"}], "positions": [1],
                          "position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},
                                                     {"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},
                                                     {"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},
                                                     {"code": 21, "text": "区域经理"}, {"code": 40, "text": "加班车申请员"}]}},
                {"url": '{0}/ms/api/setting/store/staffs/{1}/edit'.format(ms_host, warehouse_keeper_login),
                 "data": {"id": '{0}'.format(warehouse_keeper_login), "company_name": "", "name": "yr-仓管员",
                          "organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302",
                          "organization_type": 1, "department_id": "", "department_name": "", "positions_text": "仓管",
                          "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007049",
                          "mobile_company": "6352635264", "email": "", "state": 1, "state_text": "在职",
                          "hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "", "job_title_name": "",
                          "vehicle": "", "vehicle_text": "", "formal": 1, "formal_text": "编制",
                          "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],
                          "state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},
                                         {"code": 3, "text": "停职"}], "positions": [2],
                          "position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},
                                                     {"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},
                                                     {"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},
                                                     {"code": 21, "text": "区域经理"}, {"code": 40, "text": "加班车申请员"}]}},
                {"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, p_outlet_manager_login),
                 "data": {"id": '{0}'.format(p_outlet_manager_login), "company_name": "", "name": "yr-网点经理",
                          "organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302",
                          "organization_type": 1, "department_id": "", "department_name": "", "positions_text": "仓管",
                          "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007049",
                          "mobile_company": "6352635264", "email": "", "state": 1, "state_text": "在职",
                          "hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "", "job_title_name": "",
                          "vehicle": "", "vehicle_text": "", "formal": 1, "formal_text": "编制",
                          "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],
                          "state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},
                                         {"code": 3, "text": "停职"}], "positions": [3],
                          "position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},
                                                     {"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},
                                                     {"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},
                                                     {"code": 21, "text": "区域经理"}, {"code": 40, "text": "加班车申请员"}]}},
                {"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, c_outlet_manager_login),
                 "data": {"id": '{0}'.format(c_outlet_manager_login), "company_name": "", "name": "yr-网点经理",
                          "organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302",
                          "organization_type": 1, "department_id": "", "department_name": "", "positions_text": "仓管",
                          "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007049",
                          "mobile_company": "6352635264", "email": "", "state": 1, "state_text": "在职",
                          "hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "", "job_title_name": "",
                          "vehicle": "", "vehicle_text": "", "formal": 1, "formal_text": "编制",
                          "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],
                          "state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},
                                         {"code": 3, "text": "停职"}], "positions": [3],
                          "position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},
                                                     {"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},
                                                     {"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},
                                                     {"code": 21, "text": "区域经理"}, {"code": 40, "text": "加班车申请员"}]}},
                {"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, finance_login),
                 "data": {"id": '{0}'.format(finance_login), "company_name": "", "name": "yr-网点出纳",
                          "organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302",
                          "organization_type": 1, "department_id": "", "department_name": "", "positions_text": "网点出纳",
                          "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007046",
                          "mobile_company": "6352635265", "email": "", "state": 1, "state_text": "在职",
                          "hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "", "job_title_name": "",
                          "vehicle": 1, "vehicle_text": "Van", "formal": 1, "formal_text": "编制",
                          "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],
                          "state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},
                                         {"code": 3, "text": "停职"}], "positions": [4],
                          "position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},
                                                     {"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},
                                                     {"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},
                                                     {"code": 21, "text": "区域经理"}, {"code": 40, "text": "加班车申请员"}]}}]

            # 重置角色
            for item in test_data:
                res = requests.post(url=item["url"], json=item['data'], headers=headers, verify=False)
                print("重置账号{0}角色结果是：{1}".format(item['data']['id'], res.json()))
                try:
                    assert res.json()['code'] == 1
                    print("重置账号{0}角色成功".format(item['data']['id']))
                except Exception as e:
                    print("重置账号{0}角色失败".format(item['data']['id']))
                    print("错误信息是：{0}".format(e))
                    raise e

            # 重置密码
            id = [my_public_funds_courier_login, warehouse_keeper_login, p_outlet_manager_login, c_outlet_manager_login,
                  finance_login]
            for item in id:
                url_id = "{0}ms/api/setting/store/staffs/{1}/reset_password".format(ms_host, item)
                res = requests.post(url=url_id, headers=headers, verify=False)
                print("重置账号{0}密码的结果是：{1}".format(item['data']['id'], res.json()))
                try:
                    assert res.json()['code'] == 1
                    print("重置账号{0}密码成功".format(item))
                except Exception as e:
                    print("重置账号{0}密码失败".format(item))
                    print("错误信息是：{0}".format(e))
                    raise e

            # 重置寄件人信息为现金结算方式
            url_customer_2 = "{0}ms/api/setting/custmor/{1}/update_account".format(ms_host, send_id)
            data_customer_2 = {"major_mobile": "1341341341", "email": "123@123.com"}
            res_customer_2 = requests.post(url=url_customer_2, json=data_customer_2, headers=headers)
            print("重置{0}环境寄件人信息{1}的结果是：{2}".format(env, send_phone, res_customer_2.json()))
            try:
                assert res_customer_2.json()["code"] == 1
                print("重置{0}环境寄件人信息{1}成功".format(env, send_phone))
            except Exception as e:
                print("重置寄件人信息失败，报错信息是：{0}".format(e))
                raise e

        elif env == "training":
            # training环境需要新建快递员角色的账号
            url_kdy = "{0}ms/api/setting/store/staffs/".format(ms_host)
            data_kdy = {"name": "yr快递员", "mobile": "1451451464", "mobile_company": "", "positions": [1], "email": "",
                        "formal": 1, "state": 1, "organization_id": "TH01010101", "hire_date": "2020-07-13",
                        "leave_date": "", "company_name": "", "vehicle": 1}
            res_kdy = requests.post(url=url_kdy, json=data_kdy, headers=headers, verify=False)
            print("{0}环境新建快递员角色的结果是：{1}".format(env, res_kdy.json()))
            try:
                assert res_kdy.json()["message"] == "success"
                # 查询快递员的id  -Testing北京团队-取最新的id
                url_cx = "{0}ms/api/setting/store/staffs?state=1&id=&positionCategory=1&pageSize=100&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&formal=1&organizationId=TH01010101".format(
                    ms_host)
                res_cx = requests.get(url=url_cx, headers=headers, verify=False)
                print("查询新建快递员id的结果是：{0}".format(res_cx.json()))
                my_public_funds_courier_login = res_cx.json()['data']['items'][-1]['id']
                print("{0}环境新建快递员角色{1}成功".format(env, my_public_funds_courier_login))
                # 将新建的快递员id存入redis里
                RedisBase().set('my_public_funds_courier_login', my_public_funds_courier_login, ex=10800)
                print("{0}环境存入redis成功".format(env))
                # 从redis里读取快递员id
                my_public_funds_courier_login = RedisBase().get('my_public_funds_courier_login')
            except Exception as e:
                print("{0}环境新建快递员角色失败".format(env))
                raise e

            # training环境需要新建仓管员角色的账号
            url_kdy = "{0}ms/api/setting/store/staffs/".format(ms_host)
            data_kdy = {"name": "yr仓管员", "mobile": "1451451465", "mobile_company": "", "positions": [2], "email": "",
                        "formal": 1, "state": 1, "organization_id": "TH01010101", "hire_date": "2020-07-13",
                        "leave_date": "", "company_name": "", "vehicle": ""}
            res_kdy = requests.post(url=url_kdy, json=data_kdy, headers=headers, verify=False)
            print("{0}环境新建仓管员角色的结果是：{1}".format(env, res_kdy.json()))
            try:
                assert res_kdy.json()["message"] == "success"
                # 查询快递员的id  -Testing北京团队-取最新的id
                url_cx = "{0}ms/api/setting/store/staffs?state=1&id=&positionCategory=2&pageSize=100&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&formal=1&organizationId=TH01010101".format(
                    ms_host)
                res_cx = requests.get(url=url_cx, headers=headers, verify=False)
                print("查询新建仓管员id的结果是：{0}".format(res_cx.json()))
                warehouse_keeper_login = res_cx.json()['data']['items'][-1]['id']
                print("{0}环境新建仓管员角色{1}成功".format(env, warehouse_keeper_login))
                # 将新建的快递员id存入redis里
                RedisBase().set('warehouse_keeper_login', warehouse_keeper_login, ex=10800)
                print("{0}环境存入redis成功".format(env))
                # 从redis里读取快递员id
                warehouse_keeper_login = RedisBase().get('warehouse_keeper_login')
            except Exception as e:
                print("{0}环境新建仓管员角色失败".format(env))
                raise e

            # 重置财务角色--一个网点不能有超过4位出纳-先判断有多少出纳
            url_fin_count = "{0}ms/api/setting/store/staffs?state=1&positionCategory=4&pageSize=20&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&formal=1&organizationId=TH01010101".format(
                ms_host)
            res_fin_count = requests.get(url=url_fin_count, headers=headers, verify=False)
            print("查询网点出纳的结果是：{0}".format(res_fin_count.json()))
            print("查询网点出纳的人数是：{0}".format(res_fin_count.json()["data"]["pagination"]["total_count"]))
            if 0 <= res_fin_count.json()["data"]["pagination"]["total_count"] < 4:  # 0123，可以重置
                # 可以根据配置文件的finace_login重置出纳角色
                finance_login = ReadConfig().get_config(env, "finance_login")
                test_data = [{"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, finance_login),
                              "data": {"id": '{0}'.format(finance_login), "company_name": "",
                                       "name": "นางสาว สุวภัทร ทองเถาว์", "organization_name": "Testing（北京团队测试用）",
                                       "organization_id": "TH01010101", "organization_type": 1, "department_id": "32",
                                       "department_name": "Network Operations", "positions_text": "网点出纳",
                                       "administrative_area": "กรุงเทพ คลองเตย", "mobile": "0614855889",
                                       "mobile_company": "", "email": "", "state": 1, "state_text": "在职",
                                       "hire_date": "2020-07-04", "leave_date": "", "stop_duties_date": "",
                                       "job_title_name": "DC Officer", "vehicle": "", "vehicle_text": "", "formal": 1,
                                       "formal_text": "编制",
                                       "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],
                                       "state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},
                                                      {"code": 3, "text": "停职"}], "positions": [4],
                                       "position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},
                                                                  {"code": 3, "text": "网点经理"},
                                                                  {"code": 4, "text": "网点出纳"},
                                                                  {"code": 0, "text": "分配员"},
                                                                  {"code": 18, "text": "网点主管"},
                                                                  {"code": 21, "text": "区域经理"},
                                                                  {"code": 40, "text": "加班车申请员"}]}}]
                for item in test_data:
                    res = requests.post(url=item["url"], json=item['data'], headers=headers, verify=False)
                    print("重置角色的结果是：{0}".format(res.json()))
                    try:
                        assert res.json()['code'] == 1
                        print("重置账号{0}角色成功".format(item['data']['id']))
                        RedisBase().set("finance_login", finance_login, ex=10800)
                    except Exception as e:
                        print("重置账号{0}角色失败".format(item['data']['id']))
                        print("错误信息是：{0}".format(e))
                        raise e
            elif res_fin_count.json()["data"]["pagination"]["total_count"] == 4:
                # 判断配置文件的finance_login是否在列表内
                for item in res_fin_count.json()["data"]["items"]:
                    if item["id"] == eval(ReadConfig().get_config(env, "finance_login")):
                        RedisBase().set("finance_login", ReadConfig().get_config(env, "finance_login"), ex=10800)
                        break
                    else:
                        # # 选择第一个作为出纳,存入redis
                        RedisBase().set("finance_login", res_fin_count.json()["data"]["items"][0]["id"], ex=10800)
                finance_login = RedisBase().get("finance_login")
            print("本次的网点出纳是：{0}".format(finance_login))

            # 重置角色
            test_data = [{"url": '{0}/ms/api/setting/store/staffs/{1}/edit'.format(ms_host, warehouse_keeper_login),
                          "data": {"id": '{0}'.format(warehouse_keeper_login), "company_name": "",
                                   "name": "นางสาว กันย์ภิรมย์ สุคนธรัตน์", "organization_name": "Testing（北京团队测试用）",
                                   "organization_id": "TH01010101", "organization_type": 1, "department_id": "32",
                                   "department_name": "Network Operations", "positions_text": "仓管",
                                   "administrative_area": "กรุงเทพ คลองเตย", "mobile": "0954036726",
                                   "mobile_company": "", "email": "", "state": 1, "state_text": "在职",
                                   "hire_date": "2020-07-04", "leave_date": "", "stop_duties_date": "",
                                   "job_title_name": "DC Officer", "vehicle": "", "vehicle_text": "", "formal": 1,
                                   "formal_text": "编制",
                                   "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],
                                   "state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},
                                                  {"code": 3, "text": "停职"}], "positions": [2],
                                   "position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},
                                                              {"code": 3, "text": "网点经理"},
                                                              {"code": 4, "text": "网点出纳"},
                                                              {"code": 0, "text": "分配员"},
                                                              {"code": 18, "text": "网点主管"},
                                                              {"code": 21, "text": "区域经理"},
                                                              {"code": 40, "text": "加班车申请员"}]}},
                         {"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, finance_login),
                          "data": {"id": '{0}'.format(finance_login), "company_name": "",
                                   "name": "นางสาว สุวภัทร ทองเถาว์", "organization_name": "Testing（北京团队测试用）",
                                   "organization_id": "TH01010101", "organization_type": 1, "department_id": "32",
                                   "department_name": "Network Operations", "positions_text": "网点出纳",
                                   "administrative_area": "กรุงเทพ คลองเตย", "mobile": "0614855889",
                                   "mobile_company": "", "email": "", "state": 1, "state_text": "在职",
                                   "hire_date": "2020-07-04", "leave_date": "", "stop_duties_date": "",
                                   "job_title_name": "DC Officer", "vehicle": "", "vehicle_text": "", "formal": 1,
                                   "formal_text": "编制",
                                   "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],
                                   "state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},
                                                  {"code": 3, "text": "停职"}], "positions": [4],
                                   "position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},
                                                              {"code": 3, "text": "网点经理"},
                                                              {"code": 4, "text": "网点出纳"},
                                                              {"code": 0, "text": "分配员"},
                                                              {"code": 18, "text": "网点主管"},
                                                              {"code": 21, "text": "区域经理"},
                                                              {"code": 40, "text": "加班车申请员"}]}}]
            for item in test_data:
                res = requests.post(url=item["url"], json=item['data'], headers=headers, verify=False)
                print("重置角色的结果是：{0}".format(res.json()))
                try:
                    assert res.json()['code'] == 1
                    print("重置账号{0}角色成功".format(item['data']['id']))
                except Exception as e:
                    print("重置账号{0}角色失败".format(item['data']['id']))
                    print("错误信息是：{0}".format(e))
                    raise e

            # 重置密码
            id = [my_public_funds_courier_login, warehouse_keeper_login, p_outlet_manager_login, c_outlet_manager_login,
                  finance_login]
            for item in id:
                url_id = "{0}ms/api/setting/store/staffs/{1}/reset_password".format(ms_host, item)
                res = requests.post(url=url_id, headers=headers, verify=False)
                print("重置密码的结果是：{0}".format(res.json()))
                try:
                    assert res.json()['code'] == 1
                    print("重置账号{0}密码成功".format(item))
                except Exception as e:
                    print("重置账号{0}密码失败".format(item))
                    print("错误信息是：{0}".format(e))
                    raise e

            # 重置寄件人信息为现金结算方式
            url_customer_2 = "{0}ms/api/setting/custmor/{1}/update_account".format(ms_host, send_id)
            data_customer_2 = {"major_mobile": "1341341341", "email": "936874337@qq.com"}
            res_customer_2 = requests.post(url=url_customer_2, json=data_customer_2, headers=headers, verify=False)
            print("重置寄件人信息为现金结算方式的结果是：{0}".format(res_customer_2.json()))
            try:
                if res_customer_2.json()["code"] == 1:
                    print("重置{0}环境寄件人信息{1}成功".format(env, send_phone))
            except Exception as e:
                print("重置寄件人信息失败，报错信息是：{0}".format(e))
                raise e

        # 处理ms的网点出纳问题---可能配置文件的网点的出纳不是当天的出纳
        url_cn = "{0}ms/api/auth/signin".format(ms_host)
        data_cn = {"login": "{0}".format(finance_login), "password": "{0}".format(finance_pwd)}
        headers_cn = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN"}
        res_cn = requests.post(url=url_cn, json=data_cn, headers=headers_cn, verify=False)
        print("网点出纳登录的结果是{0}".format(res_cn.json()))
        # 选择任意一条数据，处理回款
        url_hk_1 = "{0}ms/api/store/receivable_bill?closed=0&staffInfoId=&pageSize=20&pageNum=1&startTime=&endTime=".format(
            ms_host)
        headers_hk_1 = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN",
                        "X-MS-SESSION-ID": res_cn.json()["data"]["session_id"]}
        res_hk_1 = requests.get(url=url_hk_1, headers=headers_hk_1, verify=False)
        print("快递员回款菜单查询结果是：{0}".format(res_hk_1.json()))
        # 兼容一下没有回款数据的就不处理了
        if res_hk_1.json()["data"]["pagination"]["total_count"] > 0:
            url_hk_2 = "{0}ms/api/store/receivable_bill/{1}/exclude".format(ms_host,
                                                                            res_hk_1.json()["data"]["items"][0]["id"])
            data_hk_2 = {"exclude_ids": []}
            res_hk_2 = requests.post(url=url_hk_2, json=data_hk_2, headers=headers_hk_1, verify=False)
            print("快递员回款-详情结果：{0}".format(res_hk_2.json()))
            url_hk_3 = "{0}ms/api/store/receivable_bill/{1}".format(ms_host, res_hk_1.json()["data"]["items"][0]["id"])
            data_hk_3 = {"settlement_amount": res_hk_2.json()["data"]["bill_info"]["unpaid_amount"], "exclude_ids": []}
            res_hk_3 = requests.post(url=url_hk_3, json=data_hk_3, headers=headers_hk_1, verify=False)
            print("快递员回款-提交结果：{0}".format(res_hk_3.json()))
            if res_hk_3.json()["message"] == 1:
                print("重置当日网点出纳为{0}成功".format(finance_login))
            # 一个网点一天只能有一个出纳  message=您无此操作权限 ，一天限制1个出纳收款，当日的收款出纳是(55,129)นางสาว สุวภัทร ทองเถาว์
            elif res_hk_3.json()["code"] == 203201:
                print("重置当日网点出纳为{0}失败".format(finance_login))
                print(res_hk_3.json())
                # 存储提示语中的id作为finance_login
                finance_login = res_hk_3.json()["message"].split("(")[1].split(")")[0].replace(",", "")
                RedisBase().set("finance_login", finance_login, ex=10800)
                print("当天的网点出纳是：{0}".format(finance_login))
                #重置该网点出纳的密码
                # 重置密码
                id = [finance_login]
                for item in id:
                    url_id = "{0}ms/api/setting/store/staffs/{1}/reset_password".format(ms_host, item)
                    res = requests.post(url=url_id, headers=headers, verify=False)
                    print("重置密码的结果是：{0}".format(res.json()))
                    try:
                        assert res.json()['code'] == 1
                        print("重置账号{0}密码成功".format(item))
                    except Exception as e:
                        print("重置账号{0}密码失败".format(item))
                        print("错误信息是：{0}".format(e))
                        raise e
        else:
            print("没有待回款的数据处理")
