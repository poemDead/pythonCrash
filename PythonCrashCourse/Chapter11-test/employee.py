class Employee:
    def __init__(self,first_name,last_name,year_income):
        self.first_name = first_name
        self.last_name = last_name
        self.year_income = year_income
    
    def give_raise(self,raise_num=5000):
        if raise_num:
            self.year_income += raise_num
        
