import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"

# To add this image in screen first
screen.addshape(image)
screen.title("US State Game")

turtle.shape(image)

data = pandas.read_csv("./50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50 states correct", "What's the state name?").title()
    if answer in all_states:
        guessed_states.append(answer)
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        country_data = data[data.state == answer]
        x_cor = country_data.x
        y_cor = country_data.y
        tim.goto(int(x_cor), int(y_cor))
        tim.write(answer)
        # or can write country_data.state.item() instead of answer to get the first item




screen.exitonclick()