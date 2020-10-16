import configparser
import sys, os
from app.Kit.Util.common_data import Common_data

sys.path.append(os.getcwd())
import allure
from assertpy import assert_that
import requests
import logging
import pytest


logging.basicConfig(level=logging.INFO)


@allure.feature('获取个人信息->目的地网点')
class Test_backyard_overtime_car_hc_personInfo():

    @pytest.mark.run(order=63)
    def test_test_backyard_overtime_car_hc_personInfo(self):
        comm = Common_data()
        host = comm.each_parameter("backyard_host")
        url = host + "api/_/hc/personInfo"
        # SESSION_ID = read_all_ini("by_warehouse_man_session","by_warehouse_end","warehouse_session_end")
        SESSION_ID = comm.get_parameter_from_redis("warehouse_session_end")
        headers = {
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json",
            "BY-PLATFORM": "FB_ANDROID",
            "X-BY-SESSION-ID": SESSION_ID
        }
        resp = requests.post(url=url, headers=headers, timeout=120, verify=False)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        #["data"]["store_id"]
        # 将仓管员登入的sessionid保存
        # 获取sessionid 存储到.ini文件中
        store_id = resp.json()["data"]["store_id"]
        logging.info(store_id)
        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # session_path = curpath + "/conf/all_data.ini"

        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/all_data.ini"
        #
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("store_id_end")
        # cf.set("store_id_end", option="store_id", value=str(store_id))
        # with open(session_path, "a+") as f:  # 可读可写，会覆盖  a+可读可写，不会覆盖
        #     cf.write(f)

        comm.write_parameter_to_redis("store_id_end",store_id)

        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
