import turtle
import pandas as p

img = './us_map.gif'

screen = turtle.Screen()
screen.bgpic(img)

data = p.read_csv('50_states.csv')
all_states = data['state'].tolist()
print(data)

answer = screen.textinput(title='Guess the State', prompt='Whats another state')
if answer in all_states:
    stateInfo = data[data.state == answer]
    jim = turtle.Turtle()
    jim.hideturtle()
    jim.penup()
    jim.goto(int(stateInfo.x), int(stateInfo.y))
    jim.write(answer)

screen.exitonclick()
