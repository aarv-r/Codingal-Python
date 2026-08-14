choice=input("Enter you choice of vehicle (Car/Bike)")
if choice=="car":
    print("You have chosen car")
    car=input("Enter your car choice here (Sports/Luxury)")
    if car=="sports":
        print("You have chosen the sports car")
    elif car=="Luxury":
        print("You have chosen the luxury car")
elif choice=="bike":
    print("You have chosen bike")
    bike=input("Enter your bike choice here (Bullet/Speed)")
    if bike=="bullet":
        print("You have chosen the bullet bike")
    elif bike=="speed":
        print("You have chosen the speed bike")
else:
    print(choice, "is not available")