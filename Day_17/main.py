from question_model import Question
from data import question_data


def main():
  questions = []
  for question in question_data:
    q_text= question["text"]
    q_answer= question["answer"]
    
    #  create a new question instance
    new_question = Question(q_text, q_answer)
    
    # add it to the question list
    questions.append(new_question)
  
  print(questions[0].text)

# the program starts here
main()