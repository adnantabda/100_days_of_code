"""Etch-A-sKetch.
Project for Angela Wu's 100 days of code challenges.
Day # 19
"""
from turtle import Turtle, Screen, resetscreen


def draw_fd():
    """Draws a straight line of 10 pcs."""
    pen.fd(10)


def draw_bk():
    """Draws a straight line of 10 pcs backwards to the pen heading."""
    pen.bk(10)


def clockwise():
    """Turns the pen clockwise by 10 degrees."""
    pen.setheading(pen.heading() - 10)


def counter_clockwise():
    """Turns the pen counter-clockwise by 10 degrees."""
    pen.setheading(pen.heading() + 10)


screen = Screen()
pen = Turtle(shape="classic")

# Event listeners
screen.listen()
screen.onkey(fun=draw_fd, key="Up")
screen.onkey(fun=draw_bk, key="Down")
screen.onkey(fun=clockwise, key="Right")
screen.onkey(fun=counter_clockwise, key="Left")
screen.onkey(fun=resetscreen, key="c")

screen.exitonclick()
