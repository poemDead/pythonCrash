class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is opening now.")
    
    def set_number_served(self,number_served):
        self.number_served = number_served
        print(f'Now the number {self.restaurant_name.title()} have served {self.number_served} people.')

    def increment_number_served(self,increment_num):
        self.number_served += increment_num
        print(f'The number served has increased {increment_num}, \nnow it has updated to {self.number_served}.')

matsuya = Restaurant('matsuya','japanese food')
matsuya.describe_restaurant()
matsuya.open_restaurant()
matsuya.set_number_served(2736)
matsuya.increment_number_served(24)