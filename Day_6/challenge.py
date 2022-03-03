
# VERSION_1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
 
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif right_is_clear():
#         turn_right()
#     else:
#         turn_left()




# CORNER_CASES
# while front_is_clear():
#     move()
# turn_left()

# VERSION_2
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
 
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#        move()
#     else:
#         turn_left()


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()  
# def next_steps(): #defining a new function.
#     turn_right()
#     move()
# while not at_goal():
#     if wall_in_front():
#        turn_left() 
#     else:
#        move()
#     if not front_is_clear() and right_is_clear():
#        next_steps()
#     elif front_is_clear() and right_is_clear():
#        next_steps()