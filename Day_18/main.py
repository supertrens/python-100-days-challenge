import random
import colorgram
from turtle import Turtle, Screen, colormode


MAX_LINE = 10
GAP = 50

colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.color

color_list = []
  
def draw_a_row():
    for _ in range(MAX_LINE):
      rand_color = random.choice(color_list)
      tim.dot(20, rand_color)
      tim.penup()
      tim.forward(GAP)
      
def set_color_from_image():
   colors = colorgram.extract('Day_18/img.jpg', 30)
   for color in colors:
     color_list.append(tuple(color.rgb))
    
def main():
  set_color_from_image()
  
  current_y = 0
  for _ in range(MAX_LINE):
    tim.setposition((0, current_y))
    draw_a_row()
    current_y += GAP
  
  tim.hideturtle()

# the program starts here
main()


screen = Screen()
screen.exitonclick()