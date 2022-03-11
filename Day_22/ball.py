from turtle import Turtle

STEP = 5
class Ball(Turtle):
  def __init__(self) -> None:
      super().__init__()
      self.create_ball()
      
  def create_ball(self):
    self.shape("circle")
    self.color("white")
    self.penup()
   
  def move(self):
    new_x = self.xcor() + STEP
    new_y = self.ycor() + STEP
    self.goto(x=new_x, y=new_y)