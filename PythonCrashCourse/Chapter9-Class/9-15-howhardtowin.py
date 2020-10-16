from random import choice

pool = [
    '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e'
    ]

first = choice(pool)
second = choice(pool)
third = choice(pool)
fourth = choice(pool)

win_number = f"{first}{second}{third}{fourth}"

my_tickets = []

while True:
    first = choice(pool)
    second = choice(pool)
    third = choice(pool)
    fourth = choice(pool)
    my_ticket = f"{first}{second}{third}{fourth}"
    my_tickets.append(my_ticket)
    if my_ticket==win_number:
        print(len(my_tickets))
        break
