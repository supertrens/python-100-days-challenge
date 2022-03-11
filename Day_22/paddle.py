from turtle import Turtle

STEP = 20

class Paddle(Turtle):
  def __init__(self) -> None:
      super().__init__()
      self.create_paddle()
      
  def create_paddle(self):
    self.penup()
    self.color("white")
    self.shape("square")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.goto(350, 0)
  
  def move_up(self):
    self.sety(self.ycor() + STEP)
    
  def move_down(self):
    self.sety(self.ycor() - STEP)
