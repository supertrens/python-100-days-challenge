from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class ScoreBoard(Turtle):
  
  def __init__(self) -> None:
    super().__init__()
    self.score = 0 
    self.penup()
    self.color("white")
    self.hideturtle()
    self.goto(x=0, y=270)
    self.refresh_board()
  
  def refresh_board(self):
    self.clear()
    self.write(f"Score:{self.score}", False, align=ALIGNMENT, font= FONT)
  
  def update_score(self):
    self.score += 1
    self.refresh_board()
  
  def reset_score(self):
    self.score = 0
    self.refresh_board()
      