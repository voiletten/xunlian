# goods/milk_cap.py - 奶盖茶子类
# 继承BaseDrink，实现奶盖茶专属优惠：购买2杯及以上立减3元
# 实例属性，__milk_cap_cost 
# get_milk_cap_cost()   -->获取奶盖的单杯价格

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from goods.base_drink import BaseDrink

class MilkCap(BaseDrink):
    __milk_cap_cost = 0
    def __init__(self,name,price):
        super().__init__(name,price)
    def get_final_price(self,buy_num):
        if buy_num >=2:
            total_price = buy_num * self.shop_discount * self.get_milk_cap_cost() -3
            return round(total_price)
        else:
            total_price = buy_num * self.shop_discount * self.get_milk_cap_cost()
            return round(total_price)
    def print_price(self,buy_num):
        if buy_num >= 2:
            print(f"恭喜触发实现奶盖茶专属优惠：购买2杯及以上立减3元,{buy_num}杯最后总计{self.get_final_price(buy_num)}")
        else:
            print(f"很遗憾没有触发实现奶盖茶专属优惠：购买2杯及以上立减3元,{buy_num}杯最后总计{self.get_final_price(buy_num)}")

    def print_final_price(self,buy_num):
        if buy_num >=2:
            total_price = self.get_milk_cap_cost() * buy_num * self.shop_discount -3
            print(f"恭喜触发实现奶盖茶专属优惠：购买2杯及以上立减3元,{buy_num}杯最后总计{round(total_price)}")
        else:
            total_price = buy_num * self.shop_discount * self.get_milk_cap_cost()
            print(f"很遗憾没有触发实现奶盖茶专属优惠：购买2杯及以上立减3元,{buy_num}杯最后总计{round(total_price)}")




    def get_milk_cap_cost(self):
        return self.__milk_cap_cost
    def set_milk_cap_cost(self,num):
        self.__milk_cap_cost = num

#测试代码

if '__main__' == __name__:
    mtea = MilkCap("naigai",10)
    mtea.set_milk_cap_cost(10)
    print (f"单杯奶茶{mtea.get_milk_cap_cost()}")
    MilkCap.set_shop_discount(0.9)
    # mtea.print_price(3)
    # mtea.print_price(1)
    mtea.print_final_price(3)
    mtea.print_final_price(1)