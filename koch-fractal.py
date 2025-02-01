import turtle
from turtle import Screen
t = turtle.Turtle()
t.speed(0)
t.pencolor("blue")
screen = Screen()



def koch(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length = length/3
        depth -= 1
        koch(length, depth)
        t.right(60)
        koch(length, depth)
        t.left(120)
        koch(length,depth)
        t.right(60)
        koch(length, depth)

t.penup()
t.goto(-150,150)
t.pendown()
for i in range(3):
    koch(200,3)
    t.left(120)

screen.exitonclick()
