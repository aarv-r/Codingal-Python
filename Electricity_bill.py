Electricity=int(input("Enter electricity units consumed here:"))
if Electricity<50:
    print("you have to pay", Electricity*2.60+25)
elif Electricity>=50 and Electricity<=100:
    print("you have to pay", Electricity*3.25+35)
elif Electricity>100 and Electricity<200:
    print("you have to pay", Electricity*5.26+45)
else:
    print("you have to pay", Electricity*8.45+75)