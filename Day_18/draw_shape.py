import random
from turtle import Screen, Turtle

       
TOTAL_ANGLE = 360
MAX_CORNERS = 15

screen = Screen()
screen.bgcolor("lightgray")

tim = Turtle()
tim.shape("turtle")

def draw_shape(corner):
  angle = TOTAL_ANGLE / corner
  for _ in range(corner):
    tim.forward(100)
    tim.right(angle)
    
def change_color():
    # rand_color = random.choices(range(256), k=3)
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


def main():
  corner = 3

  while corner < MAX_CORNERS:
    change_color()
    draw_shape(corner)
    corner += 1

main()


screen.exitonclick()