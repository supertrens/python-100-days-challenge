# from turtle import Turtle, Screen

# my_screen = Screen()
# my_screen.exitonclick()

# thuggy =   Turtle()
# thuggy.shape("turtle")
# thuggy.color("blue")

# for i in range(1,50):
#   thuggy.forward(i)


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"], align="l")
table.add_column("Type",["Electric", "Water", "Fire"], align="l")
print(table)