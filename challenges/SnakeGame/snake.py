from turtle import Turtle


class Snake:
    """Models the snake's body and functions for the game."""
    def __init__(self):
        """Initialize the snake with a 3 segment body."""
        self.snake_body = []
        starting_xposition = 0
        for _ in range(3):  # Starting body
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.goto(x=starting_xposition, y=0)
            self.snake_body.append(snake_segment)
            starting_xposition -= 20                    # each square 20x20
        self.head = self.snake_body[0]

    def move(self):
        """Keeps the snake moving and its head in the front."""
        for segment_index in range(len(self.snake_body)-1, 0, -1):  # Reverse order
            new_position = (          # X and Y coordinates of the previous segment
                            self.snake_body[segment_index - 1].xcor(),
                            self.snake_body[segment_index - 1].ycor(),
                            )
            self.snake_body[segment_index].goto(new_position)
        self.head.fd(20)

    def grow(self):
        """Increment the snake by 1 segment."""
        new_snake_segment = Turtle(shape="square")
        new_snake_segment.penup()
        new_snake_segment.color("white")
        last_position = self.snake_body[-1].pos()
        new_snake_segment.goto(last_position)
        self.snake_body.append(new_snake_segment)

    def up(self):
        """Turns the snake up."""
        if self.head.heading() != 270:  # Avoid turning 180 degrees
            self.head.setheading(90)

    def left(self):
        """Turns the snake left."""
        if self.head.heading() != 0:  # Avoid turning 180 degrees
            self.head.setheading(180)

    def down(self):
        """Turns the snake down."""
        if self.head.heading() != 90:  # Avoid turning 180 degrees
            self.head.setheading(270)

    def right(self):
        """Turns the snake right."""
        if self.head.heading() != 180:  # Avoid turning 180 degrees
            self.head.setheading(0)
