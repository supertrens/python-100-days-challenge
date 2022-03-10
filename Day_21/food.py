import random
from turtle import Turtle, color, shapesize

MAX_POSITION = 280
MIN_POSITION = -280

class Food(Turtle):
  def __init__(self) -> None:
    super().__init__(shape="square")
    self.configure_food()
    self.set_new_food_location()
  
 
  def configure_food(self):
    self.color("orangered")
    self.penup()
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.speed("fastest")
  
  def set_new_food_location(self):
    random_x = self.generate_random_coordinate()
    random_y = self.generate_random_coordinate()
    self.goto(random_x, random_y)
    
  def generate_random_coordinate(self):
    return random.randint(MIN_POSITION, MAX_POSITION)
