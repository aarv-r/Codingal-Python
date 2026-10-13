weather=(1,1,0,0,0,1,1)
sunny=weather.count(0)
print("sunny chance = ", sunny)
rainy=weather.count(1)
print("rainy chance = ", rainy)

if sunny>rainy:
    print("day is sunny")
elif rainy>sunny:
    print("day is rainy")
else:
    print("day is cloudy")