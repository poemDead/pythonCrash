from random import choice

pool = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'a',
    'b',
    'c',
    'd',
    'e',
    ]

first = choice(pool)
second = choice(pool)
third = choice(pool)
fourth = choice(pool)

print(f'The number is "{first}{second}{third}{fourth}"!')