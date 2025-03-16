import random
class Player():
    def __init__(self, ID):
        self.ID = ID
        self.numDice = 5
        self.diceRolls = [random.randint(1, 6) for _ in range(self.numDice)]

    def rollDice(self):
        self.diceRolls = [random.randint(1, 6) for _ in range(self.numDice)]
