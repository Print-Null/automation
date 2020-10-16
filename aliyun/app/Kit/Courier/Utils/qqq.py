import datetime

print(datetime.date.today())
# datetime.days

today = datetime.date.today()
min = 61

hour = min // 60
print(hour)
if hour < 10:
    hour = "0" + str(hour)
    print(hour)
fenzhong = min % 60
if fenzhong < 10:
    fenzhong = "0" + str(fenzhong)
    print(fenzhong)
print(fenzhong)

departure_time =str(today)+ " " + hour +":"+ fenzhong
print(departure_time)