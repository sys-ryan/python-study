from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# screen.onkeypress(key="Up", fun=r_paddle.go_up())
# screen.onkeypress(key="Down", fun=r_paddle.go_down())
# screen.onkeypress(key="w", fun=l_paddle.go_up())
# screen.onkeypress(key="s", fun=l_paddle.go_down())



game_is_on = True
while game_is_on:

    time.sleep(ball.move_spped)
    screen.update()
    ball.move()

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()