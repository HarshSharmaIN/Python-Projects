from screen import PongScreen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
score = ScoreBoard()
screen = PongScreen(l_paddle, r_paddle)
screen.l_paddle_movement('w', 's')
screen.r_paddle_movement('Up', 'Down')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.movement()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if ball have gone too far
    if ball.xcor() > 380:
        ball.ball_reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.ball_reset()
        score.l_point()

screen.exit()
