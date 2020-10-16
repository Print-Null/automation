
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
import configparser
from common.base import BaseTestCase
from utils.redisbase import RedisBase
from jsonschema import validate
from common.readconfig import ReadConfig
logging.basicConfig(level=logging.INFO)
cf = configparser.ConfigParser()


@allure.feature('kit-重置数据')
class Test_kit_auth_new_device_login(object):

    @pytest.mark.run(order=1)
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
        # # 仓管员
        # warehouse_keeper_login = readConfigObj.get_config(env, "warehouse_keeper_login")
        ## 揽件网点经理
        p_outlet_manager_login = readConfigObj.get_config(env, "p_outlet_manager_login")
        # 疑难件提交网点经理
        c_outlet_manager_login = readConfigObj.get_config(env, "c_outlet_manager_login")

        # ms-host地址
        ms_host = readConfigObj.get_config(env, "ms_host")
        # 10000登录ms
        url_login = "{0}ms/api/auth/signin".format(ms_host)
        data_login = {"login": "{0}".format(super_administrator_login),"password": "{0}".format(super_administrator_pwd)}
        headers_login = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN"}
        res_login = requests.post(url=url_login, json=data_login, headers=headers_login,verify=False)
        #ms环境下10000登录以后的headers
        headers = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN","X-MS-SESSION-ID": res_login.json()["data"]["session_id"]}
        if env == "trunk":
            # 快递员
            RedisBase().set('my_public_funds_courier_login',22750,ex=10800)
            # 仓管员
            RedisBase().set('warehouse_keeper_login', 22751, ex=10800)
            print("{0}环境存入redis成功".format(env))
            #从redis里读取快递员id
            my_public_funds_courier_login =  RedisBase().get('my_public_funds_courier_login')
            warehouse_keeper_login = RedisBase().get('warehouse_keeper_login')

            test_data = [{"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host,my_public_funds_courier_login),"data": {"id": '{0}'.format(my_public_funds_courier_login), "company_name": "", "name": "yr-快递员","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "","positions_text": "快递员", "administrative_area": "นนทบุรี บางใหญ่","mobile": "1871007048", "mobile_company": "6352635263", "email": "", "state": 1,"state_text": "在职", "hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "","job_title_name": "", "vehicle": 1, "vehicle_text": "Van", "formal": 1,"formal_text": "编制","formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},{"code": 3, "text": "停职"}], "positions": [1],"position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"},{"code": 40, "text": "加班车申请员"}]}},
                         {"url": '{0}/ms/api/setting/store/staffs/{1}/edit'.format(ms_host, warehouse_keeper_login),"data": {"id": '{0}'.format(warehouse_keeper_login), "company_name": "", "name": "yr-仓管员","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "","positions_text": "仓管", "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007049","mobile_company": "6352635264", "email": "", "state": 1, "state_text": "在职","hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "","job_title_name": "", "vehicle": "", "vehicle_text": "", "formal": 1,"formal_text": "编制","formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},{"code": 3, "text": "停职"}], "positions": [2],"position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"},{"code": 40, "text": "加班车申请员"}]}},
                         {"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, p_outlet_manager_login),"data": {"id": '{0}'.format(p_outlet_manager_login), "company_name": "", "name": "yr-网点经理","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "","positions_text": "仓管", "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007049","mobile_company": "6352635264", "email": "", "state": 1, "state_text": "在职","hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "","job_title_name": "", "vehicle": "", "vehicle_text": "", "formal": 1,"formal_text": "编制","formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},{"code": 3, "text": "停职"}], "positions": [3],"position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"},{"code": 40, "text": "加班车申请员"}]}},
                         {"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, c_outlet_manager_login),"data": {"id": '{0}'.format(c_outlet_manager_login), "company_name": "", "name": "yr-网点经理","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "","positions_text": "仓管", "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007049","mobile_company": "6352635264", "email": "", "state": 1, "state_text": "在职","hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "","job_title_name": "", "vehicle": "", "vehicle_text": "", "formal": 1,"formal_text": "编制","formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},{"code": 3, "text": "停职"}], "positions": [3],"position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"},{"code": 40, "text": "加班车申请员"}]}}]
            for item in test_data:
                res = requests.post(url=item["url"], json=item['data'], headers=headers, verify=False)
                try:
                    assert res.json()['code'] == 1
                    print("重置账号{0}角色成功".format(item['data']['id']))
                except Exception as e:
                    print("重置账号{0}角色失败".format(item['data']['id']))
                    print("错误信息是：{0}".format(e))
                    raise e
            # 重置密码
            id = [my_public_funds_courier_login, warehouse_keeper_login, p_outlet_manager_login,c_outlet_manager_login]
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

        elif env=="training":
            #除了我的公款，别的用例对快递员数据要求不那么高，如果redis里已经存在，可以用redis里的，只有我的公款需要重新新建快递员
            if  RedisBase().exists('my_public_funds_courier_login'):
                my_public_funds_courier_login = RedisBase().get('my_public_funds_courier_login')
                print("不需要新建快递员，本次的快递员是：{0}".format(my_public_funds_courier_login))
            else:
                #training环境需要新建快递员角色的账号
                url_kdy="{0}ms/api/setting/store/staffs/".format(ms_host)
                data_kdy={"name":"yr快递员","mobile":"1451451464","mobile_company":"","positions":[1],"email":"","formal":1,"state":1,"organization_id":"TH01010101","hire_date":"2020-07-13","leave_date":"","company_name":"","vehicle":1}
                res_kdy=requests.post(url=url_kdy,json=data_kdy,headers=headers,verify=False)
                try:
                    assert res_kdy.json()["message"]=="success"
                    #查询快递员的id  -Testing北京团队-取最新的id
                    url_cx="{0}ms/api/setting/store/staffs?state=1&id=&positionCategory=1&pageSize=100&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&formal=1&organizationId=TH01010101".format(ms_host)
                    res_cx = requests.get(url=url_cx, headers=headers,verify=False)
                    my_public_funds_courier_login=res_cx.json()['data']['items'][-1]['id']
                    print("{0}环境新建快递员角色{1}成功".format(env,my_public_funds_courier_login))
                    #将新建的快递员id存入redis里
                    RedisBase().set('my_public_funds_courier_login', my_public_funds_courier_login, ex=6000)
                    print("{0}环境存入redis成功".format(env))
                    # 从redis里读取快递员id
                    my_public_funds_courier_login = RedisBase().get('my_public_funds_courier_login')
                except Exception as e:
                    print("{0}环境新建快递员角色失败".format(env))
                    raise e

            # 除了我的公款，别的用例对仓管员数据要求不那么高，如果redis里已经存在，可以用redis里的，只有我的公款需要重新新建快递员
            if RedisBase().exists('warehouse_keeper_login'):
                warehouse_keeper_login = RedisBase().get('warehouse_keeper_login')
                print("不需要新建仓管员，本次的仓管员是：{0}".format(warehouse_keeper_login))
            else:
                # training环境需要新建仓管员角色的账号
                url_kdy = "{0}ms/api/setting/store/staffs/".format(ms_host)
                data_kdy = {"name": "yr仓管员", "mobile": "1451451465", "mobile_company": "", "positions": [2],
                            "email": "", "formal": 1, "state": 1, "organization_id": "TH01010101",
                            "hire_date": "2020-07-13", "leave_date": "", "company_name": "", "vehicle": ""}
                res_kdy = requests.post(url=url_kdy, json=data_kdy, headers=headers, verify=False)
                try:
                    assert res_kdy.json()["message"] == "success"
                    # 查询快递员的id  -Testing北京团队-取最新的id
                    url_cx = "{0}ms/api/setting/store/staffs?state=1&id=&positionCategory=2&pageSize=100&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&formal=1&organizationId=TH01010101".format(
                        ms_host)
                    res_cx = requests.get(url=url_cx, headers=headers, verify=False)
                    print(res_cx.json())
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

            #重置角色
            test_data=[{"url":'{0}/ms/api/setting/store/staffs/{1}/edit'.format(ms_host, warehouse_keeper_login),"data":{"id":'{0}'.format(warehouse_keeper_login),"company_name":"","name":"นางสาว กันย์ภิรมย์ สุคนธรัตน์","organization_name":"Testing（北京团队测试用）","organization_id":"TH01010101","organization_type":1,"department_id":"32","department_name":"Network Operations","positions_text":"仓管","administrative_area":"กรุงเทพ คลองเตย","mobile":"0954036726","mobile_company":"","email":"","state":1,"state_text":"在职","hire_date":"2020-07-04","leave_date":"","stop_duties_date":"","job_title_name":"DC Officer","vehicle":"","vehicle_text":"","formal":1,"formal_text":"编制","formal_list":[{"code":0,"text":"非编制"},{"code":1,"text":"编制"}],"state_list":[{"code":1,"text":"在职"},{"code":2,"text":"离职"},{"code":3,"text":"停职"}],"positions":[2],"position_category_list":[{"code":1,"text":"快递员"},{"code":2,"text":"仓管"},{"code":3,"text":"网点经理"},{"code":4,"text":"网点出纳"},{"code":0,"text":"分配员"},{"code":18,"text":"网点主管"},{"code":21,"text":"区域经理"},{"code":40,"text":"加班车申请员"}]}}]
            for item in test_data:
                res=requests.post(url=item["url"],json=item['data'],headers=headers,verify=False)
                try:
                    assert res.json()['code']==1
                    print("重置账号{0}角色成功".format(item['data']['id']))
                except Exception as e:
                    print("重置账号{0}角色失败".format(item['data']['id']))
                    print("错误信息是：{0}".format(e))
                    raise e

            # 重置密码
            id=[my_public_funds_courier_login,warehouse_keeper_login,p_outlet_manager_login,c_outlet_manager_login]
            for item in id:
                url_id="{0}ms/api/setting/store/staffs/{1}/reset_password".format(ms_host,item)
                res=requests.post(url=url_id, headers=headers, verify=False)
                try:
                    assert res.json()['code'] == 1
                    print("重置账号{0}密码成功".format(item))
                except Exception as e:
                    print("重置账号{0}密码失败".format(item))
                    print("错误信息是：{0}".format(e))
                    raise e