class User:
    def __init__(self,first_name,last_name,birth_year,birth_month):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_month = birth_month
    
    def greeter(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
    
    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"{full_name} is born in {self.birth_month}, {self.birth_year}.")
    
me = User('chase','zhai','1995','September')
me.greeter()
me.describe_user()