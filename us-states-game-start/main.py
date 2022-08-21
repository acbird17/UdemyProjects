import turtle
import pandas
import csv


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# screen.bgpic("./blank_states_img.gif")

data = pandas.read_csv("./50_states.csv")
states = data.state.to_list()
print(states)


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

if answer_state in states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_coords = data[data.state == answer_state]
    t.goto(int(state_coords.x), int(state_coords.y))
    t.write(state_coords.state)
print(answer_state)
screen.mainloop()