label scenario_3:

    scene classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy
    # These display lines of dialogue.

    "After a long day and with art class now over, the school day comes to an end. Your friends A and B come strolling over."

    show alpha_base_expression at left

    alpha "Dang man, finally we’re done here."

    show bravo_base_expression at bounce, right

    bravo "Yeah, the last 10 minutes felt like an entire hour! I nearly fell asleep."

    show alpha_base_expression at bounce

    alpha "Haha, I saw that! I was preparing things to throw at you, but the bell saved you."

    show bravo_base_expression at bounce

    bravo "What was that class even about?"

    show alpha_base_expression at bounce

    alpha "I have no clue but I’m sure the homework will tell me."

    show bravo_base_expression at bounce

    bravo "Don’t remind me of that! It’s as if he finds completely separate topics every week and expects us to already understand them."

    show alpha_base_expression at bounce

    alpha "Good thing that we won’t have to do that stuff until tomorrow."

    show bravo_base_expression at bounce

    bravo "Ah right! We had plans for today!"

    show alpha_base_expression at bounce

    alpha "Bowling, baby! Not that I’ve gone bowling in, like half a year, but I’ll still be able to beat you."

    show bravo_base_expression at bounce

    bravo "You’re just saying that so it won’t be that embarrassing when you can’t even lift the balls."

    show alpha_base_expression at bounce

    alpha "I can hold even the heaviest of balls!"

    show bravo_base_expression at bounce

    bravo "Haha, sure dude."

    show alpha_base_expression at bounce

    alpha "No I mean it! I’ve held them all!"

    show bravo_base_expression at bounce

    bravo "Enough about your balls. Do you want to go or not?"

    show alpha_base_expression at bounce

    alpha "Of course I want to go! Hey, let’s ask [mc] to join. Then it’ll be a challenge for us both."

    hide bravo_base_expression

    show alpha_base_expression at center

    alpha "Hey [mc] we’re going bowling now, wanna join?"

    menu:
        "Sure!":
            hide alpha_base_expression
            hide bravo_base_expression
            jump .accept_invitation

        "I’m busy today.":
            hide alpha_base_expression
            hide bravo_base_expression
            jump .decline_invitation
    
    label .accept_invitation:

        show bravo_base_expression at bounce, right

        bravo "Heck yeah!"

        show alpha_base_expression at bounce, left

        alpha "Without you it would have been too easy."

        hide alpha_base_expression
        hide bravo_base_expression

        # hide placeholder_classroom
        scene placeholder_bowling

        "Arriving at the bowling alley, you settle down and get ready to start."

        show alpha_base_expression at bounce, left

        alpha "Here we are! Our battle will be legendary!"

        show bravo_base_expression at bounce, right

        bravo "I hope you remember those words when you come in last place."

        show alpha_base_expression at bounce

        alpha "That could never happen!"

        show bravo_base_expression at bounce

        bravo "It can and it will."

        show alpha_base_expression at bounce

        alpha "Well unlike you, I don’t regularly practice."

        show bravo_base_expression at bounce

        bravo "I also don’t regularly go bowling!"

        show alpha_base_expression at bounce

        alpha "That sounds like a massive excuse for what we are about to witness!"

        show bravo_base_expression at bounce

        bravo "Well then, let’s see who’s superior! [mc], do you want to join or be the referee?"

        menu:
            "Join in!":
                hide alpha_base_expression
                hide bravo_base_expression
                hide mc_placeholder
                jump .join_in
            "Referee":
                hide alpha_base_expression
                hide bravo_base_expression
                hide mc_placeholder
                jump .referee
        
        label .join_in:

            show mc_placeholder at bounce, Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

            mc "I’ll join!"

            hide mc_placeholder

            show alpha_base_expression at bounce, left

            alpha "YAY!"

            show bravo_base_expression at bounce, right

            bravo "In that case [alpha] & I may need to join forces to defeat you."

            show alpha_base_expression at bounce

            alpha "Don’t you worry [bravo], I can defeat the both of you by my lonesome!"

            jump scenario_4


        label .referee:

            show mc_placeholder at bounce, Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

            mc "I’d rather just watch you two."

            hide mc_placeholder

            show alpha_base_expression at bounce, left

            alpha "Aww, what a bummer."

            show bravo_base_expression at bounce, right

            bravo "All good, just make sure that [alpha] doesn’t cheat, okay?"

            jump scenario_4

    
    label .decline_invitation:

        show bravo_base_expression at bounce, right

        bravo "Aw man! That’s unfortunate!"

        show alpha_base_expression at bounce, left

        alpha "No probs though, that just means that I win automatically! It will be a little lonely though."

        show bravo_base_expression at bounce

        bravo "No need to make them feel guilty! Originally it was a plan just between the two of us anyway."

        show alpha_base_expression at bounce

        alpha "Yeah, you’re right. Sorry [mc] I didn’t want to be overbearing or anything."

        hide alpha_base_expression
        hide bravo_base_expression

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

            show alpha_base_expression at bounce, left

            alpha "Really? I never really notice."

            show bravo_base_expression at bounce, right

            bravo "That’s because no matter where we go, you are the loudest one present."

            show alpha_base_expression at bounce

            alpha "Not true!? Do you remember that one time when we tried to outperform that one rooster? I didn’t manage to beat him."

            show bravo_base_expression at bounce

            bravo "Wow! One time some bird was louder than you. That completely disproves my point!"

            show alpha_base_expression at bounce

            alpha "As long as you get it now."

            show bravo_base_expression at bounce

            bravo "I was being sarcastic."

            show alpha_base_expression at bounce

            alpha "What? Now I definitely won’t go easy on you! Just you wait for my secret bowling technique!"

            show bravo_base_expression at bounce

            bravo "Yeah yeah, save your game talk for when we get there."

            hide alpha_base_expression
            hide bravo_base_expression

            "Time to go home"

            jump scenario_4


        label .not_today:

            show mc_placeholder at bounce, Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

            mc "It’s just that I don’t really feel like doing anything today. If we can postpone to another day that would be awesome!"

            hide mc_placeholder

            show alpha_base_expression at bounce, left

            alpha "But we want to go today."

            show bravo_base_expression at bounce, right

            bravo "Yeah, but [mc] did not mentally prepare themselves for this."

            bravo "Hey [mc] if you want to go on another day, feel free to tell us and we’ll be sure to figure something out."

            show alpha_base_expression at bounce

            alpha "But what about today?"

            show bravo_base_expression at bounce

            bravo "We can still go today, just no with [mc]."

            show alpha_base_expression at bounce

            alpha "Heck yeah, so we go bowling twice? I will use you as a steppingstone on my way to overthrow [mc], the absolute bowling champion!"

            show bravo_base_expression at bounce

            bravo "You can’t even climb normal stairs without falling so how do you think you will do that?"

            show alpha_base_expression at bounce

            alpha "That was like, four weeks ago! I am a different person now, I have mastered all types of stairs through vigorous training and today I will master you!"

            show bravo_base_expression at bounce

            bravo "Sure thing buddy."

            show alpha_base_expression at bounce

            alpha "See you tomorrow [mc]!"

            show bravo_base_expression at bounce

            bravo "Bye bye. And tell us when you want to go bowling at some point!"

            hide alpha_base_expression
            hide bravo_base_expression

            show mc_placeholder at bounce, Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

            mc "See you guys!"

            jump scenario_4
