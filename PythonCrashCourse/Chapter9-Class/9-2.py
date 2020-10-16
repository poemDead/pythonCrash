class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is opening now.")

matsuya = Restaurant('matsuya','japanese food')
mcdonald = Restaurant('Mcdonald','fast food')
tiedan = Restaurant('Tie dan daoxiaomian','chinese food')

matsuya.describe_restaurant()
mcdonald.describe_restaurant()
tiedan.describe_restaurant()
