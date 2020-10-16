from random import randint

class Die:

    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        result = randint(1,self.sides)
        print(result)

die1 = Die()
for i in range(10):
    die1.roll_die()
print('-------------')
die2 = Die(10)
for i in range(10):
    die2.roll_die()
print('-------------')
die3 = Die(20)
for i in range(10):
    die3.roll_die()
print('-------------')