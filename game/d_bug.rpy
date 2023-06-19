

init python:
    def edit_txt(file_name, text):
        with open(config.gamedir + "/" + file_name, "w") as f:
            f.write(text)
        return
label d_bug:

    "Welcome what should we test out?"

    menu:
        "Glitch effect":
            "Which glitch do you want to see?"
            menu:
                "Screen tear":
                    show screen tear(20, 0.1, 0.1, 0, 40)
                    pause 5.0
                    hide screen tear
                    jump d_bug

                "Character glitch":
                    "Which character?"
                    menu:
                        "Monika":
                            "Which glitch do you want to see?"
                            menu:
                                "1":
                                    #That werid cat glitch monika from act2
                                    show monika g1 at t11 zorder 1
                                    $ m_name = "Monika"
                                    m "Hi [player]"
                                    hide monika
                                    jump d_bug


                                "2":
                                    #when you delete monika in act3
                                    show monika g2 at t11 zorder 1
                                    $ m_name = "Monika"
                                    m "I don't feel so good"
                                    hide monika
                                    jump d_bug

                        "Sayori":
                            "which glitch do you want to see?"
                            menu:
                                "1":
                                    #glitch out sayori from the start act2 
                                    show sayori glitch at t11 zorder 1
                                    $ s_name = "Sayori"
                                    s "..."
                                    hide sayori
                                    jump d_bug
                            

                        "Natsuki":
                            "which glitch do you want to see?"
                            menu:
                                "1":
                                    # blue glitch one from act2
                                    show natsuki glitch1 at t11 zorder 1
                                    $ n_name = "Natsuki"
                                    n "..."
                                    hide natsuki
                                    jump d_bug


                                "2":
                                    # the creepy neck snapping one from act2
                                    show natsuki ghost1 at t11 zorder 1
                                    $ n_name = "Natsuki"
                                    n "..."
                                    show natsuki ghost2 at t11 zorder 1
                                    n "..."
                                    show natsuki ghost3 at t11 zorder 1
                                    n "..."
                                    show natsuki ghost4 at t11 zorder 1
                                    n "..."
                                    
                                    hide natsuki
                                    jump d_bug



                            
                        "Yuri":
                            "which glitch do you want to see?"
                            menu:
                                "1":
                                    #Glitch out yuri from act2
                                    show yuri glitch at t11 zorder 1
                                    $ y_name = "Yuri"
                                    y "..."
                                    hide yuri
                                    jump d_bug

                                "2":
                                    #yuri face glitch from act2
                                    show yuri glitch2 at t11 zorder 1
                                    $ y_name = "Yuri"
                                    y "..."
                                    hide yuri
                                    jump d_bug

                                "3":
                                    #the one with dragon eyes from act2
                                    show yuri dragon at t11 zorder 1
                                    $ y_name = "Yuri"
                                    y "..."
                                    hide yuri
                                    jump d_bug

                                "4":
                                    #Her killing herself
                                    show yuri stab_1 at t11 zorder 1
                                    $ y_name = "Yuri"
                                    y "..."
                                    show yuri stab_2 at t11 zorder 1
                                    pause 0.5
                                    show yuri stab_3 at t11 zorder 1
                                    pause 0.5
                                    show yuri stab_4 at t11 zorder 1
                                    pause 0.5
                                    show yuri stab_5 at t11 zorder 1
                                    pause 0.5
                                    show yuri stab_6 at t11 zorder 1
                                    y "..."
                                    hide yuri
                                    jump d_bug




                    

            

        "Write file in Sentient Souls folder":
            $ edit_txt("Hey.txt", "Did this work finally?")
            
                
            
            "File should be in Sentient Souls folder go check"
            jump d_bug


        "Test transforms":
            show monika 3a at i11 zorder 1
            "Instant appearance"
            show monika 3a at l11 zorder 1
            "Slide from the left"
            show monika 3a zorder 1 at lhide
            hide monika
            "Slide exit on left"
            show monika 3a at t11 zorder 1
            "Default"
            show monika 3a at s11 zorder 1
            "sink"
            show monika 3a at f11 zorder 1
            "focus"
            show monika 3a at hf11 zorder 1
            "hop + focus"
            show monika 3a at h11 zorder 1
            "hop"
            show monika 3a at d11 zorder 1
            "dip"
            show monika 3a at p11 zorder 1
            "unused panic"
            show monika 3a at pf11 zorder 1
            "Custom transform that I made: panicfast"
            show monika 3a at w11 zorder 11
            "Custom transform that I made: wiggle"
            show monika 3a at wl11 zorder 1
            "Custom transform that I made: wiggle looped"
            #show monika 3a at vs11 zorder 1
            #"Custom transform that I made: violent shake"
            show monika zorder 1 at rhide
            hide monika
            "Custom transform that I made: Slide exit on right"
            jump d_bug



        "Quit":
            "See ya [player]"
            $ renpy.quit()
            return

#
