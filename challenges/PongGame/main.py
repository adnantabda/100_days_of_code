"""Pong Game.
Project for Angela Wu's 100 days of code challenges.
"""
import time
from turtle import Screen
from screen_configs import SCREEN_WIDTH, SCREEN_HEIGHT, TOP_BORDER, BOTTOM_BORDER, RIGHT_BORDER, LEFT_BORDER
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# Screen setup
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)            # turns off screen

# Init paddles and ball
l_paddle = Paddle(position="left")
r_paddle = Paddle(position="right")
ball = Ball()
scoreboard = Scoreboard()

# Controlling left and right paddle:
screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

game_over = False
while not game_over:
    time.sleep(0.05)        # secs for refreshing screen
    screen.update()
    ball.fd(ball.difficulty)
    scoreboard.inform_score()

    # Collision with top and bottom borders
    if ball.ycor() > TOP_BORDER or ball.ycor() < BOTTOM_BORDER:
        ball.bounce()

    # Collision with RIGHT paddle --> (paddles= 100 pixels * 20 pixels)
    if (ball.distance(r_paddle) < 50) and (ball.xcor() > (r_paddle.xcor() - 20)):
        ball.hit(r_paddle)

    # Collision with LEFT paddle
    if (ball.distance(l_paddle) < 50) and (ball.xcor() < (l_paddle.xcor() + 20)):
        ball.hit(l_paddle)

    # Detect a point
    if ball.xcor() > RIGHT_BORDER or ball.xcor() < LEFT_BORDER:
        scoreboard.count_point(ball=ball)
        ball.point()

    # End game
    if scoreboard.score["right"] == 10 or scoreboard.score["left"] == 10:
        scoreboard.final_score()
        game_over = True

screen.exitonclick()
