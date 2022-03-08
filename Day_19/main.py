import random
from turtle import Turtle , Screen

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
GAP = 50
MAX_STEP = 10
MIN_STEP= 1

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
is_racing  = True
turtles = []

def initiate_turtles():
  colors = ["red", "orange", "yellow", "green", "blue", "purple"]
  current_y = 150
  current_x = - (SCREEN_WIDTH - 20) / 2
  
  for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=current_x, y=current_y)
    current_y -= GAP
    turtles.append(new_turtle)
    
def move():
  global is_racing
  half_width = 230

  for turtle in turtles:
    if turtle.xcor() > half_width:
      is_racing = False
      winner_color = turtle.pencolor()
    else:  
      random_step = random.randint(MIN_STEP , MAX_STEP)
      turtle.forward(random_step)
      
    
def main():
  initiate_turtles()

  while is_racing:
   move()
  

 

main()
screen.exitonclick()