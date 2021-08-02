from turtle import Turtle
from random import choice, randint

COLORS = [
    "darkgreen",
    "blue",
    "purple",
    "red",
    "orange",
    "cyan",
    "teal",
    "brown",
    "pink",
]
SPEED_INCREMENT = 5


class Cars:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = 5

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.setpos(320, randint(-250, 250))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def update_speed(self):
        self.car_speed += SPEED_INCREMENT

    def restart(self):
        for car in self.cars:
            car.setpos(-400, 0)
        self.cars = []
