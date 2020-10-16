import sys, os
from common.readconfig import ReadConfig

sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0] + "/flash")
root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app//")
configpath = os.path.join(root_path, "backyard/test_backstage/conf/conf.ini")
print(configpath)
import allure
import requests
import logging
import pytest
import configparser
from utils.redisbase import RedisBase

logging.basicConfig(level=logging.INFO)
cf = configparser.ConfigParser()


@allure.feature('kit-重置数据')
class Test_kit_auth_new_device_login(object):

    @pytest.mark.run(order=0)
    def test_restet_datas(self):
        self.redisObj = RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")

        print(configpath)
        cf.read(configpath, encoding="utf-8")
        env = RedisBase().get("runenv_py")
        print("当前环境是：{0}".format(env))
        # 超级管理员
        super_administrator_login = ReadConfig().get_config(self.runenv_py, "login_usr_10000")
        print(super_administrator_login)
        super_administrator_pwd = ReadConfig().get_config(self.runenv_py, "login_pwd_10000")
        # #快递员
        # my_public_funds_courier_login = cf.get(env, "my_public_funds_courier_login")
        # #仓管员
        # warehouse_keeper_login = cf.get(env, "warehouse_keeper_login")
        # ## 揽件网点经理
        # p_outlet_manager_login = cf.get(env, "p_outlet_manager_login")
        # #疑难件提交网点经理
        # c_outlet_manager_login = cf.get(env, "c_outlet_manager_login")
        # #网点出纳
        # finance_login = cf.get(env, "finance_login")
        # ms-host地址

        ms_host = ReadConfig().get_config(self.runenv_py, "ms_host")

        # 10000登录ms
        url_login = "{0}ms/api/auth/signin".format(ms_host)
        data_login = {"login": "{0}".format(super_administrator_login),
                      "password": "{0}".format(super_administrator_pwd)}
        res_login = requests.post(url=url_login, json=data_login, verify=False)

        headers = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN",
                   "X-MS-SESSION-ID": res_login.json()["data"]["session_id"]}
        # if env=="trunk":
        #     test_data=[{"url": '{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, my_public_funds_courier_login),"data":{"id": '{0}'.format(my_public_funds_courier_login), "company_name": "", "name": "yr-快递员","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "", "positions_text": "快递员","administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007048", "mobile_company": "6352635263","email": "", "state": 1, "state_text": "在职", "hire_date": "2020-06-29", "leave_date": "","stop_duties_date": "", "job_title_name": "", "vehicle": 1, "vehicle_text": "Van", "formal": 1,"formal_text": "编制", "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"}, {"code": 3, "text": "停职"}],"positions": [1], "position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"},{"code": 40, "text": "加班车申请员"}]}},
        #                {"url":'{0}/ms/api/setting/store/staffs/{1}/edit'.format(ms_host, warehouse_keeper_login),"data":{"id": '{0}'.format(warehouse_keeper_login), "company_name": "", "name": "yr-仓管员","organization_name": "U-Projectsunshine收派件网点", "organization_id": "TH03030302","organization_type": 1, "department_id": "", "department_name": "", "positions_text": "仓管","administrative_area": "นนทบุรี บางใหญ่", "mobile": "1871007049", "mobile_company": "6352635264","email": "", "state": 1, "state_text": "在职", "hire_date": "2020-06-29", "leave_date": "","stop_duties_date": "", "job_title_name": "", "vehicle": "", "vehicle_text": "", "formal": 1,"formal_text": "编制", "formal_list": [{"code": 0, "text": "非编制"}, {"code": 1, "text": "编制"}],"state_list": [{"code": 1, "text": "在职"}, {"code": 2, "text": "离职"}, {"code": 3, "text": "停职"}],"positions": [2],"position_category_list": [{"code": 1, "text": "快递员"}, {"code": 2, "text": "仓管"},{"code": 3, "text": "网点经理"}, {"code": 4, "text": "网点出纳"},{"code": 0, "text": "分配员"}, {"code": 18, "text": "网点主管"},{"code": 21, "text": "区域经理"}, {"code": 40, "text": "加班车申请员"}]}},
        #                {"url":'{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, p_outlet_manager_login),"data":{"id":'{0}'.format(p_outlet_manager_login),"company_name":"","name":"yr-仓管员","organization_name":"U-Projectsunshine收派件网点","organization_id":"TH03030302","organization_type":1,"department_id":"","department_name":"","positions_text":"仓管","administrative_area":"นนทบุรี บางใหญ่","mobile":"1871007049","mobile_company":"6352635264","email":"","state":1,"state_text":"在职","hire_date":"2020-06-29","leave_date":"","stop_duties_date":"","job_title_name":"","vehicle":"","vehicle_text":"","formal":1,"formal_text":"编制","formal_list":[{"code":0,"text":"非编制"},{"code":1,"text":"编制"}],"state_list":[{"code":1,"text":"在职"},{"code":2,"text":"离职"},{"code":3,"text":"停职"}],"positions":[3],"position_category_list":[{"code":1,"text":"快递员"},{"code":2,"text":"仓管"},{"code":3,"text":"网点经理"},{"code":4,"text":"网点出纳"},{"code":0,"text":"分配员"},{"code":18,"text":"网点主管"},{"code":21,"text":"区域经理"},{"code":40,"text":"加班车申请员"}]}},
        #                {"url":'{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, c_outlet_manager_login),"data":{"id":'{0}'.format(c_outlet_manager_login),"company_name":"","name":"yr-仓管员","organization_name":"U-Projectsunshine收派件网点","organization_id":"TH03030302","organization_type":1,"department_id":"","department_name":"","positions_text":"仓管","administrative_area":"นนทบุรี บางใหญ่","mobile":"1871007049","mobile_company":"6352635264","email":"","state":1,"state_text":"在职","hire_date":"2020-06-29","leave_date":"","stop_duties_date":"","job_title_name":"","vehicle":"","vehicle_text":"","formal":1,"formal_text":"编制","formal_list":[{"code":0,"text":"非编制"},{"code":1,"text":"编制"}],"state_list":[{"code":1,"text":"在职"},{"code":2,"text":"离职"},{"code":3,"text":"停职"}],"positions":[3],"position_category_list":[{"code":1,"text":"快递员"},{"code":2,"text":"仓管"},{"code":3,"text":"网点经理"},{"code":4,"text":"网点出纳"},{"code":0,"text":"分配员"},{"code":18,"text":"网点主管"},{"code":21,"text":"区域经理"},{"code":40,"text":"加班车申请员"}]}},
        #                {"url":'{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, finance_login),"data":{"id":'{0}'.format(finance_login),"company_name":"","name":"yr-网点出纳","organization_name":"U-Projectsunshine收派件网点","organization_id":"TH03030302","organization_type":1,"department_id":"","department_name":"","positions_text":"网点出纳","administrative_area":"นนทบุรี บางใหญ่","mobile":"1871007046","mobile_company":"6352635265","email":"","state":1,"state_text":"在职","hire_date":"2020-06-29","leave_date":"","stop_duties_date":"","job_title_name":"","vehicle":1,"vehicle_text":"Van","formal":1,"formal_text":"编制","formal_list":[{"code":0,"text":"非编制"},{"code":1,"text":"编制"}],"state_list":[{"code":1,"text":"在职"},{"code":2,"text":"离职"},{"code":3,"text":"停职"}],"positions":[4],"position_category_list":[{"code":1,"text":"快递员"},{"code":2,"text":"仓管"},{"code":3,"text":"网点经理"},{"code":4,"text":"网点出纳"},{"code":0,"text":"分配员"},{"code":18,"text":"网点主管"},{"code":21,"text":"区域经理"},{"code":40,"text":"加班车申请员"}]}}]
        # elif env=="training":
        #     test_data=[{"url":'{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, my_public_funds_courier_login),"data":{"id":'{0}'.format(my_public_funds_courier_login),"company_name":"","name":"นางสาว นัสรินทร์ ไสหยิด","organization_name":"Testing（北京团队测试用）","organization_id":"TH01010101","organization_type":1,"department_id":"32","department_name":"Network Operations","positions_text":"快递员","administrative_area":"กรุงเทพ คลองเตย","mobile":"0895897364","mobile_company":"","email":"","state":1,"state_text":"在职","hire_date":"2020-07-03","leave_date":"","stop_duties_date":"","job_title_name":"DC Officer","vehicle":1,"vehicle_text":"Van","formal":1,"formal_text":"编制","formal_list":[{"code":0,"text":"非编制"},{"code":1,"text":"编制"}],"state_list":[{"code":1,"text":"在职"},{"code":2,"text":"离职"},{"code":3,"text":"停职"}],"positions":[1],"position_category_list":[{"code":1,"text":"快递员"},{"code":2,"text":"仓管"},{"code":3,"text":"网点经理"},{"code":4,"text":"网点出纳"},{"code":0,"text":"分配员"},{"code":18,"text":"网点主管"},{"code":21,"text":"区域经理"},{"code":40,"text":"加班车申请员"}]}},
        #                {"url":'{0}/ms/api/setting/store/staffs/{1}/edit'.format(ms_host, warehouse_keeper_login),"data":{"id":'{0}'.format(warehouse_keeper_login),"company_name":"","name":"นางสาว กันย์ภิรมย์ สุคนธรัตน์","organization_name":"Testing（北京团队测试用）","organization_id":"TH01010101","organization_type":1,"department_id":"32","department_name":"Network Operations","positions_text":"仓管","administrative_area":"กรุงเทพ คลองเตย","mobile":"0954036726","mobile_company":"","email":"","state":1,"state_text":"在职","hire_date":"2020-07-04","leave_date":"","stop_duties_date":"","job_title_name":"DC Officer","vehicle":"","vehicle_text":"","formal":1,"formal_text":"编制","formal_list":[{"code":0,"text":"非编制"},{"code":1,"text":"编制"}],"state_list":[{"code":1,"text":"在职"},{"code":2,"text":"离职"},{"code":3,"text":"停职"}],"positions":[2],"position_category_list":[{"code":1,"text":"快递员"},{"code":2,"text":"仓管"},{"code":3,"text":"网点经理"},{"code":4,"text":"网点出纳"},{"code":0,"text":"分配员"},{"code":18,"text":"网点主管"},{"code":21,"text":"区域经理"},{"code":40,"text":"加班车申请员"}]}},
        #                {"url":'{0}ms/api/setting/store/staffs/{1}/edit'.format(ms_host, finance_login),"data":{"id":'{0}'.format(finance_login),"company_name":"","name":"นางสาว สุวภัทร ทองเถาว์","organization_name":"Testing（北京团队测试用）","organization_id":"TH01010101","organization_type":1,"department_id":"32","department_name":"Network Operations","positions_text":"网点出纳","administrative_area":"กรุงเทพ คลองเตย","mobile":"0614855889","mobile_company":"","email":"","state":1,"state_text":"在职","hire_date":"2020-07-04","leave_date":"","stop_duties_date":"","job_title_name":"DC Officer","vehicle":"","vehicle_text":"","formal":1,"formal_text":"编制","formal_list":[{"code":0,"text":"非编制"},{"code":1,"text":"编制"}],"state_list":[{"code":1,"text":"在职"},{"code":2,"text":"离职"},{"code":3,"text":"停职"}],"positions":[4],"position_category_list":[{"code":1,"text":"快递员"},{"code":2,"text":"仓管"},{"code":3,"text":"网点经理"},{"code":4,"text":"网点出纳"},{"code":0,"text":"分配员"},{"code":18,"text":"网点主管"},{"code":21,"text":"区域经理"},{"code":40,"text":"加班车申请员"}]}}]
        # for item in test_data:
        #     requests.post(url=item["url"],json=item['data'],headers=headers,verify=False)
        if env == "training":
            ## 揽件网点经理

            p_outlet_manager_login = ReadConfig().get_config(self.runenv_py, "indentifi_manager_usr")
            # 重置密码
            url_id = "{0}ms/api/setting/store/staffs/{1}/reset_password".format(ms_host, p_outlet_manager_login)
            res = requests.post(url=url_id, headers=headers, verify=False)
            print(res.text)
            url_kam = 'ms/api/customer/group/edit/add_ka'
            data_kam_vip = {"ka_id": "BA0020", "customer_group_id": "5d143ae6d5da982371bae809"}
            resp = requests.post(url=ms_host + url_kam, json=data_kam_vip, headers=headers, verify=False)
            logging.info(ms_host + url_kam)
            logging.info(data_kam_vip)
            print("修改kamvip客户分组")
            print(resp.text)
