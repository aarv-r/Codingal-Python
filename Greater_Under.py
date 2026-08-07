num1=int(input("Enter first reference number:"))
num2=int(input("Enter test number:"))
if num1>num2:
    print(num1, "is greater than", num2)
elif num1==num2:
    print(num1, "and", num2, "are equal")
else:
    print(num1, "is less than", num2)