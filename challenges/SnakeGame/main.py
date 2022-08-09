"""Snake Game.
Project for Angela Wu's 100 days of code challenges.
Day # 20
"""
from time import sleep
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Screen setup:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off animation

scoreboard = Scoreboard()
snake = Snake()
food = Food()

# Controlling the snake
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")


# Animation
game_over = False
while not game_over:
    screen.update()                 # show screen that was turned off
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.respawn()
        snake.grow()



    # TODO: 1. Detect collision with tail
    for segment in snake.tail:
        if snake.head.distance(segment) < 15:
            game_over = True
            scoreboard.end_game()

    # TODO: 2. Detect collision with screen borders




screen.exitonclick()
