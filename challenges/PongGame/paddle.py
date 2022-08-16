"""Right and left professional paddles of the game."""
from turtle import Turtle

RIGHT_PADDLE_POSITION = (450, 0)
LEFT_PADDLE_POSITION = (-450, 0)


class Paddle(Turtle):
    """Models the paddles for the game."""
    def __init__(self, position: str):
        """Initialize the right paddle."""
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if position == "right":
            self.goto(RIGHT_PADDLE_POSITION)
        elif position == "left":
            self.goto(LEFT_PADDLE_POSITION)

    # Movement
    def up(self) -> None:
        """Makes the paddle go up by 20 pixels."""
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self) -> None:
        """Makes the paddle go down by 20 pixels."""
        self.goto(x=self.xcor(), y=self.ycor() - 20)
