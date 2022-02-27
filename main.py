import turtle
import time
import pandas as p

img = './us_map.gif'

screen = turtle.Screen()
screen.bgpic(img)

data = p.read_csv('50_states.csv')
all_states = data['state'].tolist()
guessed_states = []
while len(guessed_states) < len(all_states):
    answer = screen.textinput(title=f'{len(guessed_states)} / 50 Guess the State', prompt='Whats another state').title()
    if answer == "Exit":
        missing_states = [ state for state in all_states if state not in guessed_states]
        new_data = p.DataFrame(missing_states)
        new_data.to_csv('state_to_learn.csv')

        break
    if answer in all_states:
        stateInfo = data[data.state == answer]
        time.sleep(0.2)
        jim = turtle.Turtle()
        jim.hideturtle()
        jim.penup()
        jim.goto(int(stateInfo.x), int(stateInfo.y))
        jim.write(answer)
        guessed_states.append(answer)
        time.sleep(1)

fill_out = True
while fill_out:
    for state in all_states:
        stateInfo = data[data.state == state]
        jim = turtle.Turtle()
        jim.hideturtle()
        jim.penup()
        jim.color('red')
        jim.goto(int(stateInfo.x), int(stateInfo.y))
        jim.write(state)
    fill_out = False

screen.exitonclick()
