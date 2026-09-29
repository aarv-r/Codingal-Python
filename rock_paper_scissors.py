import random
choices = ("rock", "paper", "scissors")
computer = random.choice(choices)
user = input("Enter your choice (rock, paper, scissors): ")
print("Computer's choice:", computer)
if user == computer:
    print("It's a tie")
elif user == "rock":
    if computer == "paper":
        print("You lose! Paper covers rock.")
    else:
        print("You win! Paper covers rock.")
elif user == "paper":
    if computer == "scissors":
        print("You lose! Scissors cut paper.")
    else:
        print("You win! Paper covers rock.")
elif user == "scissors":
    if computer == "rock":
        print("You lose! Rock smashes scissors.")
    else:
        print("You win! Scissors cut paper.")
else:
    print("Invalid option!")