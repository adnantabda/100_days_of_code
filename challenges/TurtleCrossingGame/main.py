"""Turtle Crossig Game.
Project for Angela Wu's 100 days of code challenges.
"""
from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setups
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)         # Turns off animation
screen.colormode(255)    # Range of colors from 0 to 255

car_manager = CarManager()
crossing_turtle = Player()
scoreboard = Scoreboard()

# Keyboard control
screen.listen()
screen.onkeypress(fun=crossing_turtle.move, key="Up")

game_over = False
while not game_over:
    sleep(0.1)          # Animation effect
    screen.update()     # Refresh the screen --> line: 9

    scoreboard.inform_level()
    car_manager.generate_car()
    car_manager.drive_cars()

    # Detect collision
    for car in car_manager.cars:
        if car.distance(crossing_turtle) < 27:  # Best distance for graphic effect.
            scoreboard.game_over_msg()
            game_over = True

    # Next level
    if crossing_turtle.is_at_finish():
        scoreboard.level += 1
        crossing_turtle.go_to_start()
        car_manager.increase_speed()

screen.exitonclick()
