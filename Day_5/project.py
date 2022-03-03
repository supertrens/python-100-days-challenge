import string
import random

print("Welcome to the PyPassword Generator!")

max_letters = int(input("How many letters would you like in your password? "))
max_symbols = int(input("How many symbols would you like? "))
max_numbers = int(input("How many numbers would you like? "))

random_letters = ""
random_symbols = ""
random_numbers = ""

for _ in range(0, max_letters):
  random_letters += random.choice(string.ascii_letters)

for _ in range(0, max_symbols):
  random_symbols += random.choice(string.punctuation)
  
for _ in range(0, max_numbers):
  random_numbers += random.choice(string.digits)

random_password = random_letters + random_symbols + random_numbers


print(random_password)
