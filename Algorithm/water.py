print("How many battles do you have?")
n  = int(input())
total_change=0


""" while n >= 3:
    change = int(n/3)
    nokori = int(n%3)
    n = change + nokori
    total_change +=change """

while n >= 2:
    if n==2:
        n += 1
    change = int(n/3)
    nokori = int(n%3)
    n = change + nokori
    total_change +=change


print(f"总共能换来{total_change}瓶")