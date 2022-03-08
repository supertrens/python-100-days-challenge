from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
  tim.forward(100)

screen.listen()
screen.onkeypress(fun=move_forward, key="space")

screen.exitonclick()