
from turtle import Turtle
WIDTH = 10
HEIGHT = 50
STARTING_POS = [(350, 0), (-350, 0)]


class Paddle:
    def __init__(self):
        self.paddles = []
        self.start_game()
        self.draw_line()
        self.current_x = int(self.paddles[0].xcor())
        self.current_y = int(self.paddles[0].ycor())

    def start_game(self):
        for pos in STARTING_POS:
            self.create_paddles(pos)

    def draw_line(self):
        bot = Turtle()
        bot.color("white")
        bot.penup()
        bot.goto(0, -300)
        bot.pendown()
        bot.setheading(90)
        bot.forward(600)
        bot.hideturtle()

    def create_paddles(self, pos):
        paddle = Turtle("square")
        paddle.turtlesize(stretch_wid=5, stretch_len=1)
        paddle.color("white")
        paddle.penup()
        paddle.goto(pos)
        self.paddles.append(paddle)

    def up(self):
        current_x = int(self.paddles[0].xcor())
        current_y = int(self.paddles[0].ycor())
        self.paddles[0].goto(current_x, (current_y + 25))

    def down(self):
        current_x = int(self.paddles[0].xcor())
        current_y = int(self.paddles[0].ycor())
        self.paddles[0].goto(current_x, (current_y - 25))

    def w(self):
        current_x = int(self.paddles[1].xcor())
        current_y = int(self.paddles[1].ycor())
        self.paddles[1].goto(current_x, (current_y + 25))

    def s(self):
        current_x = int(self.paddles[1].xcor())
        current_y = int(self.paddles[1].ycor())
        self.paddles[1].goto(current_x, (current_y - 25))

