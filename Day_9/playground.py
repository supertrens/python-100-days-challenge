# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# def get_grade(score):
#   current_grade = "Fail"
  
#   if score > 90:
#     current_grade = "Outstanding"
#   elif score > 80:
#     current_grade = "Exceeds Expectations"
#   elif score > 70:
#     current_grade = "Acceptable"
  
#   return current_grade

# for student in student_scores:
#   current_score = student_scores[student]
#   student_grades[student] = get_grade(current_score)

# print(student_grades)

# travel_log = [
#   {
#     "country": "France",  
#     "cities_visited": ["Paris", "Lille", "Dijon"], 
#     "total_visits": 12,
#   },
#   {
#     "country": "Germany",  
#     "cities_visited": ["Berlin", "Hamburg", "Munich", "Stuttgart"], 
#     "total_visits": 5,
#   },
# ]

# print(travel_log)


# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# dict[1] = 4

# print(dict[1])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])


