import datetime
import pymysql


def get_staff_info_id():
    connection = None
    cursor = None
    try:
        # 创建数据库连接，必要参数：数据库host，用户名，密码，连接的数据库名称
        connection = pymysql.connect("localhost", "root", "xiao238304", "exercise")
        cursor = connection.cursor()  # 创建操作数据库的实例
        sql1 = 'select * from fill'  # 创建执行的数据库语句
        sql2 = "select * from repertory"
        try:
            cursor.execute(sql1)  # 执行数据库语句
            emp1 = cursor.fetchall()
            cursor.execute(sql2)
            emp2 = cursor.fetchall()
            # print(type(emp))
            # print(emp)
            # print(datetime.datetime.strftime(emp[2], "%Y/%m/%d"))
            # for i in emp:
            #     order_id = i[0]
            #     staff_info_id = i[1]
            #     return [order_id, staff_info_id]
            return emp1, emp2
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


a, b = get_staff_info_id()

# a_dict = {}
for i in b:
    id = i[0]
    size = i[1]
    status = i[2]
    sum = 0
    for j in a:
        if j[0] == id:
            sum += j[1]
    # a_dict.update({id: sum})
    if status == 0:
        try:
            assert size == sum
            print("id为%s的商品已售罄" % id)
        except Exception:
            print("fill表缺失数据")
    elif status == 1:
        try:
            assert size > sum
            print("id为%s的商品库存有货" % id)
        except Exception:
            print("repertory表记录有误")
    else:
        print("status取值错误")
