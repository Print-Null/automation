import threading
import time


def sing():
    for i in range(3):
        print("我正在唱歌....")
        time.sleep(1)


def dance():
    for i in range(3):
        print("我正在跳舞....")
        time.sleep(2)


st = threading.Thread(target=sing)
sd = threading.Thread(target=dance)

st.start()
sd.start()
while True:
    length = len(threading.enumerate())
    print("当前线程数量%s" % length)
    if length <= 1:
        break
    time.sleep(0.5)
