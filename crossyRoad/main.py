from turtle import Turtle, Screen
from frog import Frog
from cars import Cars
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Frogger")

frog = Frog()
car = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(frog.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(frog.move_speed)
    screen.update()
    car.create_cars()
    car.move_cars()
    
    for vehicle in car.all_cars:
        if vehicle.distance(frog) < 20:
            game_is_on = False
            scoreboard.game_over()

    if frog.ycor() > 290:
        frog.reset()
        scoreboard.point()



screen.exitonclick()


