rows=int(input("Enter number of rows wanted for pyramid: "))
for i in range(rows):
    for j in range(1+i):
        print("* ", end=" ")
    print("")