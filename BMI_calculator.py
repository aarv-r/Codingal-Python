a=float(input("Enter weight here"))
b=float(input("Enter height here"))
c=a/(b/100)**2
print ("Your BMI is", c)
if c<=18.4:
    print("You are underweight")
elif c<=24.9:
    print("You are healthy")
elif c<=29.9:
    print("You are overweight")
elif c<=34.9:
    print("you are severely overweight")
elif c<=39.9:
    print("you are obese")
else:
    print("you are severely obese")