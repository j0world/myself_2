label in_classroom:

    scene classroom

    show teacher_base_expression at bounce, center

    teacher "Alright, everyone. Today we’re starting a new group project. Each group will work on a topic related to what we’ve studied together."

    "Whispers fill the classroom. Eyes meet. Some smile. You stay quiet."

    hide teacher_base_expression

    show mc_base_expression at bounce, center

    mc "I knew it... another group project."

    hide mc_base_expression

    show teacher_base_expression at bounce, center

    teacher "As usual, I will be assigning the groups. Get ready."

    hide teacher_base_expression

    show mc_base_expression at bounce, center

    mc "Here we go again. I’ll end up with the same classmates I struggle to work with."

    hide mc_base_expression

    show classmate_1 at bounce, left

    classmate_1 "Teacher, what topic will our group be working on?"


    show teacher_base_expression at bounce, right

    teacher "I think you’ll like it... Street art."

    hide classmate_1
    hide teacher_base_expression

    show mc_base_expression at bounce, center

    mc "Street art? Finally, something interesting might happen today."

    "What do you want to do?"

    menu:
        "Join group work":
            hide mc_base_expression
            jump .join_group_work

        "Work alone":
            hide mc_base_expression
            jump .work_alone

    label .join_group_work:

        "But once you have decided to actually work with the team instead of doing it alone (which would have been easier) you notice that you need to also decide something else:"

        menu:
            "Split tasks fairly":
                jump .split_tasks_fairly
            
            "Take your favorite task":
                jump .take_favorite_task
        
        label .split_tasks_fairly:

            "You decide to split the tasks fairly."

            show classmate_1 at bounce, left

            classmate_1 "I’d like to take care of the graphics, is that okay?"

            show classmate_2 at bounce, right

            classmate_2 "I can prepare the presentation. Maybe something interactive."

            show mc_base_expression at bounce, center

            mc "Perfect. I’ll start gathering information on the history of the movement."

            hide mc_base_expression
            hide classmate_1
            hide classmate_2

            show teacher_base_expression at bounce, center

            teacher "Great job, everyone. I can see real teamwork here."

            hide teacher_base_expression

            jump scenario_3

        
        label .take_favorite_task:

            show mc_base_expression at bounce, right

            mc "I’ll take care of the historical research. You divide the rest."

            show mc_base_expression at bounce, center

            mc "Better to be clear from the start. This way we avoid arguments. Though maybe I was a bit too direct..."

            hide mc_base_expression

            show classmate_2 at bounce, left

            classmate_2 "You could at least ask first, instead of deciding for everyone..."

            hide classmate_2

            show teacher_base_expression at bounce, center

            teacher "Remember: teamwork also means listening and respecting others."

            jump scenario_3

    label .work_alone:

        "You decided not to work with your classmates, because it feels way easier to just do it your way. But should you talk to your teacher about it or do you just go ahead…?"

        menu:
            "Ask to work alone":
                jump .ask_to_work_alone
            "Work alone on your part":
                jump .work_alone_on_your_part

        label .ask_to_work_alone:

            show mc_base_expression at bounce, right

            mc "Teacher, can I work alone? I can concentrate better that way."

            show teacher_base_expression at bounce, left

            teacher "Alright, but your work must still integrate with the group’s project."

            hide mc_base_expression
            hide teacher_base_expression

            show mc_base_expression at bounce, center

            mc "It’s not ideal… but at least I’ll be able to work in peace."

            hide mc_base_expression

            jump scenario_3

        label .work_alone_on_your_part:

            "You grab my notebook and sit far from the others."

            show mc_base_expression at bounce, center

            mc "I’ve decided: I’ll do my part on my own. Less stress."

            hide mc_base_expression

            show classmate_1 at bounce, center

            classmate_1 "Thanks for turning your part in on time, even if you didn’t really work with us..."

            hide classmate_1

            show mc_base_expression at bounce, center

            mc "Maybe I missed a chance to really try working as a team…"

            "You have finished your work on Street Art and are quite proud of yourself!" 
            "Your teammates took a way more prominent role in presenting the results, because you don’t feel too comfortable talking in front of the whole class, but whatever! You don’t need to tackle everything at once."

            hide mc_base_expression

            jump scenario_3





    

label late_for_school:

    scene classroom

    "You arrive in front of the closed classroom door. Before opening it, you stop for a moment."

    show mc_base_expression at bounce, center

    mc "Oh no, the lesson has already started!"
    
    "You open the door and the chatter stops; everyone is silent, and all eyes are on you. The teacher is standing at the front of the class with arms crossed, looking at you."

    hide mc_base_expression

    show teacher_base_expression at bounce, center

    teacher "Finally. Can you explain why you’re late, [mc]?"

    "It’s time to make a decision." 

    menu:
        "Continue to your seat.":
            jump .continue_to_seat

        "Restart the day.":
            hide mc_base_expression
            hide teacher_base_expression
            jump .rewind_time
    
    label .continue_to_seat:

        "You take a step forward, enter the classroom."

        show teacher_base_expression at bounce, center

        teacher "I’ll report you to the principal."

        "You are angry but what are you going to do… You sit at your desk."

        jump in_classroom
    
    label .rewind_time:

        "You take a step forward, enter the classroom."

        show teacher_base_expression at bounce, center

        teacher "I’ll report you to the principal."

        "If you could go back and avoid being late by changing the sequence of events that led you here..."

        jump scenario_1

