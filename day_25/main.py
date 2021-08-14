from turtle import Screen, shape
import pandas

from States import States
from Score import Score

image = "blank_states_img.gif"

screen = Screen()
screen.title("U.S. States Game")
screen.addshape(image)
shape(image)

state = States()

score = Score()
score.set_start()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()

game_over = False

while not game_over:
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state's name?"
    )
    formatted_answer = answer_state.lower().title()
    if formatted_answer == "Exit":
        break

    state.check_answer(states_list, formatted_answer)
    if state.correct:
        score.increment_score()
        current_state = states_list[state.state_idx]
        x_pos = x_list[state.state_idx]
        y_pos = y_list[state.state_idx]
        state.print_to_board(current_state, x_pos, y_pos)
        if score.current_score == 50:
            game_over = True
            state.print_win()
    else:
        game_over = True
        state.print_game_over()

missed_states = {
    "Missed States": [
        missed_state
        for missed_state in states_list
        if missed_state not in state.guessed_states
    ]
}
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("states_to_learn.csv")
