import logging
import allure
import pytest
import requests
from app.Kit.Util.common_data import Common_data
from utils.redisbase import RedisBase

@allure.feature("交接后，货物破损")
class Test_After_Problem_Piece_Damaged_Goods():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.redisObj = RedisBase()
        self.session_id = self.redisObj.get('warehouse_login_0_0_0_["data"]["sessionid"]')
        self.pno = self.redisObj.get('courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]')

    @pytest.mark.run(order=114)
    def test_after_problem_piece_damaged_goods(self):
        comm = Common_data()
        true = True
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/ticket/parcels/" + self.keyword + "/mark"
        url = host + "api/courier/v1/parcels/"+self.pno+"/problem_submission"
        header = {
            "X-FLE-SESSION-ID": self.session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }

        data = {
            "difficulty_marker_category": 20,
            "image_keys": [
                "difficulty/1593519846-1dcfb442542a428ab34e55d7e0abfc69.jpg"
            ],
            "remark": "d来源,交接后，货物破损"
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("交接后，货物破损,响应结果是：")
        logging.info(res.json())
        logging.info("请求header")
        logging.info(header)
        logging.info("请求参数")
        logging.info(data)
        logging.info("请求url")
        logging.info(url)

