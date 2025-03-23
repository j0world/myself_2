label scenario_1:
    
    scene bedroom

    "The alarm clock rings loudly, filling the room with a sharp sound."

    show mc_base_expression at bounce, center

    mc "Ugh… I don't want to go to school today. Not today… maybe I can just stay here, under the covers, for another hour…"

    "So you just ignore the alarm for now…"

    hide mc_base_expression

    show parent_1_base_expression at bounce, left

    parent_1 "[mc]! Wake up! I don’t want to hear that alarm ringing anymore. Get up, it’s time for school!"

    show mc_base_expression at bounce, right

    mc "But … I really don’t want to today. I’m so tired… I just can’t. And… I feel so… I don’t feel well at school."

    show parent_1_base_expression at bounce, left

    parent_1 "You seem really down today. I understand. Sometimes school can feel like a tough place, but I want you to know that you’re strong."
    parent_1 "If you’re not feeling up to going today, let’s talk about it. You don’t have to go through this alone."

    show mc_base_expression at bounce, right

    mc "But I REALLY don’t want to go…"

    parent_1 "It’s not about changing everything in one day, it’s about taking one step at a time. You’re already so brave for facing each day, even when it’s hard. Do you want to go today? I want you to make the choice for yourself."

    menu:
        "Go to school.":
            jump .go_to_school
        "Stay home.":
            jump .stay_home
    
    label .go_to_school:
        
        show mc_base_expression at bounce, right

        mc "I want to try, but I’m not sure I can do it."

        show parent_1_base_expression at bounce, left

        parent_1  "You’re stronger than you think. And you’re not alone. We’re with you, always."
        parent_1 "Alright, enough talking. Get up. I’ll make breakfast. I will wait for you in the living room."

        mc "Okay, okay… I’ll go. But only because you convinced me. And… thanks for understanding."

        scene living_room # change to living room

        "You have had a quick breakfast and are going to school now, even though you still feel apprehensive about it."

        hide mc_base_expression
        hide parent_1_base_expression

        jump in_classroom
    
    label .stay_home:

        show parent_1_base_expression at bounce, left

        parent_1  "Are you still not up? It’s late for breakfast. If this keeps up, you’ll be late. I know this week has been tough but you really need to move, please!"

        show mc_base_expression at bounce, right

        mc "But I really do not feel good, it stresses me out just to think about arriving there! And maybe… I also feel a bit sick..?"

        show parent_1_base_expression at bounce, left

        parent_1 "I get that, but school is non negotiable. It is so important for your future. When you come back home we can sit down and think about how we could change something. Would that help?"

        show mc_base_expression at bounce, right

        mc "No! I just don’t want to go!!"

        show parent_1_base_expression at bounce, left

        parent_1  "Ugh, okay. I can’t make you go. But I don’t want this to become a habit. You are old enough to take responsibility [mc]. I really believe you can!"

        show mc_base_expression at bounce, right

        mc "It’s not about avoiding challenges!! Can you just leave my room!?"

        hide parent_1_base_expression

        "… after a view minutes you decide to go and grudgingly go to tell your parent who is in the living room …"

        scene living_room # change to living room

        show mc_base_expression at bounce, right

        mc "... can I get some breakfast?"

        show parent_1_base_expression at bounce, left

        parent_1 "You are already very late for school. I packed you something for the way but you need to hurry."
        parent_1 "You know what, I will drive you! Then you can eat in the car. How does that sound?"

        show mc_base_expression at bounce, right

        mc "..Thank you!"

        hide mc_base_expression
        hide parent_1_base_expression

        jump late_for_school



