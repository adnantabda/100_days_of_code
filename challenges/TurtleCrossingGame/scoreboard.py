"""Scoreboard configs."""
from turtle import Turtle
FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):
    """Scoreboard to keep track of the levels and game messages."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def inform_level(self, player) -> None:
        """Displays the current level on the top-right of the screen."""
        self.goto(-260, 280)
        msg = f"Level {player.level}"
        self.write(arg=msg, move=False, align="center", font=FONT)

    def game_over_msg(self) -> None:
        """Displays a GAME OVER message on the center of the screen."""
        self.home()
        self.color("red")
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
