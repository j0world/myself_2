label scenario_4:

    scene living_room

    "You’re sitting comfortably on the couch, wrapped in a cozy blanket, watching your favorite TV show. The room is dimly lit, and the soft glow of the screen flickers across your face."
    "You can hear your parents talking in another room, their voices blending with the low hum of the TV.
    Just as the episode gets really exciting, you hear a voice from the hallway:"

    show parent_1_base_expression at bounce, left

    parent_1 "It's getting late! Time for bed!"

    show mc_placeholder at bounce, right

    mc "No! I want to keep watching! The important part is just coming up. Can I??"

    show parent_1_base_expression at bounce, left

    parent_1 "No, you really need to go to bed now, otherwise you will not be able to to get up in the morning!"

    # kind of unnatural IMO
    "You grip the remote, hesitating. You really want to see what happens next, but you also know that getting enough sleep is important."

    menu:
        "Go to bed":
            jump .go_to_bed

        "Keep watching":
            jump .keep_watching

    label .go_to_bed:

        "You decide to be responsible and go to bed, but you still feel torn about missing the end of your show. You think about your options:"

        mc "Okayy, if I have to then I will turn off the TV. But…"

        menu: 
            "Ask your parents to record the episode for tomorrow.":
                jump .record_episode
            "If you can't sleep, turn the TV back on.":
                jump .turn_tv_back_on
        
        label .record_episode:

            show mc_placeholder at bounce, right

            mc "Could you record the episode for me?? I want to watch what happens next!"

            show parent_1_base_expression at bounce, left

            parent_1 "Yes sure! That is a good idea. I will do that, so you can go get ready for bed now!"

            hide mc_placeholder
            hide parent_1_base_expression

            "You get up, walk to your parents’ room, and ask if they can record the episode."
            "They appreciate that you're thinking ahead and agree. You go to bed feeling relieved, knowing you won’t miss out and will still get enough rest."

            return

        label .turn_tv_back_on:

            show mc_placeholder at bounce, right

            mc "Alright… If i HAVE to then I will go to bed now…"

            show parent_1_base_expression at bounce, left

            parent_1 "Good night [mc]! And thanks for listening to me. I am sure you will feel better this way tomorrow!"
            parent_1 "But I know it is hard to stop watching if an episode gets interesting. I am proud of you for still choosing to go to bed."

            "You go to bed, but you keep tossing and turning, unable to stop thinking about what you missed. Frustrated, you sneak back into the living room and turn the TV on at a low volume."
            "At first, it feels like a good idea, but you end up watching way longer than planned. The next morning, you’re exhausted and struggle to wake up."

            return


    label .keep_watching:

        show mc_placeholder at bounce, right

        mc "Hmmm…. okay I will turn it off in a second…"

        "… but you never do. So you decide to ignore the bedtime call and stay on the couch, enjoying your show. It feels great in the moment, but soon, you have to face the consequences:"

        menu:
            "Continue watching TV for as long as you want.":
                jump .continue_watching
            
            "Listen to your parents and go to bed.":
                jump .listen_to_parents
        
        label .continue_watching:

            hide mc_placeholder
            hide parent_1_base_expression

            "You let the episodes keep playing, telling yourself “just one more”—"

            "Until you can barely keep your eyes open. By the time you finally turn off the TV, it’s way too late."

            "The next morning, you feel exhausted, making it really hard to get up, focus in school, and enjoy the day." 
            "But you know “It is not a catastrophe to be tired today, mistakes are what helps me understand my decisions better. Today will be exhausting at school but I will still do my best and from now on I will go to bed a little bit earlier.”"

            # go back option here? -------------

            return

        label .listen_to_parents:

            hide mc_placeholder
            hide parent_1_base_expression

            "At first, you ignore your parents and keep watching. .. Then you think to yourself “the last time I did this I was super tired at school the next day and I failed an exam…”" 

            "With a sigh, you turn off the TV and head to bed." 

            "When you go to bed you are content still (thinking) “I will be happy tomorrow, because I will be better able to concentrate tomorrow. I can be proud of myself.”"

            "The next morning, you wake up on time and feel well-rested, making the day much easier."

            return