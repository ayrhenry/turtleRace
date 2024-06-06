from turtle import *
from random import *

is_race_on = False
timmy = Turtle()
screen = Screen()
random = Random()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
turtle_objs = []

y_cor = -120

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors.pop())
    new_turtle.penup()
    turtle_objs.append(new_turtle)
    new_turtle.goto(-230, y_cor)
    y_cor += 50

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_objs:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            print(f"{winning_color} won!")
            is_race_on = False
            if winning_color == user_bet.lower():
                print("You won!")
            else:
                print("You lost!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        


screen.exitonclick()
