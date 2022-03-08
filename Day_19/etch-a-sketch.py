from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()

STEP = 10

def move_forward():
  tim.forward(STEP)
  
def move_backward():
  tim.backward(STEP)

def turn_left():
  current_heading = tim.heading()
  tim.setheading(current_heading + STEP)
  
def turn_right():
  current_heading = tim.heading()
  tim.setheading(current_heading - STEP)
  
def clear_screen():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()  

def main():
  screen.onkeypress(key="w",  fun=move_forward)
  screen.onkeypress(key="s",  fun=move_backward)
  screen.onkeypress(key="a",  fun=turn_left)
  screen.onkeypress(key="d",  fun=turn_right)
  screen.onkeypress(key="c",  fun=clear_screen)

main()

screen.exitonclick()