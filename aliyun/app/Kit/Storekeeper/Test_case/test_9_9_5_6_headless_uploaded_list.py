import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.headless_uploaded_list import Headless_Uploaded_List
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.headless_uploaded_list import Headless_Uploaded_List
from app.Kit.Storekeeper.Script.headless_uploaded_list import Headless_Uploaded_List


@allure.feature("无头件已上传列表")
class Test_Headless_Uploaded_List():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.headless = Headless_Uploaded_List()
    @allure.title("无头件已上传列表")
    @allure.story("无头件已上传列表")
    @pytest.mark.run(order=56)
    def test_headless_uploaded_list(self):
        res = self.headless.headless_uploaded_list()
        logging.info("无头件已上传列表,接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()
        # schema_res = Validate_jsonschema(res.json(), "headless_uploaded_list.json")
        # assert_that(schema_res).is_none()

