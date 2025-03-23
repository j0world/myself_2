# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Jesse")
image mc_placeholder = "char/Protagonist.png"
image mc_base_expression = "char/Protagonist.png"

define alpha = Character("Friend A", who_xalign=0.0, color="#6de8fb") # name on left
image alpha_base_expression = "char/friend_1.png"

define bravo = Character("Friend B", who_xalign=1.0, color="#9d762d") # names on right
image bravo_base_expression = "char/friend_2.png"

define parent_1 = Character("Parent 1", color="#3f2f11")
image parent_1_base_expression = "char/parent_1.png"

define teacher = Character("Teacher", color="#ebc3ac")
image teacher_base_expression = "char/Teacher.png"

define classmate_1 = Character("Classmate 1", color="#aaaaaa")
image classmate_1 = "char/classmate_1.png"

define classmate_2 = Character("Classmate 2", color="#aaaaaa")
image classmate_2 = "char/classmate_1.png"

image placeholder_classroom = im.Scale("placeholders/placeholder_classroom.png", config.screen_width, config.screen_height)
image classroom = im.Scale("bg/classroom.png", config.screen_width, config.screen_height)
image placeholder_bowling = im.Scale("placeholders/placeholder_bowling_alley.png", config.screen_width, config.screen_height)
image bedroom = im.Scale("bg/Bedroom.png", config.screen_width, config.screen_height)
image living_room = im.Scale("placeholders/placeholder_livingroom.png", config.screen_width, config.screen_height)


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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    jump scenario_1 # delete when done testing




    """
    show mc_placeholder at Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)# counts from top left cor

    mc "It's getting late! Time for bed!"

    hide mc_placeholder

    "You grip the remote, hesitating. You really want to see what happens next, but you also know that getting enough sleep is important."
    """

    # This ends the game.

    return
