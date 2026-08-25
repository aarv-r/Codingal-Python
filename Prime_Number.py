low=int(input("Enter your minimum range here: "))
high=int(input("Enter you maximum range here: "))
for num in range(low,high+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num, "Is a prime number")