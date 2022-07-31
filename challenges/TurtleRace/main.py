"""The Turtle Race.
Project for Angela Wu's 100 days of code challenges.
Day # 19
"""
from turtle import Turtle, Screen
from random import randint

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set up screen
screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("lightgreen")

user_bet = screen.textinput("Bets", f"Bet for the winner:\n({' - '.join(colors)})").lower()

# Creating a turtle for each available color
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()        # Prevent drawing
    new_turtle.color(color)   # Setting each color

# Starting Y position
starting_y = -120
# Initial position
for turtle in screen.turtles():     # screen.turtles() list all turtles in the screen
    turtle.goto(x=-270, y=starting_y)
    starting_y += 50

# Starting the RACE
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in screen.turtles():
        turtle.fd(randint(0, 10))       # random forward moves
        if turtle.xcor() >= 280:        # winner
            winner = turtle.pencolor()
            is_race_on = False

if user_bet == winner:
    print("Congratulations! You won!")
else:
    print("You loose :(")
print(f"The winner is: {winner.upper()} TURTLE!")

screen.exitonclick()
