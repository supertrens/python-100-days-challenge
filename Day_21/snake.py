from turtle import Turtle

MIN_SEGMENT = 3
SEGMENT_SIZE = 20
MOVE_PACE = 20

DIRECTION = {
  "up" : 90,
  "down" : 270,
  "left": 180,
  "right" : 0
}
class Snake:

  def __init__(self) -> None:
    self.segment_list = []
    self.create_snake()
    self.head = self.segment_list[0]

  def create_snake(self):
    for num in range(0, MIN_SEGMENT):
      gap_x = num * (- SEGMENT_SIZE)
      segment = self.create_segment(gap_x)
      self.segment_list.append(segment)
      
  def create_segment(self, gap_x):
    segment = Turtle(shape="square")
    segment.penup()
    segment.color("#f3f3f3")
    segment.goto(gap_x, 0)
    return segment
  
  def move_forward(self):
    # local variables to set updated position
    max_range = len(self.segment_list) - 1
    min_range = 0
    step = -1
    
    for segment_num in range(max_range, min_range, step):
      previous_segment = self.segment_list[segment_num - 1]
      current_segment = self.segment_list[segment_num]
      
      current_segment.goto(previous_segment.pos())
      
    self.head.forward(MOVE_PACE)
  
  def move_up(self):
    if self.head.heading() != DIRECTION["down"]:
      self.head.setheading(DIRECTION["up"])

  def move_down(self):
    if self.head.heading() != DIRECTION["up"]:
      self.head.setheading(DIRECTION["down"])
  
  def move_left(self):
    if self.head.heading() != DIRECTION["right"]:
      self.head.setheading(DIRECTION["left"])

  def move_right(self):
    if self.head.heading() != DIRECTION["left"]:
      self.head.setheading(DIRECTION["right"])

