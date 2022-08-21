import turtle
import pandas
import csv


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# screen.bgpic("./blank_states_img.gif")
guessed_states = []

data = pandas.read_csv("./50_states.csv")
states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=(f"{len(guessed_states)}/50 States So Far"), prompt="What's another state's name?").title()
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_coords = data[data.state == answer_state]
        t.goto(int(state_coords.x), int(state_coords.y))
        t.write(state_coords.state.item())
        print(guessed_states)
    elif answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
        
screen.exitonclick()