
import turtle as t
import time
import ball as b
import paddle as p
import scoreboard as sb

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

my_paddle = p.Paddle()
game_ball = b.Ball()
score = sb.Scoreboard()
screen.listen()
screen.onkeypress(my_paddle.up, "Up")
screen.onkeypress(my_paddle.down, "Down")
screen.onkeypress(my_paddle.w, "w")
screen.onkeypress(my_paddle.s, "s")
paddles = my_paddle.paddles

playing = True
while playing:
    # Start game
    screen.update()
    time.sleep(game_ball.move_speed)
    game_ball.start_ball()

    # detect bounce of wall
    if game_ball.ycor() > 290 or game_ball.ycor() < -290:
        game_ball.bounce()

    # bounce ball off paddle
    hits = 0
    if game_ball.distance(paddles[0]) < 50 and game_ball.xcor() > 320:
        score.player_a()
        game_ball.change_direction()
    elif game_ball.distance(paddles[1]) < 50 and game_ball.xcor() < -320:
        score.player_b()
        game_ball.change_direction()

    # determine if ball passed a paddle
    if game_ball.xcor() > 400 or game_ball.xcor() < -400:
        print("Game is over")
        playing = False

screen.exitonclick()



