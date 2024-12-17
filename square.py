import turtle

turtle.Screen().bgcolor("Orange")
turtle.Screen().setup(500,500)
turtle.title("Welcome to turtle")

t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()