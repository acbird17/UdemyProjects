from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.set_color()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def set_color(self):
        self.colormode(255)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return self.color(r, g, b)