rows=int(input("Enter number of rows wanted for pyramid: "))
num=1
for i in range(rows):
    for j in range(1+i):
        print(num, end=" ")
        num=num+1
    print("")