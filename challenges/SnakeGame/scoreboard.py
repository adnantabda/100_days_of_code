"""The scoreboard module for the game."""
from turtle import Turtle

SCORE_FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Times New Roman", 25, "bold")


class Scoreboard(Turtle):
    """Keeps track of the score."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        with open("high_score.txt") as high_score:
            self.high_score = int(high_score.read())
        self.lives = 5
        self.goto(x=0, y=280)
        self.inform_score()

    def inform_score(self):
        """Updates and writes the current score on the screen."""
        self.clear()
        info = f"Score: {self.score} - High Score: {self.high_score} - " \
               f"Lives: {self.lives}"
        self.write(arg=info, move=False, align="center", font=SCORE_FONT)

    def increase_score(self):
        """Increase the score by 1 point and refresh the scoreboard information."""
        self.score += 1
        self.inform_score()

    def loose_life(self):
        """Check for the high score and resets the score."""
        self.lives -= 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(str(self.high_score))
        self.score = 0
        self.inform_score()

    def end_game(self):
        """Prints the game over message on the screen when the player looses."""
        self.home()         # Moves the turtle to home coordinates (0, 0)
        self.color("yellow")
        self.write(arg=f"GAME OVER", move=False, align="center", font=GAME_OVER_FONT)
