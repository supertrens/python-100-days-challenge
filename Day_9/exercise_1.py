student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

def get_grade(score):
  current_grade = "Fail"
  
  if score > 90:
    current_grade = "Outstanding"
  elif score > 80:
    current_grade = "Exceeds Expectations"
  elif score > 70:
    current_grade = "Acceptable"
  
  return current_grade

for student in student_scores:
  current_score = student_scores[student]
  student_grades[student] = get_grade(current_score)

print(student_grades)
