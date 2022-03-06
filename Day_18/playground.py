from turtle import Screen, Turtle

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
for _  in range(15):
  tim.pendown()
  tim.forward(10)
  tim.penup()
  tim.forward(10)







screen = Screen()
screen.exitonclick()