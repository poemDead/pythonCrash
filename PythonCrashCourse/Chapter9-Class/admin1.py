from user import User

class Privileges:

    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
    
    def show_privileges(self):
        print("You have these privileges: ")
        for privilege in self.privileges:
            print(f" - {privilege}")

class Admin(User):

    def __init__(self,first_name,last_name,birth_year,birth_month):
        super().__init__(first_name,last_name,birth_year,birth_month)
        self.privileges = Privileges()

