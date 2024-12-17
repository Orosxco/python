import turtle

turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(500,500)
turtle.title("Welcome to turtle")

u = turtle.Turtle()

u.left(70)
u.forward(100)
u.right(140)
u.forward(105)
u.right(150)
u.forward(110)
u.right(140)
u.forward(90)
u.right(140)
u.forward(100)

u.penup()

u.right(40)
u.forward(150)

u.pendown()

for i in range(3):
    u.right(120)
    u.forward(100)

u.penup()

u.right(90)
u.forward(60)
u.right(90)

u.pendown()

for i in range(3):
    u.forward(100)
    u.right(120)

turtle.done()
