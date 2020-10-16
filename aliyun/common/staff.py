import pymysql
from utils.database import Database


class Staff(object):
    def __init__(self):
        pass
        # self.bi_dbcon = Database("bi")

    '''
    角色对应关系-role_id
    网点收派员 快递员角色id = 1
    网点仓管员角色id = 2
    网点经理 = 3
    网点出纳 = 4
    线路中控人员 = 31
    线路规划管理员 = 32
    加班车申请员 = 40
    人事专员角色id = 16
    人事管理员角色id = 17
    KA 经理 = 45
    KA 主管 = 46
    KA 专员 = 47
    HRIS业务员 = 51
    汽运专员 = 26
    汽运经理 = 27
    区域网点经理 = 23
    区域经理 = 21
    ----------------------
    状态对应关系-state
    在职 = 1
    离职 = 2
    停职 = 3
    '''

    def get_role_staff_id(self, **kwargs):
        role_id = kwargs.get("role_id") if kwargs.get("role_id") else None
        state = kwargs.get("state") if kwargs.get("state") else None
        store_id = kwargs.get("store_id") if kwargs.get("store_id") else None
        category = kwargs.get("category") if kwargs.get("category") else None
        limit = kwargs.get("limit") if kwargs.get("limit") else 1
        return_data = ""
        if store_id:
            sql = '''
                    SELECT
                        staff_info_id,
                        `value` 
                    FROM
                        hr_staff_items 
                    WHERE
                        staff_info_id IN (
                        SELECT
                            s.staff_info_id 
                        FROM
                            hr_staff_info AS s
                            LEFT JOIN hr_staff_info_position p ON s.staff_info_id = p.staff_info_id 
                        WHERE
                            p.position_category = {} 
                            AND s.state = {} 
                            AND s.sys_store_id = {} 
                        ) 
                        AND item = "MANGER" limit {}
                        '''.format(role_id, state, store_id, limit)
        elif category:
            sql = '''
                    SELECT
                        staff_info_id,
                        `value` 
                    FROM
                        hr_staff_items 
                    WHERE
                        staff_info_id IN (
                        SELECT
                            s.staff_info_id 
                        FROM
                            hr_staff_info AS s
                            LEFT JOIN hr_staff_info_position p ON s.staff_info_id = p.staff_info_id 
                        WHERE
                            p.position_category = {} 
                            AND s.state = {} 
                            AND s.sys_store_id IN ( SELECT id FROM sys_store WHERE category = {} ) 
                        ) 
                        AND item = "MANGER" limit {}
                        '''.format(role_id, state, category, limit)
        else:
            sql = '''
                    SELECT
                        staff_info_id,
                        `value` 
                    FROM
                        hr_staff_items 
                    WHERE
                        staff_info_id IN (
                        SELECT
                            s.staff_info_id 
                        FROM
                            hr_staff_info AS s
                            LEFT JOIN hr_staff_info_position p ON s.staff_info_id = p.staff_info_id 
                        WHERE
                            p.position_category = {} 
                            AND s.state = {} 
                        ) 
                        AND item = "MANGER" limit {}
                        '''.format(role_id, state, limit)
        print(sql)
        data = self.bi_dbcon.get(sql)
        if data:
            return_data = data["staff_info_id"]
        return return_data

    def get_role_staff_id_manger(self, **kwargs):
        return_data = ""
        staff_info_id = kwargs.get("staff_info_id")
        sql = '''
        select `value` from hr_staff_items where staff_info_id = "{}" and item = "MANGER"
        '''.format(staff_info_id)
        data = self.bi_dbcon.get(sql)
        if data:
            return_data = data["value"]
        return return_data


# _a = Staff().get_role_staff_id(role_id = 2, state = 1, limit = "0,1")
# print(Staff().get_role_staff_id_manger(staff_info_id = _a))
# 获取对应角色和状态 并且 有在职状态下 上级的员工
# 获取对应角色和状态 并且 有离职状态下 上级的员工
# 获取对应角色和状态 并且 有停职职状态下 上级的员工
