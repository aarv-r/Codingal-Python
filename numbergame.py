import random
computer = random.randint(1,10)
user=int(input("Guess a number between 1 and 10: "))
if user==computer:
    print("You have won the game")
else:
    print("You have lost the game. The number was", computer)
