sum=0
num=int(input("Enter number here:"))
temp=num
while num>0:
    rem=num%10
    sum=sum+rem**3
    num=num//10
if temp==sum:
    print("This is an Armstrong number")
else:
    print("This is not an armstrong number")