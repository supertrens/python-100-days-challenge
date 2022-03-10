import time
from turtle import Screen
from food import Food

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#444")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

game_is_on = True

snake = Snake()
food = Food()

def stop_game():
  global game_is_on
  
  game_is_on = False
  
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="space", fun=stop_game)



def update_screen():
    screen.update()
    time.sleep(0.5)

while game_is_on:
  update_screen()
  snake.move_forward()




screen.exitonclick()