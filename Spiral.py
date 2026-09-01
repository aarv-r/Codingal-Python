import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().title("Spiral Drawing")
mypen=turtle.Turtle()
mypen.speed(100)
mypen.color("red")
for i in range(100):
    mypen.forward(i*2)
    mypen.right(90)
turtle.done()