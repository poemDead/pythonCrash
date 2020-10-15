def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['tom','hannah','margot']
greet_users(usernames)