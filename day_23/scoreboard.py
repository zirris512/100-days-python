from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_score()

    def create_score(self):
        self.penup()
        self.hideturtle()
        self.setpos(-240, 260)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(
            f"Level: {self.level}", align="center", font=("Courier", 12, "normal")
        )

    def update_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over", align="center", font=("Courier", 16, "normal"))
