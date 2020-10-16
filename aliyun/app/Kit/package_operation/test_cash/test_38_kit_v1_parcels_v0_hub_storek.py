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
from common.base import BaseTestCase
from utils.redisbase import RedisBase
from jsonschema import validate
from common.readconfig import ReadConfig

logging.basicConfig(level=logging.INFO)


@allure.feature('查询10110hub的快递员id')
class Test_kit_v1_parcels_v0(object):

    @pytest.mark.run(order=38)
    def test_test_kit_v1_parcels_v0(self):
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

        # ms-host地址
        ms_host = readConfigObj.get_config(env, "ms_host")
        kit_host = readConfigObj.get_config(env, "kit_host")

        # 10000登录ms
        url_login = "{0}ms/api/auth/signin".format(ms_host)
        data_login = {"login": "{0}".format(super_administrator_login),
                      "password": "{0}".format(super_administrator_pwd)}
        headers_login = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN"}
        res_login = requests.post(url=url_login, json=data_login, headers=headers_login, verify=False)
        # ms环境下10000登录以后的headers
        headers = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN",
                   "X-MS-SESSION-ID": res_login.json()["data"]["session_id"]}
        my_public_funds_courier_login = RedisBase().get('my_public_funds_courier_login')
        # 查询快递员所在的组织机构
        url_cx_kdygv = "{0}ms/api/setting/store/staffs?id={1}&pageSize=20&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&formal=&organizationId=".format(
            ms_host, my_public_funds_courier_login)
        res_cx_kdygv = requests.get(url=url_cx_kdygv, headers=headers,verify=False)

        organization_name = res_cx_kdygv.json()["data"]["items"][0]["organization_name"]
        organization_id = res_cx_kdygv.json()["data"]["items"][0]["organization_id"]

        # 查询上级网点
        url_upper = "{0}ms/api/setting/store/manager?storeName={1}&pageSize=20&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&startTime=&endTime=&sortingNo=".format(
            ms_host, organization_name)
        res_upper = requests.get(url=url_upper, headers=headers,verify=False)
        parent_store_id = res_upper.json()["data"]["items"][0]["parent_store_id"]
        #判断是否有分管机构
        if parent_store_id == None:
            logging.info("需要新增分管机构")
            # 需要修改网点信息，添加上级网点
            url_1 = "{0}ms/api/setting/store/manager/{1}".format(ms_host,organization_id)
            data_1 = {"id": "{0}".format(organization_id), "ancestry": "", "category": 2, "category_text": "DC", "pickup_range_category": "",
                      "pickup_range_category_text": "", "client_grade": 104,
                      "client_grade_text": "B-C-zone Standard price", "parent_store_id": "TH01470301",
                      "parent_name": "", "short_name": "CNCN", "area_name": "กรุงเทพคลองเตยคลองตัน",
                      "name": "Testing（北京团队测试用）", "phone": "0647722752", "difficult_phone_first": "001122334455",
                      "difficult_phone_second": "001122334455", "country_code": "", "country_name": "Thailand",
                      "province_code": "", "province_name": "กรุงเทพ", "city_code": "", "city_name": "คลองเตย",
                      "district_code": "TH010101", "district_name": "คลองตัน", "postal_code": "",
                      "detail_address": "Beijing,China", "manager_id": "90037", "manager_name": "zengyongle(testSMS)",
                      "manager_phone": "0950214066", "lat": 40.030574, "lng": 116.4103921, "franchisee_id": "",
                      "franchisee_name": "", "sorting_code": "", "sorting_code_text": "",
                      "created_at": "2018-10-11 17:14:13", "created_at_text": "2018-10-11", "cut_time": "",
                      "cut_time_text": "", "sorting_category": 1, "sorting_no": "B", "manage_region": "1",
                      "manage_piece": "1", "manage_region_name": "", "manage_piece_name": "", "zone": "",
                      "pack_category": 2, "pack_category_text": "按拆包网点", "sorting_line": "", "hub_no": "01",
                      "store_no": "169", "sorting_hub_code": "", "delivery_frequency": 2,
                      "delivery_frequency_text": "", "frequency_enabled": "true", "sap_pc_code": "",
                      "show_pc_code": "false", "week_start": "", "week_end": "", "time_start": "", "time_end": "",
                      "dst_division": "กรุงเทพ คลองเตย คลองตัน null"}
            res_parent_store=requests.post(url=url_1,json=data_1,headers=headers,verify=False)
            logging.info(res_parent_store.json())
            parent_store_id=data_1["parent_store_id"]
        else:
            parent_store_id=res_upper.json()["data"]["items"][0]["parent_store_id"]
        # logging.info("分管机构id是")
        # logging.info(parent_store_id)

        # 查询hub下的仓管员
        cx_cgy_url = "{0}ms/api/setting/store/staffs?state=1&positionCategory=2&pageSize=20&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&formal=1&organizationId={1}".format(
            ms_host, parent_store_id)
        cx_cgy_res = requests.get(url=cx_cgy_url, headers=headers,verify=False)
        if cx_cgy_res.json()["data"]["pagination"]["total_count"] > 0:
            #代表有，就用，重置密码
            cx_cgy_id=cx_cgy_res.json()["data"]["items"][0]["id"]
        else:
            #新建仓管员
            # training环境需要新建仓管员角色的账号
            url_kdy = "{0}ms/api/setting/store/staffs/".format(ms_host)
            data_kdy = {"name": "yr仓管员", "mobile": "1871871871", "mobile_company": "", "positions": [2],
                        "email": "", "formal": 1, "state": 1, "organization_id": "{0}".format(parent_store_id),
                        "hire_date": "2020-07-13", "leave_date": "", "company_name": "", "vehicle": ""}
            res_kdy = requests.post(url=url_kdy, json=data_kdy, headers=headers, verify=False)
            try:
                assert res_kdy.json()["message"] == "success"
                # 查询快递员的id  -Testing北京团队-取最新的id
                url_cx = "{0}ms/api/setting/store/staffs?state=1&id=&positionCategory=2&pageSize=100&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&formal=1&organizationId={1}".format(
                    ms_host,parent_store_id)
                res_cx = requests.get(url=url_cx, headers=headers, verify=False)
                print(res_cx.json())
                cx_cgy_id = res_cx.json()['data']['items'][-1]['id']
                print("{0}环境新建仓管员角色{1}成功".format(env, cx_cgy_id))
                # 将新建的快递员id存入redis里
                RedisBase().set('warehouse_keeper_login_new', cx_cgy_id, ex=10800)
                print("{0}环境存入redis成功".format(env))
            except Exception as e:
                print("{0}环境新建仓管员角色失败".format(env))
                raise e

        logging.info("仓管员账号是：{0}".format(cx_cgy_id))

        id = [cx_cgy_id]
        for item in id:
            url_id = "{0}ms/api/setting/store/staffs/{1}/reset_password".format(ms_host, item)
            res = requests.post(url=url_id, headers=headers, verify=False)
            try:
                assert res.json()['code'] == 1
                print("重置账号{0}密码成功".format(item))
            except Exception as e:
                print("重置账号{0}密码失败".format(item))
                print("错误信息是：{0}".format(e))
                raise e

        #登录，存储session_id到redis，后面的集包直接用redis就好
        login_url="{0}api/courier/v1/auth/new_device_login".format(kit_host)
        login_data={"login": "{0}".format(cx_cgy_id), "password": 123456, "clientid": 15924814012781592481401278, "clientsd": 1592481401284, "os": "android", "version": "3.8.4"}
        login_headers={"content-type": "application/json; charset=UTF-8","Accept-Language": "zh-CN"}
        cgy_session_id=requests.post(url=login_url,json=login_data,headers=login_headers, verify=False).json()["data"]["sessionid"]
        RedisBase().set("cgy_session_id",cgy_session_id,ex=10800)
