class User:
    def __init__(self,first_name,last_name,birth_year,birth_month):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.login_attempts = 0
    
    def greeter(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
    
    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"{full_name} is born in {self.birth_month}, {self.birth_year}.")

    def increment_login_attempts(self):
        """
        increase login_attempts 1
        """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """
        reset login_attempts to 0
        """
        self.login_attempts = 0
