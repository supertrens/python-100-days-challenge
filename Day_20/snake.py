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
  
  def get_head(self):
    return self.segment_list[0]
  
  def move_forward(self):
    # local variables to set updated position
    head =  self.segment_list[0]
    max_range = len(self.segment_list) - 1
    min_range = 0
    step = -1
    
    for segment_num in range(max_range, min_range, step):
      previous_segment = self.segment_list[segment_num - 1]
      current_segment = self.segment_list[segment_num]
      
      current_segment.goto(previous_segment.pos())
      
    head.forward(MOVE_PACE)
  
  def move_up(self):
    head = self.get_head()
    if head.heading() != DIRECTION["down"]:
      head.setheading(DIRECTION["up"])

  def move_down(self):
    head = self.get_head()
    if head.heading() != DIRECTION["up"]:
      head.setheading(DIRECTION["down"])
  
  def move_left(self):
    head = self.get_head()
    if head.heading() != DIRECTION["right"]:
      head.setheading(DIRECTION["left"])

  def move_right(self):
    head = self.get_head()
    if head.heading() != DIRECTION["left"]:
      head.setheading(DIRECTION["right"])

