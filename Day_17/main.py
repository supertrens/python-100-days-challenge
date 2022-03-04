from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
  
  questions = []
  # build question list
  for question in question_data:
    q_text= question["text"]
    q_answer= question["answer"]
    
    #  create a new question instance
    new_question = Question(q_text, q_answer)
    
    # add it to the question list
    questions.append(new_question)
  
  # initiate the quiz
  quiz = QuizBrain(questions)
  
  while quiz.still_has_question():
    quiz.new_question()
  
  final_score = round(quiz.score / len(quiz.question_list) * 100)
  print("You've completed the quiz")
  print(f"You got {quiz.score} out of {len(quiz.question_list)}, your final score is {final_score} / 100")
  
# the program starts here
main()