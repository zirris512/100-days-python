from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_score = 0

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.current_score}/50",
            align="center",
            font=("Arial", 16, "normal"),
        )

    def set_start(self):
        self.setpos(-684 / 2 + 60, 684 / 2 - 40)
        self.update_scoreboard()

    def increment_score(self):
        self.current_score += 1
        self.update_scoreboard()
