# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("mc", color="#401447")
image mc_placeholder = "pink_girl_7.png"
define alpha = Character("Friend A")
image alpha_placeholder = "kikuri_hiroi.png"
define bravo = Character("Friend B")
image bravo_placeholder = "santa_frieren.png"

image placeholder_classroom = im.Scale("placeholder_classroom.png", config.screen_width, config.screen_height)
image placeholder_bowling = im.Scale("placeholder_bowling_alley.png", config.screen_width, config.screen_height)


transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
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

    scene placeholder_classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy
    # These display lines of dialogue.

    "With art class over now, the school day comes to an end. Your friends A and B come strolling over"

    show alpha_placeholder at left

    alpha "Dang man, finally we’re done here."

    show bravo_placeholder at bounce, right

    bravo "Yeah, the last 10 minutes felt like an entire hour! I nearly fell asleep."

    show alpha_placeholder at bounce

    alpha "Haha, I saw that! I was preparing things to throw at you, but the bell saved you."

    show bravo_placeholder at bounce

    bravo "What was that class even about?"

    show alpha_placeholder at bounce

    alpha "I have no clue but I’m sure the homework will tell me."

    show bravo_placeholder at bounce

    bravo "Don’t remind me of that! It’s as if he finds completely separate topics every week and expects us to already understand them."

    show alpha_placeholder at bounce

    alpha "Good thing that we won’t have to do that stuff until tomorrow."

    show bravo_placeholder at bounce

    bravo "Ah right! We had plans for today!"

    show alpha_placeholder at bounce

    alpha "Bowling, baby! Not that I’ve gone bowling in, like half a year, but I’ll still be able to beat you."

    show bravo_placeholder at bounce

    bravo "You’re just saying that so it won’t be that embarrassing when you can’t even lift the balls"

    show alpha_placeholder at bounce

    alpha "I can hold even the heaviest of balls!"

    show bravo_placeholder at bounce

    bravo "Haha, sure dude."

    show alpha_placeholder at bounce

    alpha "No I mean it! I’ve held them all!"

    show bravo_placeholder at bounce

    bravo "Enough about your balls. Do you want to go or not?"

    show alpha_placeholder at bounce

    alpha "Of course I want to go! Hey, let’s ask MC to join. Then it’ll be a challenge for us both."

    hide bravo_placeholder

    show alpha_placeholder at center

    alpha "Hey MC we’re going bowling now, wanna join?"

    menu:
        "Sure!":
            hide alpha_placeholder
            hide bravo_placeholder
            jump .accept_invitation

        "I’m busy today.":
            hide alpha_placeholder
            hide bravo_placeholder
            jump .decline_invitation
    
    label .accept_invitation:

        show bravo_placeholder at bounce, right

        bravo "Heck yeah!"

        show alpha_placeholder at bounce, left

        alpha "Without you it would have been too easy."

        hide alpha_placeholder
        hide bravo_placeholder

        # hide placeholder_classroom
        scene placeholder_bowling

        "Arriving at the bowling alley, you settle down and get ready to start."

        show alpha_placeholder at bounce, left

        alpha "Here we are! Our battle will be legendary!"

        show bravo_placeholder at bounce, right

        bravo "I hope you remember those words when you come in last place."

        show alpha_placeholder at bounce

        alpha "That could never happen!"

        show bravo_placeholder at bounce

        bravo "It can and it will."

        show alpha_placeholder at bounce

        alpha "Well unlike you, I don’t regularly practice."

        show bravo_placeholder at bounce

        bravo "I also don’t regularly go bowling!"

        show alpha_placeholder at bounce

        alpha "That sounds like a massive excuse for what we are about to witness!"

        show bravo_placeholder at bounce

        bravo "Well then, let’s see who’s superior! MC, do you want to join or be the referee?"

        return

    
    label .decline_invitation:

        show bravo_placeholder at bounce, right

        bravo "Aw man! That’s unfortunate!"

        show alpha_placeholder at bounce, left

        alpha "No probs though, that just means that I win automatically! It will be a little lonely though"

        show bravo_placeholder at bounce

        bravo "No need to make them feel guilty! Originally it was a plan just between the two of us anyway."

        show alpha_placeholder at bounce

        alpha "Yeah, you’re right. Sorry MC I didn’t want to be overbearing or anything."

        hide alpha_placeholder
        hide bravo_placeholder

        show mc_placeholder at Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

        mc "It’s all good! It’s just that…"

        menu: 
            "... it's too noisy for me.":
                hide mc_placeholder
                jump .too_noisy
            "... today doesn't work for me.":
                hide mc_placeholder
                jump .not_today
        
        label .too_noisy:
            show mc_placeholder at bounce, Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
            mc "It’s just that the bowling alley is a little too noisy for me"

            hide mc_placeholder

            show alpha_placeholder at bounce, left

            alpha "Really? I never really notice."

            show bravo_placeholder at bounce, right

            bravo "That’s because no matter where we go, you are the loudest one present."

            show alpha_placeholder at bounce

            alpha "Not true!? Do you remember that one time when we tried to outperform that one rooster? I didn’t manage to beat him."

            show bravo_placeholder at bounce

            bravo "Wow! One time some bird was louder than you. That completely disproves my point!"

            show alpha_placeholder at bounce

            alpha "As long as you get it now."

            show bravo_placeholder at bounce

            bravo "I was being sarcastic."

            show alpha_placeholder at bounce

            alpha "What? Now I definitely won’t go easy on you! Just you wait for my secret bowling technique!"

            show bravo_placeholder at bounce

            bravo "Yeah yeah, save your game talk for when we get there."

            hide alpha_placeholder
            hide bravo_placeholder

            "Time to go home"

            return


        label .not_today:

            show mc_placeholder at bounce, Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

            mc "It’s just that I don’t really feel like doing anything today. If we can postpone to another day that would be awesome!"

            hide mc_placeholder

            show alpha_placeholder at bounce, left

            alpha "But we want to go today."

            show bravo_placeholder at bounce, right

            bravo "Yeah, but MC did not mentally prepare themselves for this."

            bravo "Hey MC if you want to go on another day, feel free to tell us and we’ll be sure to figure something out"

            show alpha_placeholder at bounce

            alpha "But what about today?"

            show bravo_placeholder at bounce

            bravo "We can still go today, just no with MC."

            show alpha_placeholder at bounce

            alpha "Heck yeah, so we go bowling twice? I will use you as a steppingstone on my way to overthrow MC, the absolute bowling champion!"

            show bravo_placeholder at bounce

            bravo "You can’t even climb normal stairs without falling so how do you think you will do that?"

            show alpha_placeholder at bounce

            alpha "That was like, four weeks ago! I am a different person now, I have mastered all types of stairs though vigorous training and today I will master you!"

            show bravo_placeholder at bounce

            bravo "Sure thing buddy."

            show alpha_placeholder at bounce

            alpha "See you tomorrow MC!"

            show bravo_placeholder at bounce

            bravo "Bye bye. And tell us when you want to go bowling at some point!"

            hide alpha_placeholder
            hide bravo_placeholder

            show mc_placeholder at bounce, Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

            mc "See you guys!"


            return



    """
    show mc_placeholder at Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)# counts from top left cor

    mc "It's getting late! Time for bed!"

    hide mc_placeholder

    "You grip the remote, hesitating. You really want to see what happens next, but you also know that getting enough sleep is important."
    """

    # This ends the game.

    return
