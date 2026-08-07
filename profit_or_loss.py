sp=float(input("Enter selling price:"))
cp=float(input("Enter cost price:"))
if sp>cp:
    print("profit",sp-cp)
elif sp==cp:
    print("No profit no loss")
else:
    print("Loss",cp-sp)