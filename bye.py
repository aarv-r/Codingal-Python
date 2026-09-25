valid = False
while not valid:
    try:
        x = int(input("Enter a number: "))
        while x%2 ==0:
            print("Bye")
        valid = True
    except ValueError:
        print("Invalid input")