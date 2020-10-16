import configparser
import logging
import os
import allure
import pytest
import requests
from assertpy import assert_that
# from app.kit.Storekeeper.Script.ms_login import Ms_Login
# from app.kit.Util.common_data import Common_data
from app.Kit.Storekeeper.Script.ms_login import Ms_Login
from app.Kit.Util.common_data import Common_data


@allure.feature(" ")
class est_Ms_Login_45011():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.ms = Ms_Login()
    @allure.story("网点经理登入功能,用来查看出车凭证")
    @pytest.mark.run(order=77)
    def est_ms_login_45011(self):
        comm = Common_data()
        # host = read_common("ms_host")
        host = comm.each_parameter("ms_host")
        url = host + "ms/api/auth/signin"
        header = {
            "Content-Type": "application/json"
        }

        # user = read_common("ms_login_user")
        user = comm.each_parameter("Warehouse_man_personInfo_start_login")
        # pwd = read_common("ms_login_pwd")
        pwd = comm.each_parameter("Warehouse_man_personInfo_start_pwd")
        data = {"login": user, "password": pwd}
        resp = requests.post(url=url, json=data, headers=header, verify=False)
        session = resp.json()["data"]["session_id"]
        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # session_path = curpath + "/conf/ms_session.ini"


        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/ms_session.ini"
        #
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("ms")
        # cf.set("ms", option="ms_session", value=str(session))
        # with open(session_path, "w+") as f:
        #     if str(session).startswith("1"):
        #         logging.info("MS，session信息开始写入")
        #         cf.write(f)
        #         logging.info("MS,session信息写入成功")
        #         logging.info("MS，session信息是：")
        #         logging.info(session)
        comm.write_parameter_to_redis("ms_session", session)
        logging.info("ms后台登入接口,响应结果是:")
        logging.info(resp.json())
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.json()["data"]).is_not_empty()


