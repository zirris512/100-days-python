# 10 x 10 grid of dots
# 20 radius circles
# 50 pace gap
from turtle import Turtle, Screen
from random import choice

from colors import rgb_colors


def choose_color():
    return choice(rgb_colors)


def initialize_turtle():
    dot.speed(8)
    dot.hideturtle()
    dot.penup()
    dot.setpos(-250, -250)


dot = Turtle()
screen = Screen()
screen.colormode(255)

initialize_turtle()

for _ in range(10):
    for _ in range(10):
        dot.dot(20, choose_color())
        dot.forward(50)
    dot.setpos(-250, dot.ycor() + 50)

screen.exitonclick()
