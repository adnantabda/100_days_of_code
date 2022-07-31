"""Faking Damien Hirst.
Project for Angela Wu's 100 days of code challenges.
Day # 18
"""
import colorgram
import random
from turtle import Turtle, colormode, Screen

# Extract 50 colors from image (returns an object) // colorgram module
colors = colorgram.extract("hirst.jpg", 50)

colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors_list.append(new_color)

# Screen config
screen = Screen()
screen.title("Faking Damien Hirst")
colormode(255)  # Documentation (to use rgb colors between 0 and 255)

# turtle initial settings
artist = Turtle(shape="classic", visible=False)
artist.penup()      # Doesn't draw when moves
artist.speed("fastest")

# Setting starting position
x_position = -230
y_position = -200
artist.goto(x_position, y_position)

while y_position < 300:                             # 10 rows
    for _ in range(10):                             # 10 columns
        artist.dot(20, random.choice(colors_list))  # Draw a dot size 20; color random
        artist.forward(50)
    y_position += 50
    artist.goto(x_position, y_position)             # Go up for another row

# Click on screen to end and exit
screen.exitonclick()
