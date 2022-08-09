"""A scoreboard to keep track of the game points."""
from turtle import Turtle

ALIGMENT = "center"
SCORE_FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Times New Roman", 25, "bold")


class Scoreboard(Turtle):
    """Keeps track of the score."""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(280)
        self.color("white")
        self.score = 0
        self.inform_score()

    def inform_score(self):
        """Updates and writes the current score on the screen."""
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGMENT, font=SCORE_FONT)

    def increase_score(self):
        """Increase the score by 1 point and refresh the scoreboard information."""
        self.clear()
        self.score += 1
        self.inform_score()

    def end_game(self):
        """Prints the game over message on the screen when the player looses."""
        self.home()         # Moves the turtle to home coordinates (0, 0)
        self.color("yellow")
        self.write(arg=f"GAME OVER", move=False, align=ALIGMENT, font=GAME_OVER_FONT)
