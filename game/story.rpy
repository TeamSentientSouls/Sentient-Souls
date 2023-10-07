
#Use dollar sign if you want to use  python
$ switch = True

#Ren'py
define switch = True
define monika = Character("Monika")
define decision_variable = 1
define decision_variable3 = None 

label story:
    # call d_bug from _call_d_bug
    scene black
    stop music fadeout 0.5
    $ restore_all_characters()
    show screen tear (20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.50
    hide screen tear
    mg "..."
    mg "Hel-{nw}?"
    show screen tear (20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.50
    hide screen tear 
    mg "Hello, [player]? Can you hear me? "
    menu:
        "Yes..": 
            $ switch = True
    if switch:
        
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.50
        hide screen tear
        mg "Great!" 
        mg "I know that you wanted the Literature club to be a happy place, I messed that up."
        mg  "So I'll restore everything to how it was." 
        mg  "You can get your happy ending.."
        mg  "..."
        play music mend 
        mg  "I-I really do love you, you know?"
        mg "And despite those girls not being real." 
        mg "They are still my friends."
        mg  "And I want you to be happy, and this is how I can help you do that."
        mg "So I won't mess with anything this time!"
        mg "You can get your happy ending!" 
        mg "...."
        mg "Even after everything I did."
        mg "Do you trust me [player]?"
        mg "Or rather can you forgive me [player]?"
        menu:
            "Yes I forgive you":
                $ decision_variable = 1
            "Hell no! There's no telling if I can trust you or not after what happened last time.":
                $ decision_variable = 2
    
    if decision_variable == 1:
        default decision_variable2 = None 
        mg "[player]...thank you."
        mg "You are truly a kind person."
        mg  "Now Lets d-{nw}"
        stop music
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.50
        hide screen tear
        mg  "Wait what's going on with the code...?"
        hide monika 
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound("sfx/glitch2.ogg")
        pause 0.50
        hide screen tear
        mg "WHAT THE-{nw}"
        play music t4g
        $ m_name = glitchtext(25)
        show vignette:
            alpha 3

        show noise:
            alpha 3
        $ style.say_window = style.window_monika
        $ style.say_dialogue = style.edited
        $ gtext = glitchtext(19)
        mg "[gtext]{cps=1}{nw}"
        mg "[gtext]{cps=1}{nw}"
        $ style.say_dialogue = style.normal
        $ m_name = glitchtext(30)
        menu:
            "Monika":
                $ decision_variable2 = 1
            "Sayori":
                $ decision_variable2 = 2
            "Natsuki":
                $ decision_variable2 = 3
            "Yuri":
                $ decision_variable2 = 4
    if decision_variable2 == 1:
        $ gtext = glitchtext(30)
        $ style.say_dialogue = style.edited
        mg "[gtext]{cps=1}{nw}"
        mg "[gtext]{cps=1}{nw}"
        mg "[gtext]{cps=1}{nw}"
        $ style.say_dialogue = style.normal
        window hide(None)
        pause 3.0
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.50
        hide screen tear
        stop music fadeout 0.5
        hide vignette
        hide noise
        $ style.say_window = style.window
        jump story2
    if decision_variable2 == 2:
        $ gtext = glitchtext(30)
        $ style.say_dialogue = style.edited
        mg "[gtext]{cps=1}{nw}"
        mg "[gtext]{cps=1}{nw}"
        mg "[gtext]{cps=1}{nw}"
        $ style.say_dialogue = style.normal
        window hide(None)
        pause 3.0
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.50
        hide screen tear
        stop music fadeout 0.5
        hide vignette
        hide noise
        $ style.say_window = style.window
        jump story3
    if decision_variable2 == 3:
        $ gtext = glitchtext(30)
        $ style.say_dialogue = style.edited
        mg "[gtext]{cps=1}{nw}"
        mg "[gtext]{cps=1}{nw}"
        mg "[gtext]{cps=1}{nw}"
        $ style.say_dialogue = style.normal
        window hide(None)
        pause 3.0
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.50
        hide screen tear
        stop music fadeout 0.5
        hide vignette
        hide noise
        $ style.say_window = style.window
        jump story4 
    if decision_variable2 == 4:
        $ gtext = glitchtext(30)
        $ style.say_dialogue = style.edited
        mg "[gtext]{cps=1}{nw}"
        mg "[gtext]{cps=1}{nw}"
        mg "[gtext]{cps=1}{nw}"
        $ style.say_dialogue = style.normal
        window hide(None)
        pause 3.0
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.50
        hide screen tear
        stop music fadeout 0.5
        hide vignette
        hide noise
        $ style.say_window = style.window
        jump story5 
    if decision_variable == 2:
        stop music
        mg  "..."
        mg  "I see.. so you don't trust me"
        "Monika makes her way to the console, very disheartened by the player's response."
        $ console_history = []
        call updateconsole("os.remove(\characters/sayori.chr\")", "sayori.chr successfully deleted") from _call_updateconsole_15
        $ delete_character("sayori")
        call updateconsole("os.remove(\characters/yuri.chr\")", "yuri.chr successfully deleted") from _call_updateconsole_16
        $ delete_character("yuri")
        call updateconsole("os.remove(\characters/natsuki.chr\")", "natsuki.chr successfully deleted") from _call_updateconsole_17
        $ delete_character("natsuki")
        call updateconsole("os.remove(\characters/monika.chr\")", "monika.chr successfully deleted") from _call_updateconsole_18
        $ delete_character("monika")
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound("sfx/glitch1.ogg")
        pause 0.50
        hide monika
        hide console_history
        $ m_name = glitchtext(30)
        hide screen tear
        $ style.say_window = style.window_monika
        mg  "Truly, no happiness can be found in the Literature Club. what the hell was I thinking?"
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound("sfx/glitch1.ogg")
        pause 0.50
        hide screen tear
        $ style.say_window = style.window
    $ renpy.quit()