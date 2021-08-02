from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setpos(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.setpos(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.setpos(x=self.xcor(), y=new_y)
