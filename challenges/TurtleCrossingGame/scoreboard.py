"""Scoreboard configs."""
from turtle import Turtle
LEVEL_FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):
    """Scoreboard to keep track of the levels and game messages."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1

    def inform_level(self,) -> None:
        """Displays the current level on the top-right of the screen."""
        self.clear()
        self.goto(-290, 280)
        msg = f"Level {self.level}"
        self.write(arg=msg, move=False, align="left", font=LEVEL_FONT)

    def game_over_msg(self) -> None:
        """Displays a GAME OVER message on the center of the screen."""
        self.home()
        self.color("red")
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
