"""Official ball used to play the game."""
from turtle import Turtle


class Ball(Turtle):
    """Models the ball for the game."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(65, 255, 0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.setheading(50)         # Starting angle
        self.difficulty = 10        # Starting speed

    def bounce(self):
        """Sets a new heading for the wall after bounces with a border."""
        new_angle = self.heading() * -1
        self.setheading(new_angle)

    def hit(self, against: Turtle) -> None:
        """Takes the angle the ball is hitting an objectand sets the new
        heading of the ball to the opposite angle it hit the object.
        """
        new_angle = against.towards(self) * -1  # Opposite angle of impact
        self.setheading(new_angle)
        self.difficulty += 1        # Increases the ball speed with each hit

    def point(self) -> None:
        """Resets the ball's speed, sets the ball on the center of screen
        and changes it's direction to the opposite angle.
        """
        self.difficulty = 10        # Resets the original speed
        self.goto(0, 0)
        self.setheading(self.heading() + 180)
