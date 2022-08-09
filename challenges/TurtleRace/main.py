"""The Turtle Race.
Project for Angela Wu's 100 days of code challenges.
Day # 19
"""
from turtle import Turtle, Screen
from random import randint, shuffle

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
    new_turtle.speed("slowest")
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
    shuffle(screen.turtles())    # starts at a random turtle
    for turtle in screen.turtles():
        turtle.fd(randint(0, 10))       # random forward moves
        if turtle.xcor() >= 280:  # 300(border of screen) - 20(turtle center)
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("\n\U0001F947 Congratulations! You won! \U0001F947")
            else:
                print("\nYou loose\n¯ \\ _ (ツ) _ / ¯")


print(f"\n\U0001F3C1\U0001F3C1\U0001F3C1 The winner is \U0001F3C1\U0001F3C1\U0001F3C1"
      f"\n\t\U0001F422 {winner.upper()} TURTLE! \U0001F3C6")

screen.exitonclick()
