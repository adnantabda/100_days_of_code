from turtle import Turtle
from random import randint


class Food(Turtle):
    """Models the food the snake is going to eat."""
    def __init__(self):
        """Initialize a single circle as food."""
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.respawn()

    def respawn(self):
        """Make the food re-appear in a random point of the screen."""
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(x=random_x, y=random_y)
