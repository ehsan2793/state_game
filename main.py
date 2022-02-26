import turtle
import time
import pandas as p

img = './us_map.gif'

screen = turtle.Screen()
screen.bgpic(img)

data = p.read_csv('50_states.csv')
all_states = data['state'].tolist()
print(data)
guessed_states = []
while len(guessed_states) < len(all_states):
    answer = screen.textinput(title=f'{len(guessed_states)} / 50 Guess the State', prompt='Whats another state').title()
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

screen.exitonclick()
