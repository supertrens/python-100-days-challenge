import random
from turtle import Turtle, Screen

GAP = 5
MAX_DEGREE = 360

tim = Turtle()
tim.speed("fastest")
tim.pensize(2)


def draw_circle():
  tim.circle(100)
  current_heading = tim.heading()
  tim.setheading(current_heading + GAP)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

def main():
  counter = int(MAX_DEGREE / GAP)
  for _ in range(counter):
    change_color()
    draw_circle()
    
main()

screen = Screen()
screen.exitonclick()