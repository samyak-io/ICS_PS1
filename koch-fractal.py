import turtle
from turtle import Screen
t = turtle.Turtle()
t.speed(0)
t.pencolor("blue")
screen = Screen()



def koch(length, step):
    if step == 0:
        t.forward(length)
    else:
        length = length/3
        step -= 1
        koch(length, step)
        t.right(60)
        koch(length, step)
        t.left(120)
        koch(length,step)
        t.right(60)
        koch(length,step)

t.penup()
t.goto(-150,150)
t.pendown()
for i in range(3):
    koch(200,3)
    t.left(120)

screen.exitonclick()