from turtle import Turtle, Screen
from frog import Frog
from cars import Cars
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Frogger")

frog = Frog()
car = Cars(0,0)

def random_car():
    random_x = random.randrange(-280,280,10)
    return (random_x, 300)
    print(random_x)

random_car()

screen.listen()
screen.onkey(frog.up, "Up")
screen.onkey(frog.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    





screen.exitonclick()


