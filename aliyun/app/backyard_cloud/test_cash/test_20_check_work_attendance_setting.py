#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :2020/8/27 20:54
# @Author :lemon_yaoxiaonie
# @Email  :363111505@qq.com
# @File   :test_20_attendance.py
import pytest
import requests
import logging
from utils.redisbase import RedisBase
import time


@pytest.mark.usefixtures("get_data")
@pytest.mark.usefixtures("get_case_title")
# 考勤模块--考勤设置、考勤统计
class TestCheckWorkAttendanceSetting:
    def test_attendance_del_attachment(self, get_data):  # 'code': -1
        title = "清除底片"
        logging.info(title)
        url = "{0}/web/attendance/del_attachment".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        # data={"staff_info_id":RedisBase().get("staff_id")}
        data = {"staff_info_id": "BW3kz27k84"}  # 先从数据库里取个员工的staff_id

        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_attendance_get_attachment(self, get_data):  # 'code': -1
        title = "查看底片"
        logging.info(title)
        url = "{0}/web/attendance/get_attachment".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "X-Token": RedisBase().get("company_signin_X-Token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())



    # @pytest.mark.parametrize("type",[1,2,3])   #群组类型 1 限制上下班时间 2 不限制时间 3 不用打卡',
    # @pytest.mark.parametrize("is_holiday",[1,2])  #is_holiday 节假日是否休息 1 法定节假日休息 2 不休息
    # @pytest.mark.parametrize("out_range",[1,2])  #out_range 是否可外勤 1 可以外勤打卡 2 不可以',
    # @pytest.mark.parametrize("change_type",[1,2])  #change_type  1 即时生效 2 次日生效
    def test_attendance_add_setting(self, get_data):  # 'code': -1
        title = "添加考勤规则群组"
        logging.info(title)
        url = "{0}/web/attendance/add_setting".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        data = {"name": "考勤"+str(int(time.time())), "type": 2, "is_holiday": 1, "out_range": 1, "change_type": 1, "duration": 5,
                "staff_info_ids": [RedisBase().get("staff_id")], "department_id": [1],
                "week_setting": [
                    {
                        "week": 1,
                        "start": "09:00",
                        "end": "18:00"
                    },
                    {
                        "week": 2,
                        "start": "08:00",
                        "end": "15:00"
                    }
                ],
                "area_setting": [
                    {
                        "name": "朝阳",
                        "lng": 1982.2323,
                        "lat": 5121.993,
                        "range": 200
                    },
                    {
                        "name": "海淀",
                        "lng": 982.2323,
                        "lat": 21.993,
                        "range": 500
                    }
                ]
                }
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            RedisBase().set("attendance_add_name",data["name"],ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())

    def test_attendance_attendance_setting_list(self, get_data):  # 'code': -1
        title = "考勤群组列表"
        logging.info(title)
        url = "{0}/web/attendance/attendance_setting_list".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        data={"name":RedisBase().get("attendance_add_name")}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            #存取新增的考勤组id
            RedisBase().set("attendence_add_id",res.json()["data"]["result"][0]["id"],ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_attendance_edit_setting(self, get_data):  # change_type传2，报错--ok
        title = "编辑群组规则"
        logging.info(title)
        url = "{0}/web/attendance/edit_setting".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        data = {"id":RedisBase().get("attendence_add_id"),"name": "aaa考勤"+str(int(time.time())), "type": 2, "is_holiday": 1, "out_range": 1, "change_type": 2, "duration": 5,
                "staff_info_ids": ["A29krwDoRn"], "department_ids": [1],
                "week_setting": [
                    {
                        "week": 1,
                        "start": "09:00",
                        "end": "18:00"
                    },
                    {
                        "week": 2,
                        "start": "08:00",
                        "end": "15:00"
                    }
                ],
                "area_setting": [
                    {
                        "name": "朝阳",
                        "lng": 1982.2323,
                        "lat": 5121.993,
                        "range": 200
                    },
                    {
                        "name": "海淀",
                        "lng": 982.2323,
                        "lat": 21.993,
                        "range": 500
                    }
                ]
                }
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())

    def test_attendance_attendance_setting_info(self, get_data):
        title = "查看员工考勤规则群组"
        logging.info(title)
        url = "{0}/web/attendance/attendance_setting_info?staff_info_id={1}".format(get_data[1], "BW3kz27k84")
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}

        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_attendance_all_setting_list(self, get_data):
        title = "规则列表下拉菜单"
        logging.info(title)
        url = "{0}/web/attendance/all_setting_list".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_statistics_reissue_setting(self, get_data):
        title = "后台补卡配置"
        logging.info(title)
        url = "{0}/web/attendance/reissue_setting".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        data={'days': 5, 'times': 1}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.text)
            logging.info(res.json())

    def test_statistics_reissue_info(self, get_data):
        title = "补卡配置信息"
        logging.info(title)
        url = "{0}/web/attendance/reissue_info".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        data={'days': 5, 'times': 1}  #几天内几次
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.text)
            logging.info(res.json())

    def test_statistics_attendance(self, get_data):  #start_date”必须符合日期格式YYYY-MM-DD
        title = "员工考勤统计表"
        logging.info(title)
        url = "{0}/web/statistics/attendance".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        # data = {"page":1,"page_size":20,"stat_date":time.strftime('%Y-%m-%d'),"end_date":time.strftime('%Y-%m-%d')}
        data={'page': 1, 'page_size': 20, 'stat_date': '2020-08-28', 'end_date': '2020-08-28'}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.text)
            logging.info(res.json())

