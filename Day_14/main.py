import random
import os

import art
from game_data import data


score = 0
is_game_over = False
  
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    
def get_new_random_item():
  return  random.choice(data)

def display_comparison(first, second):
  print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}. (FOLLOWERS: {first['follower_count']}M)")
  print(art.vs)
  print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}.\n\n")

def get_user_choice(first, second):
  response = input("Who has more followers? Type 'A' or 'B': ").upper()
  
  if response == 'A':
    return first
  if response == 'B':
    return second

def validate_response(first, second, choice):
  global score

  if first['follower_count'] > second['follower_count']:
    correct_answer = first
  else:
    correct_answer = second
  
  is_correct = choice == correct_answer
  
  if is_correct:
      score += 1
    
  return is_correct

def display_game_status():  
  clear_screen()
  
  if(not is_game_over):
    print(f"You're right! Current score: {score}")
  else:
    print(f"Wrong answer!\n Final Score: {score}")

def main():
  global is_game_over
  
  # initiate the items
  first_item = get_new_random_item()
  second_item = get_new_random_item()
  
  while not is_game_over:
   display_comparison(first_item, second_item)
   choice = get_user_choice(first_item,second_item)
   is_game_over = not validate_response(first_item, second_item, choice)
   display_game_status()

   first_item = choice
   second_item = get_new_random_item()


# The program starts here
main()