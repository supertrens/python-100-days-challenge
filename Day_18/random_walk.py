import random
from turtle import Turtle , Screen

MAX_REPETITION = 1500


tom = Turtle()
tom.shape("turtle")
tom.pensize(10)
tom.speed("fastest")

direction = [0, 90, 180, 270]


def change_color():
    # rand_color = random.choices(range(256), k=3)
    # tom.color(rand_color)

    R = random.random()
    B = random.random()
    G = random.random()

    tom.color(R, G, B)
    

def move():
  random_direction = random.choice(direction)
  tom.forward(20)
  tom.setheading(random_direction)

def main():
  for _ in range(MAX_REPETITION):
    change_color()
    move()


# The program starts here
main()  

screen = Screen()
screen.exitonclick()