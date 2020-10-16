import datetime
import pymysql

connection = None
cursor = None
try:
    # 创建数据库连接，必要参数：数据库host，用户名，密码，连接的数据库名称
    connection = pymysql.connect("localhost", "root", "xiao238304", "employees")
    cursor = connection.cursor()  # 创建操作数据库的实例
    sql = "select * from dept_emp limit 20"  # 创建执行的数据库语句
    try:
        cursor.execute(sql)     # 执行数据库语句
        emp = cursor.fetchone()
        print(type(emp))
        print(emp)
        print(datetime.datetime.strftime(emp[2], "%Y/%m/%d"))
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
