num=input("Enter your number here:")
n=len(num)
if n%2==1:
    print(int(num[n//2]))
else:
    print(int(num[n//2])*int(num[n//2-1]))