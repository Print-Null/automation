import pymysql as pymysql

# 每次需要清理出车线路
def clear_van_proof(van_line_name):

    db = pymysql.connect(host='192.168.0.229', user='fle_development', password='123456', port=3306)
    cou = db.cursor()
    # sql = 'DELETE FROM fle_development.fleet_van_proof WHERE van_line_name="测试到车"'
    sql = 'DELETE FROM fle_development.fleet_van_proof WHERE van_line_name="%s"'%van_line_name
    effect_row = cou.execute(sql)
    db.commit()
    # 打印影响的行数
    print('database version:', effect_row)
    # 关闭游标
    cou.close()
    # 关闭连接
    db.close()

# if __name__ == '__main__':
#     clear_van_proof("测试到车")