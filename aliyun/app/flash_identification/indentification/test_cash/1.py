import datetime
import time
# timeArray = datetime.datetime.today()
# print(timeArray)
# print(datetime.date.today())
# timeStamp = int(time.mktime(timeArray))
# print(timeStamp)
# d = datetime.date.today()
# data_sj = time.strptime(str(d),"%Y-%m-%d")       #定义格式
# print(data_sj)
# time_int = eval(str(int(time.mktime(time.strptime(str(datetime.date.today()),"%Y-%m-%d")))))
# print(time_int)

# test2 = 1592845200
# data_sj = time.localtime(test2)
# time_str = time.strftime("%Y-%m-%d %H:%M:%S",data_sj)            #时间戳转换正常时间
# print(time_str)
#
# test3 = 1592931599
# data_sj1 = time.localtime(test3)
# time_str1 = time.strftime("%Y-%m-%d %H:%M:%S",data_sj1)            #时间戳转换正常时间
# print(time_str1)
#
# time_int = (int(time.mktime(time.strptime(str(datetime.date.today()) + " 01:00:00","%Y-%m-%d %H:%M:%S"))))
# print(time_int)
#
# time_int2 = (int(time.mktime(time.strptime(str(datetime.date.today() +datetime.timedelta(days=1)) + " 00:59:59","%Y-%m-%d %H:%M:%S"))))
# print(time_int2)

# print(str((datetime.datetime.today() + datetime.timedelta(days=1)))[0:10] + " 00:59:59")
# print(str((datetime.datetime.today() + datetime.timedelta(days=1)))[0:10] + " 00:59:59")
#
# print(datetime.date.today() +datetime.timedelta(days=1) )

# time_int2 = (int(time.mktime(time.strptime((str((datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))[0:10] + " 00:59:59")).time(),"%Y-%m-%d %H:%M:%S")))
# print(time_int2)

print(datetime.datetime.today())
print(str(datetime.date.today()) + " 00:00:00" +" - " + str(datetime.date.today()) + " 23:59:59")
print(str(datetime.date.today()) + "23:59:59")
# 2020-06-01 00:00:00 - 2020-06-23 23:59:59