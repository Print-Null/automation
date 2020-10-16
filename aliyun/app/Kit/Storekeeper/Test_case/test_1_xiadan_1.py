# from Courier.Script.xiadan_1 import Write_Order_11

#给张洋使用的，一个任务，揽收多个订单。
# class Test_AA1():
# from app.kit.Courier.Script.xiadan_1 import Write_Order_11
from app.Kit.Courier.Script.xiadan_1 import Write_Order_11


class est_AA1():

    def setup(self):
        self.aa = Write_Order_11()


    def est_xiadan1(self):
        res = self.aa.write_order(1)
        print(res)


