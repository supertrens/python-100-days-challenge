import string
import random

print("Welcome to the PyPassword Generator!")

max_letters = int(input("How many letters would you like in your password? "))
max_symbols = int(input("How many symbols would you like? "))
max_numbers = int(input("How many numbers would you like? "))

# generate the random letters, symbols and numbers
random_letters = random.sample(string.ascii_letters, max_letters)
random_symbols = random.sample(string.punctuation, max_symbols)
random_numbers = random.sample(string.digits, max_numbers)

# add all of them as a single list
random_password = []
random_password.extend(random_letters)
random_password.extend(random_symbols)
random_password.extend(random_numbers)

# shuffle the list
random.shuffle(random_password)

password_string = "".join(random_password)

print(password_string)




