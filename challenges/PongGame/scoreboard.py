"""The scoreboard of the game that keeps track of the game results."""
import time
from turtle import Turtle
from screen_configs import right_score_position, left_score_position


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = {"right": 0, "left": 0}
        self.hideturtle()
        self.penup()
        self.inform_score()

    def inform_score(self) -> None:
        """Set the score on the top of the screen and
        updates the current score clearing up the previous one.
        """
        self.color("white")
        self.clear()    # Prevents writing over each score
        # Right Score
        self.goto(right_score_position)
        self.write(arg=self.score["right"], move=False, align="center", font=("Courier", 80, "normal"))
        # Left Score
        self.goto(left_score_position)
        self.write(arg=self.score["left"], move=False, align="center", font=("Courier", 80, "normal"))

    def count_point(self, ball: Turtle) -> None:
        """Displays a message on the screen and checks on which side is the ball
        to count a point to the opposite player.
        """
        if ball.xcor() < 0:  # Ball is on the left side
            self.score["right"] += 1
        else:   # Ball on the right side
            self.score["left"] += 1
        self.home()
        self.color("blue")
        self.write(arg="Point!", move=False, align="center", font=("Courier", 80, "normal"))
        time.sleep(0.3)
        self.clear()

    def final_score(self):
        """Displays a message on the screen informing the game is over."""
        self.home()
        self.color("red")
        self.write(arg="Game Over", move=False, align="center", font=("Courier", 80, "normal"))
        time.sleep(0.3)
