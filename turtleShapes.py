import turtle
import random

timmy = turtle.Turtle()
timmy.pensize(10)
timmy.speed(10)

def set_color():
    turtle.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return timmy.pencolor(r, g, b)

def random_walk():
    angles = [90, 180, 270, 360]
    angle = random.choice(angles)
    # angle = 360 / sides
    # for _ in range (50):
    timmy.right(angle)
    timmy.forward(25)
    
while 1 > 0:
    set_color()
    random_walk()

screen = turtle.Screen()
screen.exitonclick()
