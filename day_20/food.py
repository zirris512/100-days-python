from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_loc = (randrange(-280, 280, 20), randrange(-280, 280, 20))
        self.setpos(random_loc)
