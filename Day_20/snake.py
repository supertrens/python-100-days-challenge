from turtle import Turtle

class Snake:
  MIN_SEGMENT = 3
  SEGMENT_SIZE = 20
  
  def __init__(self) -> None:
    self.segment_list = []
    
    for num in range(0, self.MIN_SEGMENT):
      gap_x = num * -self.SEGMENT_SIZE
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
    head =  self.segment_list[0]
    max_range = len(self.segment_list) - 1
    min_range = 0
    step = -1
    
    for segment_num in range(max_range, min_range, step):
      previous_segment = self.segment_list[segment_num - 1]
      current_segment = self.segment_list[segment_num]
      
      current_segment.goto(previous_segment.pos())
      
    head.forward(10)
  
  def move_up(self):
    head = self.segment_list[0]
    if head.heading() == -90:
      pass
    else:
      head.setheading(90)


  def move_down(self):
    head = self.segment_list[0]
    if head.heading() == 90:
      pass
    else:
      head.setheading(-90)
    
