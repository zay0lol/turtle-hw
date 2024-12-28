import turtle

screen = turtle.Screen()
screen.bgcolor("blue")

pen = turtle.Turtle()

def drawpentagon():
    pen.color("orange")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(100)
        pen.left(72)
    pen.end_fill()

def drawrhombus():
    pen.color("yellow")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(120)
        pen.left(60)
        pen.forward(120)
        pen.left(120)
    pen.end_fill()

pen.penup()
pen.goto(-200, 0)
pen.pendown()
drawpentagon()

pen.penup()
pen.goto(150, 0)
pen.pendown()
drawrhombus()

pen.hideturtle()

turtle.done()
