import time
from turtle import Screen

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#444")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

game_is_on = True

snake = Snake()

screen.onkey(key="w", fun=snake.move_up)
screen.onkey(key="s", fun=snake.move_down)

def update_screen():
    screen.update()
    time.sleep(0.5)

while game_is_on:
  update_screen()
  snake.move_forward()




screen.exitonclick()