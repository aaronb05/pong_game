import random
from turtle import Turtle


START_DIRECTION = random.randint(-35, 35)


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        # self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def start_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def change_direction(self):
        self.x_move *= -1
        self.move_speed *= 0.9


