
import random
import os

MIN_VALUE = 1
MAX_VALUE = 100
LEVELS = ["Easy", "Medium", "Hard", "Very Hard"]

print("Welcome to the guessing the number game:")
print(f"I'm thinking of a number between {MIN_VALUE} and {MAX_VALUE}")

keep_asking_for_level = True
is_completed = False
magic_number = random.randrange(MIN_VALUE, MAX_VALUE + 1)

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def set_level():
  level = input("""
      Please choose a difficulty:\n\n\
                          Easy (press 1)
                          Medium (press 2)
                          Hard (press 3)
                          Very Hard (press 4)
                          Quit (press 5)
      """)
  clear_screen()
  return level

def is_level_valide():
  if(level == 5):
    print("Thank you for playing the game!")
    return True
  if(level >= 1 and level <= 4 ):
    print(f"you have selected '{LEVELS[level-1]}' ({level})")
    return True
  else:
    print(f"you have selected {level} which is an invalid selection. Please try again")
    return False

def get_allow_trial_count():
  match level:
    case 1:
      trial = 10
    case 2:
      trial = 7
    case 3:
      trial = 5
    case 4: 
      trial = 3
    case _:
      trial = 0
  
  return trial

def display_status():
  attempt_str = "attempt"
  if trial_count > MIN_VALUE :
    attempt_str = "attempts"
    
  print(f"You have {trial_count} {attempt_str} remaining to guess the number.")

def validate_answer():
  if guess == magic_number:
    initial_total_count = get_allow_trial_count()
    print(f"Congratulations you got the number in {initial_total_count - trial_count} trial(s)")
    return True
  
  if guess > magic_number:
    print("Too high.")
  else:
    print("Too low.")
  
  return False

def play_again():
  if trial_count == 0:
    print("Game Over!\n")
    print(f"The magic number was: {magic_number}")
  else:
     print("Guess Again!\n")


while keep_asking_for_level:
  level = int(set_level())
  keep_asking_for_level = not is_level_valide()
  trial_count = get_allow_trial_count()

while trial_count > 0 and not is_completed:
  display_status()
  guess = int(input("Make a guess: "))
  
  # decrease the counter
  trial_count -= 1
  
  is_completed = validate_answer() 
  
  if(not is_completed):
    play_again()


