from turtle import Turtle, Screen
import random

race_on=False

screen=Screen()
screen.setup(height=400, width=500)
bet=screen.textinput(title="Make your bet.", prompt="Guess which turtle will win the race.")

colors=["red","green","blue","black","orange","yellow"]
y_pos=[-70,-40,-10,20,50,80]
all_turtle=[]

for i in range(6):
    new_turtle= Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtle.append(new_turtle)

if bet:
    race_on=True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_on=False
            turtle_col= turtle.pencolor()
            if turtle_col == bet.lower():
                print("You have won !")
            else:
                print(f"You lost, winner is {turtle_col} turtle !")
        distance=random.randint(0,11)
        turtle.forward(distance)

screen.exitonclick()