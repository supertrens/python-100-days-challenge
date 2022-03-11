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
    self.x_move= STEP
    self.y_move = STEP
   
  def move(self):
    self.check_collision_with_wall()
    
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(x=new_x, y=new_y)
  
  def check_collision_with_wall(self):
    if(self.ycor() > 280 or self.ycor() < -280 ):
      self.bounce()
  
  def bounce(self):
    self.y_move *= -1
