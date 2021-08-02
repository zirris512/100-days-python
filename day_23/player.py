from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.set_start()
        self.setheading(90)

    def move(self):
        self.forward(10)

    def set_start(self):
        self.setpos(x=0, y=-280)
