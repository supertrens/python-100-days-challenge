from turtle import Screen

from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
screen.listen()

paddle = Paddle()

screen.onkey(key="Up", fun=paddle.move_up)
screen.onkey(key="Down", fun=paddle.move_down)

game_is_on = True

while game_is_on:
  screen.update()


screen.exitonclick()