import sys, os

sys.path.append(os.getcwd())
import requests
import hashlib
import time
import utils.redisbase as redisbase
from common.readconfig import ReadConfig


class staff(object):

    def __init__(self):
        self.redisObj = redisbase.RedisBase()
        self.readConfigObj = ReadConfig()
        self.runenv = self.redisObj.get("runenv_py")
        if self.runenv is False:
            self.runenv = "trunk"
        self.fbi_url = self.readConfigObj.get_config(self.runenv, "fbi_host")

    def bi_login(self):
        url = self.fbi_url + 'v1/login?'
        pwd = hashlib.md5(("fbi" + '10000' + str(int(time.time()))).encode(encoding = 'utf-8')).hexdigest() + str(
            int(time.time()))
        body = {'username': 10000, 'password': pwd}
        data = requests.post(url = url, data = body, verify = False)
        token = data.json()['body']['token'] if data.json()['body']['token'] else ""
        return token

    def bi_staff_modify(self, **kwargs):
        body = {}
        staff_info_id = kwargs["staff_info_id"] if 'staff_info_id' in kwargs.keys() else None
        if staff_info_id is None:
            return "error parameter"

        headers = {}
        token = self.bi_login()
        headers.update(Authorization = 'Bearer ' + token)
        url = self.fbi_url + '/v1/staffs/view?staff_info_id=' + str(staff_info_id)
        datainfo = requests.get(url = url, headers = headers, verify = False)
        if datainfo.json()["code"] == 0:
            body = datainfo.json()["body"]
        body.update(job_title = kwargs["job_title"]) if 'job_title' in kwargs.keys() else None
        body.update(sys_store_id = kwargs["sys_store_id"]) if 'sys_store_id' in kwargs.keys() else None
        body.update(sys_department_id = kwargs["sys_department_id"]) if 'sys_department_id' in kwargs.keys() else None
        body.update(
            node_department_id = kwargs["node_department_id"]) if 'node_department_id' in kwargs.keys() else None
        print(body)

        body.update(state = kwargs["state"]) if 'state' in kwargs.keys() else None
        body.update(formal = kwargs["formal"]) if 'formal' in kwargs.keys() else None
        body.update(name = kwargs["name"]) if 'name' in kwargs.keys() else None
        body.update(mobile = kwargs["mobile"]) if 'mobile' in kwargs.keys() else None
        body.update(event = kwargs["event"]) if 'event' in kwargs.keys() else None
        body.update(email = kwargs["email"]) if 'email' in kwargs.keys() else None
        print(body)
        url = self.fbi_url + 'v1/staffs/create?'
        data = requests.post(url = url, headers = headers, json = body, verify = False)
        if data.json()["code"] == 0:
            return staff_info_id
        else:
            return 'error:' + str(data.json()["msg"])


a = staff().bi_staff_modify(staff_info_id = 22722, state = "2")
print(a)

# staff_info_id 员工账号信息
# name 员工姓名
# mobile 手机
# mobile 手机
# job_title 职位
# sys_store_id 网点Id
# sys_department_id 部门Id
# node_department_id 子部门id
# node_department_id 子部门id
# formal 员工属性（下拉列表：1 编制、0 非编制、2:加盟商（合作商）3: 其他（合作商））4:实习生
# state 员工状态 1 在职 2 离职 3 停职
# hire_date 入职时间
# leave_date 离职时间
# stop_duties_date 停职日期
# outsourcing_category 员工外协类型
# area_id 区域id(包含多个)
# area_manager_id 区域经理id
# master_staff 主账号
# is_sub_staff 是否是子账号 1:是 0:否
