import datetime
import pymysql


def get_staff_info_id(pno):
    connection = None
    cursor = None
    try:
        # 创建数据库连接，必要参数：数据库host，用户名，密码，连接的数据库名称
        connection = pymysql.connect("192.168.0.229", "fle_development", "123456", "fle_development")
        cursor = connection.cursor()  # 创建操作数据库的实例
        sql = 'select id,staff_info_id from ticket_pickup where ka_warehouse_id = (SELECT ka_warehouse_id from order_info where pno="{0}")'.format(
            pno)  # 创建执行的数据库语句
        try:
            cursor.execute(sql)  # 执行数据库语句
            emp = cursor.fetchall()
            # print(type(emp))
            # print(emp)
            # print(datetime.datetime.strftime(emp[2], "%Y/%m/%d"))
            for i in emp:
                order_id = i[0]
                staff_info_id = i[1]
                # print(order_id, staff_info_id)
                return [order_id, staff_info_id]
        except Exception as ex:
            print(ex)
        # finally:  # finally下的语句不管有异常还是没有异常都会执行
        #     cursor.close()
        #     connection.close()
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


a = get_staff_info_id("TH46061RHP2Z")[0]
b = get_staff_info_id("TH46061RHP2Z")[1]
print(a, b)
