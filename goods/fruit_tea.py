# goods/fruit_tea.py - 果茶子类
# 继承BaseDrink，实现果茶专属优惠：全场折扣基础上额外95折
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from goods.base_drink import BaseDrink



class FruitTea(BaseDrink):
    def __init__(self,name,price):
        super().__init__(name,price)
    def get_final_price(self,buy_num):

        total = self.price * buy_num
        print("=====")

        return round(total * 0.95  * self.shop_discount)

#重写打印小票方法：显示果茶专属优惠信息
    def print_ticket(self, buy_num: int):
        total = self.get_final_price(buy_num)
        print(f"实现果茶专属优惠：全场折扣基础上额外95折，折后{total}元")

#测试代码

if __name__ == "__main__":
    tea = FruitTea("果茶",10)
    FruitTea.set_shop_discount(0.9)
    tea.print_ticket(2)
