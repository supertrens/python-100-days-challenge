import time
from tracemalloc import stop
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#444")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

segment_list = []
game_is_on = True

def create_segment(gap_x):
  segment = Turtle(shape="square")
  segment.penup()
  segment.color("#f3f3f3")
  segment.goto(gap_x, 0)
  
  return segment

def move_forward():
  screen.update()
  time.sleep(0.5)
  
  # local variables to set updated position
  head =  segment_list[0]
  max_range = len(segment_list) - 1
  min_range = 0
  step = -1
  
  for segment_num in range(max_range, min_range, step):
    previous_segment = segment_list[segment_num - 1]
    current_segment = segment_list[segment_num]
    
    current_segment.goto(previous_segment.pos())
    
  head.forward(10)
      

def move_up():
  head = segment_list[0]
  if head.heading() == -90:
     pass
  else:
    head.setheading(90)



def move_down():
  head = segment_list[0]
  if head.heading() == 90:
   pass
  else:
    head.setheading(-90)


screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)

def main():         
  for num in range(0,3):
    gap_x = num * -20
    segment = create_segment(gap_x)
    segment_list.append(segment)
    
main()

while game_is_on:
  move_forward()




screen.exitonclick()