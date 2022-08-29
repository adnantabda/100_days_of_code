"""Turtle character configs."""

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Models the turtle character of the game."""
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.go_to_start()
        self.level = 1

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        """Moves the turtle forward."""
        self.forward(MOVE_DISTANCE)

    def is_at_finish(self) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            self.level += 1
            return True
