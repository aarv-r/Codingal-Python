def hotel_pricing(days, rent):
    return days*rent
def airplane_ticket_pricing(people, amount):
    return people*amount
def food(people, amount):
    return people*amount

a=int(input("Enter the number of days you will stay in the hotel: "))
b=int(input("Enter the rent per day for the hotel: "))
c=int(input("Enter the number of people traveling: "))
d=int(input("enter the pricing of tickets: "))
e=int(input("Enter the price of food per person: "))

total=hotel_pricing(a, b) + airplane_ticket_pricing(c, d) + food(c, e)
print("Total expenditure= ", total)