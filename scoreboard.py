
from turtle import Turtle
TOP = (0, 250)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def player_a(self):
        self.r_score += 1
        self.update_score()

    def player_b(self):
        self.l_score += 1
        self.update_score()

    def game_over(self):
        if self.l_score > self.r_score:
            print("Player 1 wins!")
        elif self.l_score < self.r_score:
            print("Player 2 wins!")
        else:
            print("Game is a tie! please play again")
