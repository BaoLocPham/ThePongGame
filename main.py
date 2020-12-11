from turtle import Screen
from ScoreBoard import ScoreBoard
from Paddle import Paddle
from Ball import Ball
import winsound
import os
import sys
import time
screen = Screen()
screen.setup(width=800, height=600)
upper_bound = screen.window_height()//2-10
lower_bound = -upper_bound
right_bound = screen.window_width()//2-10
left_bound = -right_bound
screen.bgcolor('black')
screen.title("Fake Ass Pong Game")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def game_on():
    screen.tracer(0)
    screen.listen()
    scoreboard = ScoreBoard()
    scoreboard.print_score()
    lP = Paddle(-360, 0)
    rP = Paddle(360, 0)
    ball = Ball()
    screen.onkeypress(lP.up, "w")
    screen.onkeypress(lP.down, "s")
    screen.onkeypress(rP.up, "Up")
    screen.onkeypress(rP.down, "Down")

    winsound.PlaySound(resource_path("sound/winner.wav"), winsound.SND_ASYNC)
    time.sleep(4)
    game_over = False
    while not game_over:
        time.sleep(0.03)
        screen.update()
        ball.move()
        # detect collision with walls
        if ball.ycor() > upper_bound or ball.ycor() < lower_bound:
            ball.bouncing_wall()
        # detect miss the ball
        if ball.xcor() > right_bound:
            winsound.PlaySound(resource_path("sound/correct.wav"), winsound.SND_ASYNC)
            ball.refresh()
            scoreboard.increase_left()
            if scoreboard.lScore == 3:
                game_over = True
            time.sleep(1)
        if ball.xcor() < left_bound:
            winsound.PlaySound(resource_path("sound/correct.wav"), winsound.SND_ASYNC)
            ball.refresh()
            scoreboard.increase_right()
            if scoreboard.rScore == 3:
                game_over = True
            time.sleep(1)

        # detect collision with paddle
        if ball.distance(rP) < 50 and ball.xcor() > 340 or ball.distance(lP) < 50 and ball.xcor() < -340:
            ball.bouncing_paddle()
            winsound.PlaySound(resource_path("sound/bouncing.wav"), winsound.SND_ASYNC)

    scoreboard.print_final()
    winsound.PlaySound(resource_path("sound/happynes.wav"), winsound.SND_ASYNC)


while True:
    game_on()
    time.sleep(1)
    cont = screen.textinput("Continue?", prompt="Continue?(yes or no)").lower()
    if cont == 'yes':
        screen.reset()
        continue
    else:
        screen.clear()
        break

screen.exitonclick()