import logging

import pytest
from assertpy import assert_that
import allure

# from Storekeeper.Script.headless_upload import Handless_Upload
# from app.kit.Storekeeper.Script.headless_upload import Handless_Upload
from app.Kit.Storekeeper.Script.headless_upload import Handless_Upload


@allure.feature("无头件上传")
class Test_headless_upload():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.headless = Handless_Upload()

    @allure.title("无头件上传")
    @allure.story("无头件上传")
    @pytest.mark.run(order=55)
    def test_handless_upload(self):
        res = self.headless.handless_upload()
        logging.info("无头件上传，接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_none()

