import turtle
from turtle import Screen
import math

# Setup Turtle
turtle.speed(0)  # Fastest rendering
turtle.hideturtle()
turtle.bgcolor("white")
screen = Screen()
turtle.pencolor("red")


def draw_circle(x, y, radius):
    """Draws a circle outline at (x, y) with a given radius."""
    turtle.penup()
    turtle.goto(x, y - radius)  # Move to the bottom of the circle
    turtle.pendown()
    turtle.circle(radius)


# Parameters for the imaginary circle that holds the 10 outer circles
imaginary_circle_radius = 100  # Distance of the outer circles from center
outer_circle_radius = 200  # Size of each outer circle
num_outer_circles = 10  # Number of outer circles

def draw_ashoka_logo():
    turtle.color("red")

    # Draw the 10 evenly spaced outer circles
    for i in range(num_outer_circles):
        angle = i * (360 / num_outer_circles)  # Equal spacing around the imaginary circle
        x = imaginary_circle_radius * math.cos(math.radians(angle))
        y = imaginary_circle_radius * math.sin(math.radians(angle))

        draw_circle(x, y, outer_circle_radius)

    # 4 Central Circles (with different radii) centered at (0,0)
    central_circle_radii = [145, 172.5, 206, 243, 271.5, 300]  # Varying sizes

    for radius in central_circle_radii:
        draw_circle(0, 0, radius)

    #remove the middle circle
    turtle.color("white")
    turtle.pensize(7)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(0,-110)
    turtle.circle(110,360,20)
    # turtle.circle(100,360,10)
    turtle.end_fill()
    
    turtle.pensize(1)
    turtle.color("red")
    draw_circle(0,0,125)

draw_ashoka_logo()


# Display the final result (no animation)
turtle.done()
