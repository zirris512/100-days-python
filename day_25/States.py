from turtle import Turtle


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.correct = False
        self.state_idx = None
        self.guessed_states = []

    def check_answer(self, answers: list, guess: str):
        self.correct = False
        if guess in answers and guess not in self.guessed_states:
            self.state_idx = answers.index(guess)
            self.guessed_states.append(answers[self.state_idx])
            self.correct = True

    def print_to_board(self, state: str, x: int, y: int):
        self.setpos(x, y)
        self.write(state, align="center")

    def print_game_over(self):
        self.setpos(0, 684 / 2 - 40)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))

    def print_win(self):
        self.setpos(0, 684 / 2 - 40)
        self.write("You win!", align="center", font=("Arial", 20, "normal"))
