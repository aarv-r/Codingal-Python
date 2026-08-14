health=input("Enter your health cause here (Yes/no):")
if health=="yes":
    print("You can take the exam")
else:
    attendance=int(input("Enter your attendance percentage here"))
    if attendance>=75:
        print("You can take the exam")
    else:
        print("You cannot take the exam")
