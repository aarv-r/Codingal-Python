n=int(input("Enter number you would like to have the sum of whole numbers with:"))
sum=0
for i in range(0,n+1):
    sum=sum+i
print(f"The sum of whole numbers from 0 to {n} is: {sum}")