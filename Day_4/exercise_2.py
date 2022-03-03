# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut","Massachusetts", "Maryland","South Carolina", "New Hampshire", "Virginia", "New York"]

# print(states_of_america)
import random


names_string = input("Give me everybody names, separated by a comma.")
names = names_string.split(", ")

random_number = random.randint(0, len(names)-1)
print(f"{names[random_number]} is going to buy the meal today!")