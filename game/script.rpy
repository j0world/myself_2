# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# characters
define mc = Character("Jesse")
image mc_placeholder = "char/Protagonist.png"
image mc_base_expression = "char/Protagonist.png"

define alpha = Character("Charlie", who_xalign=0.0, color="#6de8fb") # name on left
image alpha_base_expression = "char/friend_1.png"

define bravo = Character("Kim", who_xalign=1.0, color="#9d762d") # names on right
image bravo_base_expression = "char/friend_2.png"

define parent_1 = Character("Mom", color="#3f2f11")
image parent_1_base_expression = "char/parent_1.png"

define teacher = Character("Teacher", color="#ebc3ac")
image teacher_base_expression = "char/Teacher.png"

define classmate_1 = Character("Classmate 1", color="#aaaaaa")
image classmate_1 = "char/classmate_1.png"

define classmate_2 = Character("Classmate 2", color="#aaaaaa")
image classmate_2 = "char/classmate_1.png"


# background images
image placeholder_classroom = im.Scale("placeholders/placeholder_classroom.png", config.screen_width, config.screen_height)
image classroom = im.Scale("bg/classroom.png", config.screen_width, config.screen_height)
image placeholder_bowling = im.Scale("bg/Bowling.png", config.screen_width, config.screen_height)
image bedroom = im.Scale("bg/Bedroom.png", config.screen_width, config.screen_height)
image living_room = im.Scale("bg/living_room_front.png", config.screen_width, config.screen_height)
image living_room_tv = im.Scale("bg/living_room_tv.png", config.screen_width, config.screen_height)
image living_room_food = im.Scale("bg/living_room_food.png", config.screen_width, config.screen_height)


transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    #repeat


# The game starts here.

label start:

    jump scenario_1

    # This ends the game.
    return
