import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=900, height=500)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()


right_paddle = Paddle((430, 0))
left_paddle = Paddle((-430, 0))


screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

ball = Ball()
scoreboard = Scoreboard()


game_is_running = True
while game_is_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 420:
        ball.bounce_from_paddle()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -420:
        ball.bounce_from_paddle()
    if ball.xcor() > 430:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    if ball.xcor() < -430:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()



screen.exitonclick()