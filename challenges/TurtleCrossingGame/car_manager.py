"""The control manager for all the cars in the game."""

from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
SPEED_INCREMENT = 10


class CarManager:
    """Manager to control all cars in the game."""
    def __init__(self):
        """Initializing an empty list to contain the new generated cars."""
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        """If the car is valid (1 in 6 chances), the manager will generate a car
        and place it on the screen.
        """
        is_car_valid = randint(1, 6)    # To slow down the generation of cars rate
        if is_car_valid == 6:           # Proceed to generate the car.
            car = Turtle()
            car.penup()
            car.shape("square")
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(x=300, y=randint(-250, 250))       # sets x and y coordinates
            self.cars.append(car)

    def drive_cars(self):
        """Sets in motion all the generated cars."""
        for car in self.cars:
            car.backward(self.speed)

    def increase_speed(self):
        """Increases all the cars speed by the MOVE_INCREMENT."""
        self.speed += SPEED_INCREMENT
