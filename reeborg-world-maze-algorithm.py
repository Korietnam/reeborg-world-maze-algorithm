# website used
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# the code
# copy and paste code into website

# NOTE: this is not intended to be used in a stand alone python terminal!

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif front_is_clear() and right_is_clear():
        turn_right()
        if right_is_clear():
            move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
        if right_is_clear():
            move()