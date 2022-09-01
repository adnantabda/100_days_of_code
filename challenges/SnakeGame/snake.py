"""Snake's set ups and controls."""
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # coordinates for snake position.
TOP_BORDER = RIGHT_BORDER = 290
BOTTOM_BORDER = LEFT_BORDER = -290


class Snake:
    """Models the snake's body and functions for the game."""
    def __init__(self):
        """Initialize the snake with a 3 segment body."""
        self.body = []
        self.generate_snake()
        self.head = self.body[0]

    def generate_snake(self):
        for position in STARTING_POSITIONS:  # Starting body
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.goto(position)
            self.body.append(snake_segment)
        self.head = self.body[0]

    def move(self):
        """Keeps the snake moving and its head in the front."""
        for segment_index in range(len(self.body)-1, 0, -1):  # Reverse order
            new_position = (  # X and Y coordinates of the previous segment
                            self.body[segment_index - 1].xcor(),
                            self.body[segment_index - 1].ycor(),
                            )
            self.body[segment_index].goto(new_position)
        self.head.fd(20)

    def grow(self):
        """Increment the snake by 1 segment."""
        new_snake_segment = Turtle(shape="square")
        new_snake_segment.penup()
        new_snake_segment.color("white")
        last_position = self.body[-1].pos()
        new_snake_segment.goto(last_position)
        self.body.append(new_snake_segment)

    def up(self):
        """Turns the snake's head to the top of the screen."""
        if self.head.heading() != 270:  # Avoid turning 180 degrees
            self.head.setheading(90)

    def left(self):
        """Turns the snake's head to the left of the screen."""
        if self.head.heading() != 0:  # Avoid turning 180 degrees
            self.head.setheading(180)

    def down(self):
        """Turns the snake's head to the bottom of the screen."""
        if self.head.heading() != 90:  # Avoid turning 180 degrees
            self.head.setheading(270)

    def right(self):
        """Turns the snake's head to the right of the screen."""
        if self.head.heading() != 180:  # Avoid turning 180 degrees
            self.head.setheading(0)

    def collide_with_border(self):  # Detect collision with borders
        """Returns True if the snake collided with any screen borders."""
        if (self.head.xcor() > RIGHT_BORDER or
           self.head.xcor() < LEFT_BORDER or
           self.head.ycor() > TOP_BORDER or
           self.head.ycor() < BOTTOM_BORDER):
            return True

    def collide_with_tail(self):
        """Returns True if the head of the snake collided with it's tail."""
        for segment in self.body[1:]:
            if self.head.distance(segment) < 15:
                return True

    def reset_snake(self):
        for segment in self.body:
            segment.reset()
        self.body = []  # Generate a new empty snake
        self.generate_snake()
