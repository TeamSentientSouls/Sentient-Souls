define talk = None
label day3Yuri:
    scene bg bedroom 
    "Ugh, what time is it?"
    "I go to check the clock, and I quickly realize.."
    play music t7
    "OH SHIT I'M GOING TO BE LATE!"
    "I throw on my clothes, and then head out quickly."
    scene bg kitchen with wipeleft_scene
    scene bg house with wipeleft_scene 
    "Sayori isn't outside, I'm guessing she's already made it to school. Not even she wakes up this late."
    "I rush to the school."
    scene bg corridor with wipeleft_scene
    scene class with wipeleft_scene
    "I make it to class just in time, and sit down."
    "Guess it's time to listen to this teacher lecture for hours..."
    stop music fadeout 1.0
    scene bg class_day with wipeleft_scene
    "The day drags on so slowly, I can feel the anxiety of returning to the club swelling up in me, but I know I have to bring back the club for everyone's sake."
    scene bg corridor with wipeleft_scene
    "I make my way towards the clubroom, bracing for the possible damage due to yesterday."
    scene bg club_day 
    "I arrive in the clubroom, and I'm met with just a few faces..."
    "Monika, and Natsuki... I thought for sure Sayori would be here."
    "I make my way to Monika's desk to ask her whats going on."
    mc "Hey Monika... Where's Sayori? I understand Yuri not being here... but Sayori?"
    play music t10 fadein 0.5
    show monika 1p at t11 zorder 1 
    m "She seemed.. Really down about what happened yesterday. Yuri's probably still pissed off. I'm surprised Natsuki is here; she hasn't said a word to me."
    mc "Maybe I could talk to her? She usually says something, considering how... She can be at times."
    mc "Don't take it the wrong way though."
    show monika 1g at t11 zorder 1 
    "Monika is still downcast, I guess that joke was in bad taste."
    m "[player] I don't think this is the time for jokes."
    "Monika appears as she is about to cry."
    m 1g "I just really want to see them back together"
    m "I've worked so hard for this club."
    show monika 1p at s11 zorder 1 
    "Monika then starts to cry."
    m "I really don't want it to crumble.. Not like this.." #Note to self, please add a custom pose of Monika tearing up for this scene. -Void
    mc "Monika.."
    mc "I will help you get through this; I will help the club get through this."
    mc "Just relax and take some deep breaths."
    mc "I am here for you."
    "Me and Monika share a tight embrace." #Possibly add a CG for this? I know It's not Monika's route but it would be a really nice touch. -Void
    show monika 2c at t11 zorder 1
    m "You should go talk to Sayori though. She seems really down after yesterday, and I think she could really use someone to talk to."
    mc "Is it that urgent?"
    m "Seems that way."
    m "I want everyone to get back together. I don't want to screw this up.. You really should talk to Sayori."
    "I get what Monika is saying, but we can't disregard Natsuki either. She might also need someone to talk to. Should I listen to Monika or help out Natsuki?"
menu:
    "Talk to Natsuki":
        $talk = 1
    "Talk to Sayori":
        $talk = 2
