import random
from turtle import Screen, Turtle


screen = Screen()
screen.bgcolor("lightgray")

tim = Turtle()
tim.shape("turtle")
tim.color("red")



# MAKE A SQUARE
# count = 0 
# while count < 4:
#   tim.forward(100)
#   tim.right(90)
#   count += 1
  
# tim.color("blue")
# tim.penup()
# tim.forward(100)
# tim.pendown()

# MAKE ANOTHER SQUARE SIDE BY SIDE
# for _ in range(4):
#   tim.forward(100)
#   tim.right(90)


# MAKE DASHED LINE
# for _  in range(15):
#   tim.pendown()
#   tim.forward(10)
#   tim.penup()
#   tim.forward(10)

# Draw different shapes based on how many corners
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
       
TOTAL_ANGLE = 360
MAX_CORNERS = 15
corner = 3


while corner < MAX_CORNERS:
  change_color()
  draw_shape(corner)
  corner += 1









screen.exitonclick()