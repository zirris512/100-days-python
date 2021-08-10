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
        self.high_score = 0
        self.get_high_score()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGN,
            font=FONT,
        )

    def get_high_score(self):
        try:
            with open("high_score.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("high_score.txt", mode="w") as file:
                file.write("0")

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()
