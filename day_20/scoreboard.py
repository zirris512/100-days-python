from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()
