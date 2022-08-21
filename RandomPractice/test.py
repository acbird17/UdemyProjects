from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)


def draw_line():
    dash = Turtle()
    dash.pensize(2)
    dash.penup()
    dash.pencolor("white")
    dash.setheading(270)
    dash.forward(200)
    dash.setheading(90)
    for _ in range(13):
        dash.pendown()
        dash.forward(50)
        dash.penup()
        dash.forward(50)
        
draw_line()       
screen.exitonclick()