if talk == 2: 
    $ decisions_ending += 1
    mc "I'll go talk to Sayori. I trust your judgement Monika, and if it's that urgent, then I should."
    m 1a"Thank you [player]. I think she'll really appreciate you talking to her."
    m 1d "I'll go talk to Natsuki. Hopefully I can help her calm down. You go talk to Sayori; We need to fix things."
    mc "Alright, got it. Thanks again Monika for letting me know."
    m 1e "It's no problem."
    show monika at thide zorder 1 
    hide monika 
    "Alright, time to head to Sayori's"
    "Something feels.. off, but I brush it off."
    scene bg residential_day with wipeleft_scene
    play music suspensepiano fadein 1.0
    "Walking all by myself feels kind've sad. It's always nice to have Sayori blabbering about whatever."
    "Hopefully I can help her with what ever she's dealing with..?"
    "I'm still just wondering what could be wrong with Sayori.."
    "She's always so vibrant and full of joy. It's so unlike her."
    scene bg house with wipeleft_scene
    "I make it to her house and knock on her door."
    mc "Sayori? Are you home?"
    "Sayori doesn't answer oddly enough."
    mc "Sayori!! Are you in there?"
    "She still doesn't answer."
    play sound audio.wind
    "I hear absolutely nothing. All I hear is the wind, and absolute dead silence."
    "The wind sends shivers down my spine, and it doesn't help me feel better."
    "I feel like something terrible is going to happen."
    "Why do I feel this way?"
    "I knock once last time."
    mc "Sayori! Are you ok? Please say something!"
    "I'm greeted by nothing but the wind and the sound of silence."
    "That's it. I'm going in."
    "I gently open the door."
    "I walk inside the house, slowly opening the door with anticipation."
    play sound audio.closet_open 
    scene bg kitchen with wipeleft
    "It doesn't take me even a second to find Sayori."
    show sayori 1u at t11 zorder 1 
    stop music fadeout 1.0 
    "Sayori is in her living room. Zoned out completely. Staring at nothing."
    mc "Sayori..?"
    "There's tears in her eyes, and then she finally snaps out of her trance."
    play music ifonlyyou fadein 1.5   
    s 2t "Oh! Your uh..."
    s "You're here..."
    s "Hehe.."
    mc "Sayori, is everything okay?"
    mc "I'm here for you.. y'know?"
    s 1v "[player]..."
    s "I'm so lost.."
    "Sayori starts to lose her composure."
    "I've never seen Sayori like this before."
    s "I've failed my friends."
    s "The clubs falling apart."
    s 1w "AND I CAN'T DO ANYTHING ABOUT IT!"
    mc "Sayori.."
    mc "You can not put this on yourself."
    mc "You can't put the entire weight of the world on your shoulders."
    mc "You've done.. An absolutely fantastic job at helping your friends."
    mc "I've never seen someone so invested in keeping their friends happy."
    mc "How you do it.. Sayori.. Is completely beyond me."
    mc "But things happen."
    s 1u "..."
    s "[player].."
    s "It feels like I've failed at my purpose.."
    mc "Well, we are both in this club. Monika is too."
    mc "We can all fix this together."
    mc "Natsuki was even at the club today. Its not all bad you know?"
    s "She.. was?"
    mc "Yes she was Sayori. Things aren't the best, but they are mendable.. You know?"
    s "I just don't believe it [player]."
    s "I..."
    mc "Sayori, are you good?"
    s "[player].. I need to tell you something important."
    "This sounds worrying.."
    s "You see.. the thing is."
    s "I.."
    show screen tear (20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    scene black
    stop music
    mc "What the hell?"
    mys "STOP!!"
    mc "WHAT IS GOING ON??"
    play music creepypanic
    "I have absolutely no clue what is going on. I need to get back to Sayori."
    "I don't know if I'm hallucinating or what, but I just want to-"
    "I hear a soft sob."
    "This is offically weird as hell. I've never experienced something of this caliber."
    "This feels like a nightmare."
    "Yet, a different voice kicks it. It sounds distorted but familar."
    mys "Please.. Calm down.."
    "Am I hearing a conversation right now?"
    mys "{b}SHUT UP! EVERYTHING THAT HAPPENED IS YOUR FAULT! YOU FUCKING LITTLE BIT-{/b}"
    stop music
    play sound audio.glass 
    pause 1
    mys "I.."
    pause 0.2 
    mys "You.."
    pause 0.2
    "The distorted voices soft sobs turn into a full blown cry."
    mys "I can't believe that yo-"
    show screen tear (20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    scene bg kitchen 
    show sayori 4w at h11 zorder 1 
    s "[player]!"


    
    
    



    

    