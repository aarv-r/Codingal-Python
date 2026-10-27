import random
name = input("Please enter your name: ")
number=random.randint(1, 100)
print("Hello", name, "Guess a number between 1 and 100")
if number%2==0:
    print("The number is even.")
else:
    print("The number is odd.")
for i in range(0, 6):
    choice=int(input("Enter your guess: "))
    if choice==number:
        print("Congrats! You guessed the number correctly.")
        break
    elif number>choice:
        print("The number is greater than your guess.")
    elif number<choice:
        print("The number is less than your guess.")
else:
    print("Game over! The number was", number)
    