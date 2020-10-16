
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
        # # 网点出纳
        # finance_login = readConfigObj.get_config(env, "finance_login")
        finance_pwd = readConfigObj.get_config(env, "finance_pwd")

        # ms-host地址
        ms_host = readConfigObj.get_config(env, "ms_host")
        #寄件人手机号
        send_phone = readConfigObj.get_config(env,"send_phone")
        #寄件人姓名
        send_name = readConfigObj.get_config(env,"send_name")
        # 寄件人编码
        send_id = readConfigObj.get_config(env, "send_id")

        # 10000登录ms
        url_login = "{0}ms/api/auth/signin".format(ms_host)
        data_login = {"login": "{0}".format(super_administrator_login),
                      "password": "{0}".format(super_administrator_pwd)}
        headers_login = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN"}
        res_login = requests.post(url=url_login, json=data_login, headers=headers_login, verify=False)
        # ms环境下10000登录以后的headers
        headers = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN",
                   "X-MS-SESSION-ID": res_login.json()["data"]["session_id"]}

        # 重置寄件人信息为现金结算方式
        url_customer_2 = "{0}ms/api/setting/custmor/{1}/update_account".format(ms_host, send_id)
        data_customer_2 = {"major_mobile": "1341341341", "email": "123@123.com"}
        try:
            res_customer_2 = requests.post(url=url_customer_2, json=data_customer_2, headers=headers, verify=False)
            assert res_customer_2.json()["code"] == 1
            print("重置{0}环境寄件人信息{1}成功".format(env, send_phone))
        except Exception as e:
            print("重置寄件人信息失败，报错信息是：{0}".format(e))
            raise e

        if env == "trunk":
            RedisBase().set('finance_login', 22753, ex=10800)
            # 快递员
            RedisBase().set('my_public_funds_courier_login',22750,ex=10800)
            # 仓管员
            RedisBase().set('warehouse_keeper_login', 22751, ex=10800)
            print("{0}环境存入redis成功".format(env))
            #从redis里读取快递员id
            my_public_funds_courier_login =  RedisBase().get('my_public_funds_courier_login')
            warehouse_keeper_login = RedisBase().get('warehouse_keeper_login')
            finance_login = RedisBase().get('finance_login')

            test_data = [{"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host,my_public_funds_courier_login),"data": {"id": '{0}'.format(my_public_funds_courier_login), "company_name": "", "name": "yr-快递员","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "","positions_text": "快递员", "administrative_area": "นนทบุรี บางใหญ่","mobile": "1871007048", "mobile_company": "6352635263", "email": "", "state": 1,"state_text": "在职", "hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "","job_title_name": "", "vehicle": 1, "vehicle_text": "Van", "formal": 1,"formal_text": "编制","formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},{"code": 3, "text": "停职"}], "positions": [1],"position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"},{"code": 40, "text": "加班车申请员"}]}},
                         {"url": '{0}/ms/api/setting/store/staffs/{1}/edit'.format(ms_host, warehouse_keeper_login),"data": {"id": '{0}'.format(warehouse_keeper_login), "company_name": "", "name": "yr-仓管员","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "","positions_text": "仓管", "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007049","mobile_company": "6352635264", "email": "", "state": 1, "state_text": "在职","hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "","job_title_name": "", "vehicle": "", "vehicle_text": "", "formal": 1,"formal_text": "编制","formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},{"code": 3, "text": "停职"}], "positions": [2],"position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"},{"code": 40, "text": "加班车申请员"}]}},
                         {"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, p_outlet_manager_login),"data": {"id": '{0}'.format(p_outlet_manager_login), "company_name": "", "name": "yr-网点经理","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "","positions_text": "仓管", "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007049","mobile_company": "6352635264", "email": "", "state": 1, "state_text": "在职","hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "","job_title_name": "", "vehicle": "", "vehicle_text": "", "formal": 1,"formal_text": "编制","formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},{"code": 3, "text": "停职"}], "positions": [3],"position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"},{"code": 40, "text": "加班车申请员"}]}},
                         {"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, c_outlet_manager_login),"data": {"id": '{0}'.format(c_outlet_manager_login), "company_name": "", "name": "yr-网点经理","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "","positions_text": "仓管", "administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007049","mobile_company": "6352635264", "email": "", "state": 1, "state_text": "在职","hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "","job_title_name": "", "vehicle": "", "vehicle_text": "", "formal": 1,"formal_text": "编制","formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},{"code": 3, "text": "停职"}], "positions": [3],"position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"},{"code": 40, "text": "加班车申请员"}]}},
                         {"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, finance_login),"data": {"id": '{0}'.format(finance_login), "company_name": "", "name": "yr-网点出纳","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "","positions_text": "网点出纳", "administrative_area": "นนทบุรี บางใหญ่","mobile": "1871007046", "mobile_company": "6352635265", "email": "", "state": 1,"state_text": "在职", "hire_date": "2020-06-29", "leave_date": "", "stop_duties_date": "","job_title_name": "", "vehicle": 1, "vehicle_text": "Van", "formal": 1,"formal_text": "编制","formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},{"code": 3, "text": "停职"}], "positions": [4],"position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"},{"code": 40, "text": "加班车申请员"}]}}]
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
            id = [my_public_funds_courier_login, warehouse_keeper_login, p_outlet_manager_login,c_outlet_manager_login, finance_login]
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

            # 重置寄件人信息为现金结算方式
            url_customer_1 = "{0}/ms/api/setting/custmor?name=&pageSize=20&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&keyWord={1}&startTime=&endTime=".format(ms_host, send_phone)
            res = requests.get(url=url_customer_1, headers=headers)
            id = res.json()["data"]["items"][0]["id"]
            url_customer_2 = "{0}ms/api/setting/custmor/{1}".format(ms_host, id)
            data_customer_2={"id":"CA1100","name":"{0}".format(send_name),"email":"123@123.com","company_size_category":3,"company_size_category_text":"C (现金结算客户)","state":1,"state_text":"开通","authentication_type":1,"authentication_type_text":"企业","registered_address":"顶顶顶","registered_captial_investement":"1222123","tax_id":"9876543210111","authentication_phone":"3443455446","authentication_fax":"","bill_country_code":"TH","bill_country_name":"Thailand","bill_province_code":"TH01","bill_province_name":"กรุงเทพ","bill_city_code":"TH0101","bill_city_name":"คลองเตย","bill_district_code":"TH010101","bill_district_name":"คลองตัน","bill_postal_code":"10110","bill_address":"的地方","bill_contact_person":"43434234","bill_phone":"18012345689","bill_email":"234234@123.com","client_grade":999,"client_grade_text":"New Standard price","client_type_category":2,"client_type_category_text":"折扣价格","account_type_category":1,"account_type_category_text":"普通签约客户","cod_account_source":"","cod_account_source_text":"","discount_rate":1,"discount_limit_enabled":"false","return_category":0,"return_category_text":"费率","return_uniform_amount":"","return_discount_rate":1,"settlement_category":1,"settlement_category_text":"现场结算","settlement_cycle_text":"","month_account_date":"","weighing_category":0,"weighing_category_text":"按重量/尺寸","credit_term":10,"credit_limit":10000,"opened":"true","cod_settlement_category":0,"cod_settlement_category_text":"费率","cod_settlement_cycle":0,"cod_settlement_cycle_text":"日","cod_uniform_amount":"","opened_text":"开通","cod_poundage_rate_str":"2.50","cod_poundage_rate":25,"cod_poundage_minimum":0,"insure_rate":0,"staff_info_id":17105,"staff_info_name":"哎呀呀业务员2","sign_date_text":"2020-06-23","bank_code":1,"bank_name":"曼谷银行","account_holder":"dfsfd","bank_account_no":"36325241225212","major_mobile":"{0}".format(send_phone),"images":[],"images_text":"","ka_warehouses":[{"id":"5ef1b3d62d738a35fe43be5d","warehouse_no":"12345689","ka_id":"CA1100","ka_info_id":"CA1100","name":"www","country_name":"Thailand","country_code":"TH","province_name":"กรุงเทพ","province_code":"TH01","city_name":"คลองเตย","city_code":"TH0101","district_name":"คลองตัน","district_code":"TH010101","opened":"","postal_code":"10110","detail_address":"dfsdfe","lat":"","lng":"","phone":"18524125541","src_name":"dfdf","store_id":"","store_name":"","store_manager_id":"","store_manager_email":"","ntc_enabled":""}],"mobile":"","cod_enabled":"true","agent_id":None,"agent_name":"","sub_client_local_cpr":"","reject_return_strategy_category":2,"reject_return_strategy_category_text":"直接退回","remark":"","custmor_certificate_images":[{"id":"5ef1b3d62d738a35fe43be5c","name":"微信图片_20200623153909.jpg","object_key":"custmorCertificate/1592897963-dca4063bb0a842a987a2524430157b2f.jpg","object_url":"https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/custmorCertificate/1592897963-dca4063bb0a842a987a2524430157b2f.jpg","object_url_th":"https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/custmorCertificate/1592897963-dca4063bb0a842a987a2524430157b2f.jpg?x-oss-process=style/th","object_url_x3":"https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/custmorCertificate/1592897963-dca4063bb0a842a987a2524430157b2f.jpg?x-oss-process=style/x3","image_name":"微信图片_20200623153909.jpg","image_key":"custmorCertificate/1592897963-dca4063bb0a842a987a2524430157b2f.jpg","created_at":1592898512}],"custmor_certificate_images_text":"","forbid_call_order":"false","forbid_call_order_reason_category":"","forbid_call_order_reason_category_text":"","created_at":1592898512,"commission_effective_date":[2020,6,24],"commission_effective_date_text":"2020-06-24","speed_enabled":"true","speed_client_type_category":1,"speed_client_type_category_text":"普通价格","speed_client_grade":115,"speed_client_grade_text":"B-C-zone Speed price","speed_discount_rate":0,"speed_compensation_rate":1000,"cod_approval_state":2,"cod_approval_state_text":"已通过","cod_approval_remark":"","ka_return_addresses":[]}
            try:
                res_customer_2 = requests.post(url=url_customer_2, json=data_customer_2, headers=headers)
                assert res_customer_2.json()["code"] == 1
                print("重置{0}环境寄件人信息{1}成功".format(env, send_phone))
            except Exception as e:
                print("重置寄件人信息失败，报错信息是：{0}".format(e))
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

            # 如果redis里已经存在网点出纳，可以用redis里的，只有我的公款需要重新新建快递员
            if RedisBase().exists('finance_login'):
                finance_login = RedisBase().get('finance_login')
                print("本次的网点出纳是：{0}".format(finance_login))
            else:
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
                                           "organization_id": "TH01010101", "organization_type": 1,
                                           "department_id": "32",
                                           "department_name": "Network Operations", "positions_text": "网点出纳",
                                           "administrative_area": "กรุงเทพ คลองเตย", "mobile": "0614855889",
                                           "mobile_company": "", "email": "", "state": 1, "state_text": "在职",
                                           "hire_date": "2020-07-04", "leave_date": "", "stop_duties_date": "",
                                           "job_title_name": "DC Officer", "vehicle": "", "vehicle_text": "",
                                           "formal": 1,
                                           "formal_text": "编制",
                                           "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],
                                           "state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"},
                                                          {"code": 3, "text": "停职"}], "positions": [4],
                                           "position_category_list": [{"code": 1, "text": "快递员"},
                                                                      {"code": 2, "text": "仓管"},
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
            id = [my_public_funds_courier_login, warehouse_keeper_login, p_outlet_manager_login,
                  c_outlet_manager_login, finance_login]
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

            # # 重置寄件人信息为现金结算方式
            # url_customer_1 = "{0}/ms/api/setting/custmor?name=&pageSize=20&pageNum=1&countryCode=&provinceCode=&cityCode=&districtCode=&keyWord={1}&startTime=&endTime=".format(ms_host, send_phone)
            # res = requests.get(url=url_customer_1, headers=headers, verify=False)
            # id = res.json()["data"]["items"][0]["id"]
            # url_customer_2 = "{0}ms/api/setting/custmor/{1}".format(ms_host, id)
            # data_customer_2 ={"id":"CA0624","name":"{0}".format(send_name),"email":"936874337123@qq.com","company_size_category":3,"company_size_category_text":"C (现金结算客户)","state":1,"state_text":"开通","authentication_type":2,"authentication_type_text":"个人","permanent_address":"曼谷地区","authentication_name":"yr","authentication_citizen_id":"1101011992010","bill_country_code":"TH","bill_country_name":"Thailand","bill_province_code":"TH01","bill_province_name":"กรุงเทพ","bill_city_code":"TH0101","bill_city_name":"คลองเตย","bill_district_code":"TH010101","bill_district_name":"คลองตัน","bill_postal_code":"10110","bill_address":"rtrtrt","bill_contact_person":"小希","bill_phone":"1452145236","bill_email":"93687433117@qq.com","client_grade":999,"client_grade_text":"Standard price","client_type_category":2,"client_type_category_text":"折扣价格","account_type_category":1,"account_type_category_text":"普通签约客户","cod_account_source":"","cod_account_source_text":"","discount_rate":2,"discount_limit_enabled":"false","return_category":0,"return_category_text":"费率","return_uniform_amount":"","return_discount_rate":1,"settlement_category":1,"settlement_category_text":"现场结算","settlement_cycle_text":"","month_account_date":"","weighing_category":0,"weighing_category_text":"按重量/尺寸","credit_term":1,"credit_limit":0,"opened":"true","cod_settlement_category":0,"cod_settlement_category_text":"费率","cod_settlement_cycle":0,"cod_settlement_cycle_text":"日","cod_uniform_amount":"","opened_text":"开通","cod_poundage_rate_str":"2.50","cod_poundage_rate":25,"cod_poundage_minimum":0,"insure_rate":5,"staff_info_id":10002,"staff_info_name":"super admin sale","sign_date_text":"2020-07-04","bank_code":1,"bank_name":"曼谷银行","account_holder":"test开户行","bank_account_no":"62148301184568","major_mobile":"{0}".format(send_phone),"images":[],"images_text":"","ka_warehouses":[{"id":"5f001469d5da98531c2a592e","warehouse_no":"","ka_id":"CA0624","ka_info_id":"CA0624","name":"test","country_name":"Thailand","country_code":"TH","province_name":"กรุงเทพ","province_code":"TH01","city_name":"คลองเตย","city_code":"TH0101","district_name":"คลองตัน","district_code":"TH010101","opened":"","postal_code":"10110","detail_address":"testest","lat":"","lng":"","phone":"1452145237","src_name":"dfer","store_id":"","store_name":"","store_manager_id":"","store_manager_email":"","ntc_enabled":""}],"mobile":"","cod_enabled":"true","agent_id":None,"agent_name":"","sub_client_local_cpr":"","reject_return_strategy_category":2,"reject_return_strategy_category_text":"直接退回","remark":"qwew","custmor_certificate_images":[{"id":"5f001464d5da98531c2a592d","name":"微信截图_20200704132800.png","object_key":"custmorCertificate/1593840495-8cfe87ec177049908f1c4d6541577283.png","object_url":"https://fle-training-asset-internal.oss-ap-southeast-1.aliyuncs.com/custmorCertificate/1593840495-8cfe87ec177049908f1c4d6541577283.png","object_url_th":"https://fle-training-asset-internal.oss-ap-southeast-1.aliyuncs.com/custmorCertificate/1593840495-8cfe87ec177049908f1c4d6541577283.png?x-oss-process=style/th","object_url_x3":"https://fle-training-asset-internal.oss-ap-southeast-1.aliyuncs.com/custmorCertificate/1593840495-8cfe87ec177049908f1c4d6541577283.png?x-oss-process=style/x3","image_name":"微信截图_20200704132800.png","image_key":"custmorCertificate/1593840495-8cfe87ec177049908f1c4d6541577283.png","created_at":1593840745}],"custmor_certificate_images_text":"","forbid_call_order":"false","forbid_call_order_reason_category":"","forbid_call_order_reason_category_text":"","created_at":1593840740,"commission_effective_date":"","commission_effective_date_text":"","speed_enabled":"true","speed_client_type_category":2,"speed_client_type_category_text":"折扣价格","speed_client_grade":115,"speed_client_grade_text":"B-C-zone Speed price","speed_discount_rate":1,"speed_compensation_rate":1000,"cod_approval_state":2,"cod_approval_state_text":"已通过","cod_approval_remark":"","ka_return_addresses":[]}
            # try:
            #     res_customer_2=requests.post(url=url_customer_2, json=data_customer_2, headers=headers,verify=False)
            #     assert res_customer_2.json()["code"] == 1
            #     print("重置{0}环境寄件人信息{1}成功".format(env,send_phone))
            # except Exception as e:
            #     print("重置寄件人信息失败，报错信息是：{0}".format(e))
            #     raise e