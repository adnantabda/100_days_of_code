"""Snake Game.
Project for Angela Wu's 100 days of code challenges.
"""
from time import sleep
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen setups:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off animation

scoreboard = Scoreboard()
snake = Snake()
food = Food()

# Controlling the snake with keyboard arrows
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")

game_over = False
while not game_over:
    screen.update()  # show screen that was turned off - line 16
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.respawn()
        snake.grow()

    # Detect collision with screen borders and tail
    if snake.collide_with_border() or snake.collide_with_tail():
        scoreboard.loose_life()
        if scoreboard.lives > 0:
            snake.reset_snake()
        # Game Over
        elif scoreboard.lives == 0:
            scoreboard.end_game()
            game_over = True


screen.exitonclick()
