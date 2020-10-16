import logging

import pytest
from assertpy import assert_that
import allure

# from app.kit.Storekeeper.Script.query_company_name import Query_Company_Name
from app.Kit.Storekeeper.Script.query_company_name import Query_Company_Name


@allure.feature("查询公司名称")
class Test_Query_Company_Name():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.com = Query_Company_Name()

    @pytest.mark.run(order=11)
    def test_query_company_name(self):
        res = self.com.query_company_name()
        logging.info("查询公司名称,接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_empty()


