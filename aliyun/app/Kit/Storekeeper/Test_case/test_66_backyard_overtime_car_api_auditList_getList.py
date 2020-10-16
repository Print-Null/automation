import configparser
import sys, os

# from app.kit.Storekeeper.utils.read_ini_file_all import read_all_ini
# from app.kit.Util.common_data import Common_data

from app.Kit.Util.common_data import Common_data

sys.path.append(os.getcwd())
import allure
from assertpy import assert_that
import requests
import logging
import pytest

logging.basicConfig(level=logging.INFO)


@allure.feature('网点经理->待处理列表展示')
class Test_backyard_overtime_car_api_auditList_getList(object):

    @pytest.mark.run(order=66)
    def test_test_backyard_overtime_car_api_auditList_getList(self):
        comm = Common_data()
        host = comm.each_parameter("backyard_host")
        url = host + "api/_/auditList/getList"
        # SESSION_ID = read_all_ini("by_warehouse_man_session", "outlet_manager", "outlet_manager_session")
        SESSION_ID = comm.get_parameter_from_redis("outlet_manager_session")
        headers = {
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json",
            "BY-PLATFORM": "FB_ANDROID",
            "X-BY-SESSION-ID": SESSION_ID
        }

        data = {
          "audit_show_type": 2,
          "audit_state_type": 1,
          "page_num": 1
        }
        resp = requests.post(url=url, json=data, headers=headers, timeout=120, verify=False)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        #["data"]["dataList"][0]["id"]
        # 将仓管员登入的sessionid保存
        # 获取sessionid 存储到.ini文件中
        session = resp.json()["data"]["dataList"][0]["id"]
        logging.info(session)
        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # session_path = curpath + "/conf/all_data.ini"
        # session_path = os.path.join(os.path.abspath(
        #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        #     "conf/all_data.ini")

        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/all_data.ini"
        #
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("auditList_getList")
        # cf.set("auditList_getList", option="auditList_getList", value=str(session))
        # with open(session_path, "a+") as f:  # 可读可写，会覆盖  a+可读可写，不会覆盖
        #     cf.write(f)

        comm.write_parameter_to_redis("auditList_getList", session)
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["msg"]).is_equal_to("请求成功!")




