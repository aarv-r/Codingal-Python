import turtle
turtle.Screen().bgcolor("teal")
turtle.Screen().setup(width=600, height=800)
polygon=turtle.Turtle()
sides=int(input("Enter number of sides: "))
sidelength=int(input("Enter length of each side:"))
angle=360/sides
for i in range(sides):
    polygon.forward(sidelength)
    polygon.left(angle)
turtle.done()