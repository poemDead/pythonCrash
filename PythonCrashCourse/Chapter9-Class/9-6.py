'''
练习 9-6:冰激凌小店 冰激凌小店是一种特殊的餐馆。
编写一个名为 IceCreamStand 的类，
让它继承为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。
这两个版本的 Restaurant 类都可以，
挑选你更喜欢的那个即可。
添加一个名为 flavors 的属性，
用于 存储一个由各种口味的冰激凌组成的列表。
编写一个显示这些冰激凌的方法。创建一个 IceCreamStand 实例，并调用这个方法。
'''
from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """
    make icecreamstand restaurant
    """
    
    def __init__(self,restaurant_name,flavors):
        super().__init__(restaurant_name,cuisine_type='Ice Cream Stand')
        self.flavors = flavors
    
    def describe_flavors(self):
        print("We have these flavors: ")
        for flavor in self.flavors:
            print(f" - {flavor}")

new = IceCreamStand('Your_Ice',['Chocolate','Blueberry'])
new.describe_flavors()