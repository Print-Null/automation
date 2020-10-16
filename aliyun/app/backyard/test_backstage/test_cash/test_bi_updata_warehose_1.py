import json

import allure
import pytest
import requests
from assertpy import assert_that

from app.backyard.test_backstage.util.read_ini import read_ini
from app.backyard.test_backstage.util.read_json_file import read_json_file
from common.readconfig import ReadConfig
from utils import redisbase
import time

from utils.redisbase import RedisBase


@allure.feature("修改申请加班车仓管员账号")
class Test_Bi_Update_warehouse_1():

    def setup(self):
        # self.session_bi = read_ini("bi_login","token","token")
        self.session_bi = RedisBase().get("bi_login")
        self.redisObj = redisbase.RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        self.host = ReadConfig().get_config(self.runenv_py, "fbi_host")
        self.Warehouse_man_personInfo_start_login = ReadConfig().get_config(self.runenv_py, "Warehouse_man_personInfo_start_login")
    @pytest.mark.run(order=3)
    def test_bi_update_warehouse_1(self):
        null = None
        time_bi = int(time.time())
        # url = self.host + "v1/staffs/create?lang=&time="+str(time_bi)+"&auth=92f1ff3bbff587d3c33bd70366ef33c7&fbid=10000&_view=formal"
        url = self.host + "v1/staffs/create?lang=&time="+str(time_bi)+"&auth=92f1ff3bbff587d3c33bd70366ef33c7&fbid=10000&_view=formal"
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Authorization": "Bearer " + self.session_bi,
            "Content-Type": "application/json;charset=UTF-8"
        }

        data_te = json.dumps(read_json_file("apply_warehouse1_te")) #测试环境仓管
        print(data_te)
        print(type(data_te))
        #需要获取tra环境的数据填写这
        #data_tra =


        # data_te = {
        #     "staff_info_id": 22602,
        #     "emp_id": "",
        #     "name": "shop出纳2",
        #     "name_en": null,
        #     "sex": "0",
        #     "identity": "1212122314",
        #     "mobile": "1212122314",
        #     "mobile_company": null,
        #     "email": "",
        #     "personal_email": null,
        #     "job_title": "220",
        #     "sys_store_id": "TH01010314",
        #     "sys_department_id": "3",
        #     "node_department_id": 0,
        #     "formal": "1",
        #     "company_name_ef": null,
        #     "state": "1",
        #     "hire_date": "2020-01-11 00:00:00",
        #     "leave_date": null,
        #     "updated_at": "2020-04-18 08:19:31",
        #     "branch": null,
        #     "uuid": "a995bf36-e634-498c-83fb-8d32baf9dd15",
        #     "hire_date_origin": null,
        #     "is_sub_staff": 0,
        #     "payment_markup": "",
        #     "stop_duties_date": null,
        #     "bank_no": null,
        #     "payment_state": 1,
        #     "leave_reason": "",
        #     "creater": 10000,
        #     "is_auto_system_change": 0,
        #     "id": 26881,
        #     "oil_card_deposit": 0,
        #     "bank_type": 2,
        #     "stop_duties_count": 0,
        #     "stop_duty_reason": null,
        #     "wait_leave_state": 0,
        #     "health_status": 1,
        #     "disability_certificate": null,
        #     "vehicle_source": 0,
        #     "vehicle_use_date": null,
        #     "staff_type": 0,
        #     "stop_payment_type": null,
        #     "week_working_day": 6,
        #     "job_title_grade": null,
        #     "job_title_level": null,
        #     "bank_no_name": "shop出纳2",
        #     "bank_name": "TMB",
        #     "staff_car_type": "",
        #     "staff_car_no": "",
        #     "driver_license": "",
        #     "outsourcing_type": "",
        #     "equipment_cost": "",
        #     "equipment_deduction_type": "",
        #     "equipment_deduction_type_text": "",
        #     "stop_duty_reason_title": "",
        #     "patment_markup_other": "",
        #     "payment_markup_name_arr": "",
        #     "position_category": [
        #         2
        #     ],
        #     "position_category_name": "仓管  ",
        #     "job_title_name": "Mini-CS officer",
        #     "sys_department_name": "Customer Service",
        #     "department_level": [
        #         3
        #     ],
        #     "job_title_level_name": null,
        #     "sys_store_name": "自动化测试001",
        #     "manager": "22601",
        #     "manager_name": "shop出纳1",
        #     "manager_state": "1",
        #     "stop_payment_type_arr": [],
        #     "sys_district": "0",
        #     "email_state": "-1",
        #     "email_suffix": "-1",
        #     "img_driving_license": [],
        #     "img_identity": [],
        #     "img_driver_license": [],
        #     "img_bank_info": [],
        #     "img_temp_contract": [],
        #     "img_household_registry": [],
        #     "img_vehicle": [],
        #     "region_id": [],
        #     "piece_id": [],
        #     "payment_markup_name_arr_list": "",
        #     "area_manager_strore": [],
        #     "profile_object_key": null
        # }
        if self.runenv_py == "trunk":
            resp = requests.post(url=url, headers=header, data=data_te, verify=False)
            print(resp.json())
            assert_that(resp.json()["code"]).is_equal_to(0)
            assert_that(resp.json()["body"]["staff_info_id"]).is_equal_to(int(self.Warehouse_man_personInfo_start_login))
        elif self.runenv_py == "training":
            data_tra = json.dumps(read_json_file("apply_warehouse1_tra")) #预发布环境仓管
            resp_tra = requests.post(url=url, headers=header, data=data_tra, verify=False)
            print(resp_tra.json())
            assert_that(resp_tra.json()["code"]).is_equal_to(0)
            assert_that(resp_tra.json()["body"]["staff_info_id"]).is_equal_to(int(self.Warehouse_man_personInfo_start_login))




