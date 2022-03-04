import random


class QuizBrain:
  def __init__(self, question_list):
     self.score = 0
     self.question_number = 0
     self.question_list = question_list

  
  def new_question(self):
    current_question = self.question_list[self.question_number]
    self.increment_question_counter()
    
    answer= input(f"Q.{self.question_number}: {current_question.text} (True/False)?: " )
    
    self.check_answer(correct_answer= current_question.answer, given_answer= answer)
  
  def still_has_question(self):
    return self.question_number  <  len(self.question_list)
  
  def increment_question_counter(self):
    if(self.still_has_question()):
      self.question_number += 1
  
  def increment_score(self):
    self.score += 1
    
  def check_answer(self, correct_answer, given_answer):
    if(correct_answer.lower() == given_answer.lower()):
      self.increment_score()
      print("You got it right!")
    else:
      print("That's wrong")
    
    print(f"The correct answer was: {correct_answer}!")
    print(f"Your current score is: {self.score} / {self.question_number}")
    print("\n")


