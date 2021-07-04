from turtle import Turtle, Screen
import random

did_gun_blast = False
screen = Screen()
screen.setup(width=500, height=400)
userinput = screen.textinput(title="Make a bet.", prompt="Which turtle will win the race? Enter a color: ")

colors_list = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
y_positions = [-70,-40,-10,20,50,80,110]
turtles = []

for turtle_number in range(0,7):
    timur = Turtle(shape="turtle")
    timur.color(colors_list[turtle_number])
    timur.penup()
    timur.goto(x=-230,y=y_positions[turtle_number])
    turtles.append(timur)

if userinput:
    did_gun_blast = True

while did_gun_blast:

    for turtle in turtles:
        if turtle.xcor() > 230:
            did_gun_blast = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == userinput:
                print(f"You've won! The {winning_turtle} turtle has won the race!")
            else:
                print(f"You lost! The {winning_turtle} turtle has won the race!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)




screen.exitonclick()