#先新增一个，或者之前新增两个，一个编辑一个删除---待完成
    def test_attendance_del_setting(self, get_data):
        title = "删除考勤规则群组"
        logging.info(title)
        url = "{0}/web/attendance/del_setting".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        # data = {"id":RedisBase().get("attendence_add_id")}
        data = {"id":23}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())

    def test_attendance_ph_days(self, get_data):  # 'code': -1
        title = "公休日ph日期"
        logging.info(title)
        url = "{0}/web/attendance/ph_days".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        data = {"year":2020}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_attendance_get_attendance_info(self, get_data):  # 'code': -1
        title = "获取考勤信息"
        logging.info(title)
        url = "{0}/app/attendance/get_attendance_info".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        res = requests.post(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_attendance_info(self, get_data):  # {'code': 0, 'message': 'month请选择日期', 'data': None}
        title = "app-考勤打卡考勤日历"
        logging.info(title)
        url = "{0}/app/attendance/info?month={1}".format(get_data[1],"2020-08-01")
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())


    # def test_attendance_save_ph_days(self, get_data):  # 没开发完
    #     title = "保存ph 公休日"
    #     logging.info(title)
    #     url = "{0}/web/attendance/save_ph_days".format(get_data[1])
    #     headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
    #                "Content-Type": "application/json"}
    #     data = {"date_list":["2020-08-29","2020-08-30"],"year_at":2020}
    #     res = requests.post(url=url, json=data,headers=headers)
    #     try:
    #         assert res.status_code == 200
    #         assert res.json()["code"] == 1
    #         assert res.json()["message"].upper() == "SUCCESS"
    #         logging.info("断言成功,响应结果是:")
    #     except Exception as e:
    #         logging.error("断言失败,报错信息是:")
    #         logging.error(e)
    #         raise e
    #     finally:
    #         logging.info(url)
    #         logging.info(headers)
    #         logging.info(res.json())

    # def test_attendance_attendance_list(self, get_data):  #'code': -1
    #     title = "打卡设置列表页"
    #     logging.info(title)
    #     url = "{0}/web/attendance/attachment_list".format(get_data[1])
    #     headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),"Content-Type":"application/json"}
    #     data={}
    #     res = requests.get(url=url, headers=headers)
    #     try:
    #         assert res.status_code == 200
    #         assert res.json()["code"] == 1
    #         assert res.json()["message"].upper() == "SUCCESS"
    #         logging.info("断言成功,响应结果是:")
    #         logging.info(res.json())
    #     except Exception as e:
    #         logging.error("断言失败,报错信息是:")
    #         logging.error(e)
    #         raise e
    #     finally:
    #         logging.info(url)
    #         logging.info(headers)
    #         logging.info(res.json())
