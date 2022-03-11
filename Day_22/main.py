
import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
screen.listen()

paddle_1 = Paddle(orientation="right")
paddle_2 = Paddle(orientation="left")
ball = Ball()

# right paddle control
screen.onkey(key="Up", fun=paddle_1.move_up)
screen.onkey(key="Down", fun=paddle_1.move_down)

# left paddle control
screen.onkey(key="w", fun=paddle_2.move_up)
screen.onkey(key="s", fun=paddle_2.move_down)

game_is_on = True

while game_is_on:
  time.sleep(0.1)
  screen.update()
  ball.move()


screen.exitonclick()