import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(5)

# Function to move the turtle without drawing
def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

# Function to draw a line segment
def draw_segment(x1, y1, x2, y2):
    move(x1, y1)
    pen.goto(x2, y2)


# Function to draw サ (sa)
def draw_sa():
    draw_segment(-300,70,-230,70)
    draw_segment(-280,90,-280,50)
    draw_segment(-250,90,-250,30)
    pen.setheading(-10)
    pen.circle(-40,-30)

    # draw_segment()
def draw_mi():
    draw_segment(-200,90,-150,70)
    draw_segment(-200,70,-150,50)
    draw_segment(-200,50,-150,30)

def draw_small_ya():
    draw_segment(-120,90,-110,30)
    draw_segment(-140,80,-80,80)
    draw_segment(-80,80,-100,50)

def draw_ku():
    draw_segment(-40,90,-65,65)
    draw_segment(-50,77,-20,77)
    pen.setheading(-80)
    pen.circle(-50,70)
#     draw_segment()
# def draw_mi():
#     # Top horizontal line
#     draw_segment(-160, 50, -140, 50)
#     # Middle horizontal line
#     draw_segment(-160, 40, -140, 40)
#     # Bottom horizontal line
#     draw_segment(-160, 30, -140, 30)

# # Function to draw ャ (small ya)
# def draw_small_ya():
#     # Small curve
#     move(-120, 40)
#     pen.goto(-110, 40)
#     pen.goto(-115, 30)

# # Function to draw ク (ku)
# def draw_ku():
#     # Top horizontal line
#     draw_segment(-90, 50, -70, 50)
#     # Diagonal line
#     draw_segment(-90, 50, -80, 30)
#     # Bottom horizontal line
#     draw_segment(-80, 30, -70, 30)

# Draw the name サミャック
draw_sa()       # サ
draw_mi()       # ミ
draw_small_ya() # ャ
draw_ku()       # ク

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()