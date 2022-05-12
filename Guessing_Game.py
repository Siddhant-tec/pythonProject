import random
class GuessingGame():
    def __init__(self):
        self.guessed_number = int(input())
        self.number = random.choice([x for x in range(1, 11)])

    def guess(self):
        if self.number == self.guessed_number:
            print("Player guessed Correct!")
        else:
            print("Player Lost!")
            print("Number was", self.number)


plays = int(input())
game = GuessingGame()
for player in range(plays):
    game.guess()
    
