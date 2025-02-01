import turtle
from turtle import Screen
# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(10)

turtle.screensize(canvwidth=400, canvheight=300, 
                  bg="skyblue")
screen = Screen()
screen.setup(1000, 400)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Function to draw the letter 'S'
def draw_S():
    t.setheading(0)
    t.forward(50)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)

# Function to draw the letter 'A'
def draw_A():
    t.setheading(0)
    t.left(75)
    t.forward(100)
    t.right(150)
    t.forward(100)
    t.backward(50)
    t.right(105)
    t.forward(30)

# Function to draw the letter 'M'
def draw_M():
    t.setheading(90)
    t.forward(100)
    t.right(135)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.right(135)
    t.forward(100)

# Function to draw the letter 'Y'
def draw_Y():
    t.setheading(90)
    t.forward(50)
    t.left(30)
    t.forward(60)
    t.backward(60)
    t.right(60)
    t.forward(60)
    t.backward(60)
    t.left(30)
    t.backward(50)

# Function to draw the letter 'K'
def draw_K():
    t.setheading(90)
    t.forward(100)
    t.backward(50)
    t.right(45)
    t.forward(70)
    t.backward(70)
    t.right(90)
    t.forward(70)

# Function to draw the letter 'H'
def draw_H():
    t.setheading(90)
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.backward(100)

# Function to draw the letter 'O'
def draw_O():
    t.setheading(0)
    t.circle(50)

# Function to draw the letter 'B'
def draw_B():
    t.setheading(90)
    t.forward(100)
    t.right(90)
    for _ in range(2):
        t.circle(-25, 180)
        t.right(180)

# Function to draw the letter 'R'
def draw_R():
    t.setheading(90)
    t.forward(100)
    t.right(90)
    t.circle(-25, 180)
    t.setheading(-45)
    t.forward(70)

# Function to draw the letter 'G'
def draw_G():
    t.setheading(0)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.circle(-30,200)

# Function to draw the letter 'D'
def draw_D():
    t.setheading(90)
    t.forward(100)
    t.right(90)
    t.circle(-50, 180)

# Function to draw the letter 'E'
def draw_E():
    t.setheading(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)

# "Samyak"
move(-300, 98)
draw_S()

move(-220, 0)
draw_A()
print(t.pos())

move(-150, 0)
draw_M()

move(-5, 0)
draw_Y()

move(22, 0)
draw_A()

move(90, 0)
draw_K()

# "Khobragade"
move(-300, -150)
draw_K()

move(-220, -150)
draw_H()

move(-100, -150)
draw_O()

move(-25, -150)
draw_B()

move(17, -150)
draw_R()

move(80, -150)
draw_A()

move(173, -150)
draw_G()

move(200, -150)
draw_A()

move(280, -150)
draw_D()

move(350, -150)
draw_E()



t.hideturtle()
turtle.done()