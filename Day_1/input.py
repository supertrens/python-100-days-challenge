# print( input("What is your name? ") + " is awesome")

# 1. Create a greeting for your program.
print("Welcome to band name generator")

# 2. Ask the user for the city that they grew up in.
# city = input("Which city did you grow up in?\n")
# 3. Ask the user for the name of a pet.
# pet = input("What's your pet name?\n")
# 4. Combine the name of their city and pet and show them their band name.
# print("Your Band name could Be " + city + " " + pet)

lead_singer = input("Who is the lead singer? ")
guitarist = input("Who is the guitarist? ")
player = input("who is the player? ")

# players_initials = lead_singer[0] + lead_singer[1] + guitarist[0] + guitarist[1]+ player[0] + player[1]
if(len(lead_singer) < 2 or len(guitarist)< 2 or len(player) < 2):
  print("Nom nou tro kout")
else:
  players_initials = lead_singer[0:2],  guitarist[0:2], player[0:2]
  print("Your band name could be the: ", players_initials)








