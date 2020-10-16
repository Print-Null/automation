import pytest
import requests
from assertpy import assert_that

from app.backyard.test_backstage.util.write_ini import write_ini
from common.readconfig import ReadConfig
from utils import redisbase

#ms登入
from utils.redisbase import RedisBase


class Test_Ms_Login():
    def setup(self):
        self.redisObj = redisbase.RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        self.host = ReadConfig().get_config(self.runenv_py, "ms_host")
    @pytest.mark.run(order=6)
    def test_ms_login(self):

        url = self.host + "ms/api/auth/signin"
        header = {
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"zh-CN",
            "Content-Type":"application/json;charset=UTF-8"
        }
        login = ReadConfig().get_config(self.runenv_py, "ms_houtai_login_user")
        password = ReadConfig().get_config(self.runenv_py, "ms_houtai_login_pwd")
        data = {"login":login,"password":password}
        resp = requests.post(url=url,headers=header,json=data,verify=False)
        print(url)
        print(header)
        print(data)
        print(resp.json())
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.json()["data"]).is_not_empty()
        ms_token = resp.json()["data"]["session_id"]
        RedisBase().set('ms_token', ms_token, ex=6000)
        # write_ini(filename="bi_login", section="ms_token", option="ms_token", Values=ms_token, mode="a+")