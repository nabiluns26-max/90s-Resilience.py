from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

for sisi in (6, 10, 20):
    dadu = Die(sisi)
    print(f"\nMelempar dadu {sisi} sisi sebanyak 10 kali:")
    for _ in range(10):
        dadu.roll_die()