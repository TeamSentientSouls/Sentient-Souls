define decision_argument = None 
label yuri_day2:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    define decisions_ending = 0 
    "Another day passes, and it's time for the club meeting already."
    "I've gotten a little more comfortable here over the past couple days."
    "Entering the clubroom, the usual scene greets me."
    show sayori 2x at t11 zorder 2
    s "Hi [player]~"
    mc "Yo, Sayori."
    mc "Looks like you're in a good mood today."
    s 1q "Ehehe~"
    s "I'm just still not used to you being in the club, that's all."
    mc "I see..."
    mc "...That's a pretty simple thing to get you in a good mood."
    mc "But I guess it's always the simple things with you, anyway."
    s 1d "Speaking of which..."
    s "I'm kinda hungry..."
    s "Will you come with me to buy a snack?"
    mc "No thanks."
    s 4h "Eh??"
    s "T-That's not like you at all!!"
    mc "I have my reasons."
    mc "Why don't we take a look at your purse, Sayori?"
    s 4l "E-Eh?"
    show sayori at s11
    s "Why that...all of a sudden?"
    mc "No reason, really."
    mc "I just wanted to look at it."
    s 1l "A-Ah..."
    show sayori at t11 zorder 2
    "Sayori nervously retrieves her coin purse."
    "She fumbles with the latch and gets it open."
    "Then, she turns it upside-down and lets its contents spill onto the desk."
    "Only two small coins fall out."
    s 5a "A-Ahaha..."
    mc "I knew it..."
    mc "I can see right through you, Sayori."
    s 5c "That's not fair!"
    s "How did you even know?"
    mc "It's simple."
    mc "If you had enough money in the first place, you would have bought a snack before coming to the clubroom."
    mc "So, either you're not hungry and wanted an excuse to take a walk..."
    mc "Or, you planned to conveniently forget that you spent all your money, so that I would lend you some!"
    mc "But there's one more thing..."
    mc "...You're always hungry!"
    mc "And so, that only leaves the one option!"
    s 4p "Uwaaa~!"
    s "I give up!"
    s "Don't make me feel guiltyyy!"
    mc "If you feel guilty, that means you deserve to feel guilty..."
    show yuri 1c at t33 zorder 2
    y "Pfff.."
    "Yuri suddenly giggles."
    show sayori 4g
    mc "Eh?"
    "I didn't notice that she was listening in."
    "Her face is in her book, as always."
    show sayori at f32 zorder 3
    s 1h "Yuriiii..."
    s "Tell [player] to let me borrow some money..."
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y 3h "That's--!"
    y "Don't get me involved like that, Sayori..."
    y "Besides..."
    y 1k "You should only buy what you can responsibly afford..."
    y "And frankly, after pulling a mischievous little stunt like that, your suffering is fair enough retribution."
    show sayori 1b
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1r "Ahaha!"
    s 3x "I really like when you speak your mind, Yuri..."
    s "It doesn't happen much, but it's a fun side of you!"
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y 3j "That's..."
    y "I already told you.. I was planning on getting out of my comfort zone."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1x "You were right, though..."
    s "I did something bad and now I have to accept the revolution."
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y 3h "Retribution..."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1l "That!"
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y "Still, coming from you, Sayori..."
    y 1h "I guess there's a devil inside all of us, isn't there?"
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1q "Ehehe..."
    show sayori at t32 zorder 2
    mc "Don't let her fool you."
    mc "Sayori knows exactly what she's doing."
    mc "After all, she told you guys she was bringing me to the club before she even told me..."
    show sayori at f32 zorder 3
    s 1h "B-But...!"
    s "You wouldn't have come if it weren't for the cupcakes..."
    s "So I had to trick Natsuki into making them!"
    show sayori at t32 zorder 2
    mc "Come on, give me more credit than that, Sayori."
    show sayori at f32 zorder 3
    s 1l "Ehehe..."
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 4p at hf32 zorder 3
    "{i}Pwap!{/i}"
    hide white
    s 4p "Kyaa--!"
    "Out of nowhere, something smacks Sayori in the face and tumbles onto the desk."
    s 4j "Ow..."
    s "What was--"
    s 4n "Eh??"
    s "A-A cookie!"
    "Sure enough, it's a giant cookie wrapped in plastic."
    "Sayori glances around."
    s 4m "I-Is this a miracle??"
    s "It's because I paid my restitution!"
    show sayori at t32 zorder 2
    mc "Retribution..."
    show sayori 4n
    show yuri at f33 zorder 3
    y 1h "Actually, that almosts works..."
    show yuri at t33 zorder 2
    show natsuki 3z at f31 zorder 3
    n "Ahahaha!"
    n "I {i}was{/i} just gonna give it to you."
    n 3d "But then I heard you blab about the cupcakes."
    n "It was totally worth seeing your reaction, though. Ahaha!"
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 4m "N-Natsuki!"
    s "That's so nice of you!"
    s 4s "I'm so happy..."
    "Sayori hugs the cookie."
    show sayori at t32 zorder 2
    mc "Jeez, just eat it..."
    "Sayori rapidly tears open the wrapper and takes a big bite."
    show sayori at f32 zorder 3
    s 4q "Sho good..."
    show sayori at hf32 zorder 3
    s 4o "Mmf--!"
    "Sayori suddenly clasps her hands over her mouth."
    s 4p "I bit my tongue..."
    show sayori at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3a "Ehehe."
    n "You're going through a lot over just one cookie."
    "Natsuki takes a bite of her own cookie."
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 1c "Ah, yours looks really good too, Natsuki!"
    s "Can I try it?"
    show sayori at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4e "Jeez..."
    n "Beggars can't be choosers!"
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 1h "But yours is chocolate..."
    show sayori at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4c "Yeah, why do you think I gave you that one?"
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 1g "Fine..."
    s 1q "Still, I'm really happy that you shared this one with me."
    s "Ehehe~"
    show sayori at t21 zorder 2 behind natsuki
    "Sayori gets out of her seat and goes behind Natsuki, then wraps her arms around her."
    n 12c "Ah-- Jeez..."
    n "I get it, I get it."
    "Cookie still in hand, Natsuki reaches up to nudge Sayori off of her."
    show sayori 1n at h21
    s "...{i}Om.{/i}"
    "Sayori suddenly leans down and takes a bite out of Natsuki's cookie."
    n 1p "{i}H-Hey!!{/i}"
    n "Did you seriously just do that?!"
    s 1q "Uhuhuhu!"
    show sayori at lhide
    hide sayori
    "Mouth full, Sayori trots away to safety."
    show yuri 1c
    "Yuri and I laugh as well."
    show yuri 1a
    show natsuki at f31 zorder 3
    n 1w "Jeez! You're such a kid sometimes!"
    n 1h "Monika! Can you tell Sayori--"
    n 1c "--Eh?"
    "Natsuki glances around."
    "Monika isn't in the clubroom."
    n 4q "Ugh..."
    n "Where's Monika, anyway?"
    show natsuki at t31 zorder 2
    show yuri 2f at f33 zorder 3
    y "Good question..."
    y "Have any of you heard anything about her being late today?"
    "Yuri silently whispers to herself something, but I don't think any of the other members hear it."
    show yuri 2h
    y "You would think she'd try a little harder.. We just got a new member."
    show sayori 1b at f32 zorder 3
    show yuri at t33 zorder 2
    s "Not me..."
    show sayori at t32 zorder 2
    mc "Yeah, I haven't either."
    show yuri at f33 zorder 3
    y 2l "Hm..."
    y "That's a bit unusual."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1g "I hope she's okay..."
    show sayori at t32 zorder 2
    show natsuki 3k at f31 zorder 3
    n "Of course she's okay."
    n "She probably just had something to do today."
    n 3t "She's pretty popular, after all..."
    show natsuki at t31 zorder 2
    show sayori 4m at f32 zorder 3
    s "Eh?"
    s "You don't think she..."
    s "She has a...!"
    show sayori at t32 zorder 2
    show yuri 1h at f33 zorder 3
    y "I wouldn't be surprised."
    show yuri at t33 zorder 2
    show sayori 1r at f32 zorder 3
    show sayori at t32 zorder 2
    show natsuki 1p at f31 zorder 3
    hide natsuki
    hide sayori
    hide yuri
    with wipeleft
    "Suddenly, the door swings open."
    show monika 1g at l41
    m "Sorry! I'm super sorry!"
    mc "Ah, there you are..."
    m "I didn't mean to be late..."
    m "I hope you guys weren't worried or anything!"
    show sayori 4n at f42 zorder 3
    s "Eh??"
    s "Monika chose the club over her boyfriend after all!"
    s "You're so strong-willed!"
    show sayori at t42 zorder 2
    show monika at f41 zorder 3
    m 1l "B-Boyfriend...?"
    m "What on Earth are you talking about Sayori?"
    "Monika quizzically glances at me."
    show monika at t41 zorder 2
    mc "Ah, never mind that..."
    mc "What held you up, anyway?"
    show monika at f41 zorder 3
    m 1e "Ah..."
    m "Well, my last period today was study hall."
    m "To be honest, I kind of just lost track of time..."
    m "Ahaha..."
    show monika at t41 zorder 2
    show natsuki 2c at f43 zorder 3
    n "That makes no sense, though."
    n "You would have heard the bell ring, at least."
    show natsuki at t43 zorder 2
    show monika at f41 zorder 3
    m 1m "I must not have heard it, since I was practicing piano..."
    show monika at t41 zorder 2
    show yuri 1e at f44 zorder 3
    y "Piano...?"
    y "I wasn't aware you played music as well, Monika."
    show yuri at t44 zorder 2
    show monika at f41 zorder 3
    m 1l "Ah, I don't, really...!"
    m "I kind of just started recently."
    m 1m "I've always wanted to learn piano."
    show monika at t41 zorder 2
    show sayori 4x at f42 zorder 3
    s "That's so cool!"
    s "You should play something for us, Monika!"
    show sayori at t42 zorder 2
    show monika at f41 zorder 3
    m "That's..."
    "Monika looks at me."
    m 1a "Maybe once I get a little bit better, I will."
    show monika at t41 zorder 2
    show sayori at f42 zorder 3
    s 4q "Yay~!"
    show sayori at t42 zorder 2
    mc "That sounds cool."
    mc "I'd also look forward to it."
    show monika at f41 zorder 3
    m 1b "Is that so?"
    m 4k "In that case, I'll work hard for everyone!"
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    show monika 5 at t11 zorder 2
    hide sayori
    hide natsuki
    hide yuri
    "Monika smiles sweetly."
    mc "Ah..."
    mc "I didn't mean any pressure or anything like that!"
    m 1a "Ahaha, don't worry."
    m "I've been practicing a whole lot recently."
    m "And I'd really love the chance to share once I'm ready."
    mc "I see..."
    mc "In that case, best of luck."
    m 1j "Thanks~!"
    m 1a "So, I didn't miss anything, did I?"
    mc "Not...not really."
    show monika at thide zorder 1
    hide monika
    "I choose to leave out Sayori's mischievous escapade."
    "I'm sure Natsuki will end up complaining to her, anyway."
    "It looks like everyone has already settled down."
    "Sayori somehow already finished her entire cookie."
    "Yuri is back to her book, and Natsuki disappeared into the closet."
    scene bg club_day
    with wipeleft_scene
    "I'm really curious to talk to Yuri a little bit more..."
    "But at the same time, I would feel bad for distracting her from reading."
    "I catch a glimpse of the cover of her book."
    "It looks like the same book that she lent to me..."
    "More than that, she seems to be on the first few pages."
    play music t6 fadeout 1.0
    show yuri 1e at t11 zorder 2
    y "Ah..."
    "Crap--"
    "I think she noticed me looking at her..."
    "She sneaks another glance at me, and our eyes meet for a split second."
    y 1i "..."
    "Then it looks as she's about to say something, but I take the initiative."
    mc "Sorry..."
    mc "I was just spacing out..."
    "I mutter this, sensing I made her uncomfortable."
    y 1g "Oh..."
    y "It's fine..."
    y 1a "If I was focused, then I probably wouldn't have noticed in the first place."
    y "But I'm just re-reading a bit of this, so..."
    mc "That's the book that you gave me, right?"
    y "Mhm."
    y "I wanted to re-read some of it."
    y 2d "So I could be ready incase you wanted to read with me!"
    mc "Just curious, how come you have two copies of the same book?"
    y 3l "Ah..."
    y "Well, when I stopped at the bookstore yesterday--"
    y 1q "I...just happened to buy two of them."
    mc "Ah, I see."
    mc "I'll definitely start reading it soon!"
    y 2u "I'm glad to hear..."
    y "Once it starts to pick up, you might have a hard time putting it down."
    y 2c "It's a very engaging and relatable story."
    mc "Is that so...?"
    mc "What's it about, anyway?"
    y 1f "Well..."
    y "Mmm..."
    "Yuri closes the book and scans her eyes over the back."
    "The book is titled \"Portrait of Markov\"."
    "There's an ominous-looking eye symbol on the front cover."
    y 1a "Alright..."
    y "I just wanted to make sure I don't accidentally give anything away."
    y "Basically, it's about this girl in high school who moves in with her long-lost younger sister..."
    y "But as soon as she does so, her life gets really strange."
    y 1m "She gets targeted by these people who escaped from a human experiment prison..."
    y "And while her life is in danger, she needs to desperately choose who to trust."
    y 1i "No matter what she does, she ends up destroying most of her relationships and her life starts to fall apart..."
    mc "That's kind of--!"
    "That's kind of dark, isn't it?"
    "Yuri made it sound like it was going to be a nice story, so that dark turn came from nowhere."
    y 1c "Ahaha."
    "Yuri gently giggles, all of a sudden."
    y "Are you not a fan of that sort of thing, [player]?"
    mc "No, it's not that..."
    mc "I mean, I can definitely enjoy those kinds of stories, so don't worry."
    y 2u "I hope so..."
    "Yeah... I totally forgot that Yuri is into those things."
    y "It's just that those kinds of stories..."
    y 1a "They challenge you to look at life from a strange new perspective."
    y "When horrible things happen not just because someone wants to be evil..."
    y 1m "But because they have their own goals, or their own philosophy that they believe in."
    y "Then suddenly, when you thought you related to the protagonist..."
    y "They're made out to be the naive one for letting their one-sided morals interfere with the villain's plans."
    y 3q "I'm...I'm rambling, aren't I...?"
    y 4b "I'm sorry..."
    mc "Hey, don't apologize...!"
    mc "I haven't lost interest or anything."
    y "Well..."
    y "I guess it's alright, then..."
    y 4a "But I feel like I should let you know that I have this problem..."
    y "When I let things like books and writing fill my thoughts..."
    y "I kind of forget to pay attention to other people..."
    y 3t "So I'm sorry if I end up saying something strange!"
    y "And please stop me if I start talking too much!"
    mc "That's--"
    mc "I really don't think you need to worry..."
    mc "That just means you're passionate about reading."
    mc "The least I can do is listen."
    mc "It's a literature club, after all..."
    "Yuri seems a lot more at ease now that we are reading together.."
    "I do hope that lasts."
    y 1a "Ah--"
    y "That's..."
    y "Well, if that's the case..."
    y 1c "Then we should start reading together!"
    mc "Sounds great!"
    mc "Let me just get the book..."
    "I quickly retrieve the book that I had put into my bag."
    mc "Alright...it's fine if I sit here, right?"
    "I slip into the seat next to Yuri's."
    y 3q "Ah...!"
    y "Yeah..."
    mc "Are you sure?"
    mc "You seem a little apprehensive..."
    y "That's..."
    y 1h "I'm sorry..."
    y "It's not that I don't want you to!"
    y "I'm just not used to reading with someone."
    mc "I see..."
    mc "Well, just tell me if I end up distracting you or anything."
    y 1a "Alright."
    show yuri at thide zorder 1
    hide yuri
    "I open the book and start the prologue."
    "I soon understand what Yuri means about reading in company."
    "It's as if I can feel her presence over my shoulder as I read."
    "It's not a particularly bad thing."
    "Maybe a little distracting, but the feeling is somewhat comforting."
    "Yuri is in the corner of my eye."
    "I realize that she's not actually looking at her own book."
    "I glance over."
    "It looks like she's reading from my book instead--"
    show yuri 3n at t11 zorder 2
    y "S-Sorry!"
    y "I was just--!"
    mc "Yuri, you really apologize a lot, don't you?"
    y "I...I do?"
    y 4a "I don't really mean to..."
    y "Sorry..."
    y 4c "I mean--!"
    mc "Ahaha."
    mc "Here, this should work, right?"
    "I slide my desk until it's up against Yuri's, then hold my book more between the two of them."
    y 2v "Ah..."
    y "I suppose so..."
    "Yuri timidly closes her own copy."
    "Once we each lean in a little bit, our shoulders are almost touching."
    "It feels like my left arm is in the way, so instead I use my right hand to hold the book open."
    mc "Ah, I guess that makes it kind of difficult to turn the page..."
    y "Here..."
    $ persistent.clear[2] = True
    scene y_cg1_base with dissolve_cg
    "Yuri takes her left arm and holds the left side of the book between her thumb and forefinger."
    mc "Ah..."
    "I do the same with my right arm, on the right side of the book."
    "That way, I turn a page, and Yuri slides it under her thumb after it flips to her side."
    "But in holding it like this..."
    "We're huddled even closer together than before."
    "It's actually kind of distracting me...!"
    "It's as if I can feel the warmth of Yuri's face, and she's in the corner of my vision..."
    show y_cg1_exp1 at cgfade
    y "...Are you ready?"
    mc "Eh?"
    y "To turn the page..."
    mc "Ah...sorry!"
    mc "I think I got a bit distracted for a second..."
    "I glance over at Yuri's face again, and our eyes meet."
    "I don't know how I'll be able to keep up with her..."
    y "Ah..."
    show y_cg1_exp2 at cgfade
    y "That's okay."
    y "You're not as used to reading, right?"
    y "I don't mind being patient if it takes you a bit longer..."
    y "It's probably the least I can do..."
    y "Since you've been so patient with me..."
    mc "Y-Yeah..."
    mc "Thanks."
    hide y_cg1_exp1
    hide y_cg1_exp2
    "We continue reading."
    "Yuri no longer asks me if I'm ready to turn the page."
    "Instead, I just assume that she finishes the page before me, so I turn it by my own volition."
    "We continue the first chapter in silence."
    "Even so, turning each page almost feels like an intimate exchange..."
    "My thumb gently letting go of the page, letting it flutter over to her side as she catches it under her own thumb."
    mc "Hey, Yuri..."
    mc "This might be a silly thought, but..."
    mc "The main character kind of reminds me of you a little bit."
    show y_cg1_exp1 at cgfade
    y "You...think so?"
    y "How does she?"
    mc "Well, she's blunt.."
    mc "But she also second-guesses all of the things that she says and does."
    mc "Both of which.. Kind of do remind me of you!"
    mc "It's not like I can see into your head or anything..."
    mc "But they're kind of reminiscent of some of your mannerisms."
    y "I-I see..."
    scene bg club_day
    show yuri 2t at i11 zorder 2
    with dissolve_cg
    "Yuri remains silent for a moment."
    y "Well [player]..."
    y 1b "Speaking my mind is something that I do pride myself in..!"
    y 1h "And.. I hope you mean both of those things in a good way."
    mc "Of course I do! Sorry if you took it the wrong way.."
    mc "I guess in a way.. It's kind of cute..."
    y 3q "A-Ah--"
    y "That's nice of you to say [player].."
    show monika 4 at l31
    m "Okay, everyone!"
    show yuri 3n at h11
    y "...!"
    show monika at f31 zorder 3
    m "I think it's about time we share today's poems with each other."
    m "We might not have enough time if we wait too long."
    show monika at t31 zorder 2
    show yuri at f11 zorder 3
    y 3w "Ah..."
    "Yuri exhales, spared from finishing her thought."
    show yuri at t11 zorder 2
    show monika at f31 zorder 3
    m 1 "Is that alright, Yuri?"
    m "You look kind of down..."
    m "I'm sorry if you haven't been looking forward to this..."
    show monika at t31 zorder 2
    show yuri at f11 zorder 3
    y 3v "Ah, it's not..."
    y "...It's fine."
    show yuri at t11 zorder 2
    show monika at thide zorder 1
    hide monika
    "Yuri releases her hand from the book, causing it to close on top of my thumb."
    mc "Alright..."
    mc "I guess I'll do some more reading tonight."
    mc "Or would you prefer I only read it with you?"
    y 2f "Um...!"
    y "I...guess I don't have too much of a preference either way..."
    mc "Hmm..."
    mc "In that case, I'll read a little more tonight."
    mc "It'll be more fun to read with you after it picks up a bit, you know?"
    y 2a "That's good reasoning."
    y "In that case, feel free to finish the first two chapters in your own time."
    mc "Alright!"
    show yuri at thide zorder 1
    hide yuri
    "I stand up."
    "I make a mental note of where I left off in the book, then slip it back into my bag."
    scene bg club_day with wipeleft_scene
    play music t5 
    show monika 4b at t11 zorder 1
    m "Okay everyone!"
    m "I think it's time that we share poems."
    show monika 1c at t21 zorder 1 
    show yuri 1y6 at t22 zorder 2 
    y "I'm working with [player] first!"
    m 1i "..."
    show monika 1i at t31 zorder 1 
    show yuri 1y6 at t32 zorder 2 
    show natsuki 4b at t33 zorder 3 
    n "Hey! Why do you get to make that choice?"
    y 1r "I'm sure [player] wants to share with me first anyway. Isn't that right?"
    "I'm too intimidated by Yuri to say anything, so I just go along with it."
    mc "Yeah, I want to read with Yuri first."
    n 5f "Ugh!"
    n 5e "Whatever! You two are so peanut butter and jelly it's ridiculous."
    "Yuri scoffs at Natsuki's statement, but doesn't say anything to her."
    hide yuri with moveoutleft
    hide natsuki with moveoutright
    show monika 1q at t11 zorder 1 
    "Before we leave, Monika whispers something in my ear."
    m "Don't let yourself get intimidated by her. She's been awfully different these last few days and I don't know why."
    "That's odd.. Perhaps I'll bring it up with Yuri in the future."
    mc "Thanks Monika. I'll keep that in mind."
    m 1a "Monika smiles at me, and then we part."
    show monika at thide zorder 1
    scene bg club_day with wipeleft_scene
    show yuri 1d at t11 zorder 1 
    y "Lets see what you've written today!"
    mc "You seem excited."
    y 1e "Well, you've been really nice to me thus far. More real then anyone in the club I would say"
    y 1d "So I know you'll write the best!"
    mc "Jeez don't expect that much from me"
    mc "I've never even written a poem before."
    y 1r "Don't say that! Just let me see your poem"
    "I hand Yuri my poem, and she reads it carefully."
    y 1d "Huhu.."
    mc "What it's that bad?"
    y 1b "No! It's a really nice poem [player]!"
    y 3s "It feels so real, the poem is beauty in its most pristine form."
    mc "Isn't every poem real?"
    mc "What makes my poem different from anyone else's?"
    y "Your poem is just unique. It's made from your perspective, and experiences. Experiences no one here has, I don't think anyone else could've written a poem like this."
    mc "Woah, Yuri don't go all philosophical on me."
    mc "All I do is sit around playing video games and watching anime, and this is literally my first poem."
    mc "Unless those are.. Unique experiences.."
    y 1g "You know what, never mind."
    y 1j "Besides, I need to put you in your place a little bit."
    y "Because you're not the next Shakespeare just yet!"
    "Yuri chuckles at her joke."
    "I assume that joke means that the poem wasn't flawless, even though it really sounded like it was a few seconds ago.."
    y 1h "Well, I do see some beginning writing habits."
    y "And, having been through that myself, I kind of learned to pick up on them."
    y 1k "I think one of the most noticeable aspects of new writers is that they make their style too deliberate."
    y "In other words, they tend to pick a writing style seperate from the topic matter, and they form-fit the two together."
    y "The end result of the poem is that the style and expressiveness are ruined."
    "Wow, I didn't realize Yuri could be so constructive. Even after all that aggression yesterday, when she finds her train of thought, her demeanor changes totally."
    y 1l "Of course, it's definitely not something you can be blamed for!"
    y 1j "There's a lot of skills that go into writing a poem."
    y "Finding them and building them is difficult, and then you have to put the two together."
    y 1d "Though, I still really enjoyed your poem, while there were things that could be changed..."
    y "The poem was still unique, and very enjoyable!"
    y 1b "You can always come to me for feedback if you'd like. I'd be more then happy to help."
    y 1h "And, if you're going to ask anyone for feedback, definitely don't pick Natsuki. She's so biased towards her style, it's pathetic really."
    mc "Yuri, you shouldn't say that!"
    y 1g "Well it's true."
    "I'm pretty bewildered by Yuri's words. That was really harsh, maybe Natsuki and Yuri don't have the best relationship? I decide to attempt to divert the conversation."
    mc "Do you mind if I read your poem now?"
    y 1d "Certainly! I'd love to share my thought process behind it."
    "Yuri smiles dreamily, as if it's a rare opportunity for her. That's kind've ironic.. considering we are in a literature club."
    call showpoem (poem_y1) from _call_showpoem
    y 1g "That took you a while to read.."
    y 4b "Is my handwriting that bad?"
    mc "What? No! I wasn't thinking that at all!"
    mc "I just don't read script very often."
    mc "I actually think your handwriting is very pretty."
    y 4a "Oh?"
    y 1b "Well that's a relief."
    mc "Also I really liked the poem!"
    mc "Thought it was short, it was really descriptive!"
    y 1h "I hope it wasn't too short."
    y "I usually write poems longer then this."
    mc "Oh not at all!"
    y 1b "I'm really glad that you liked it!"
    y "If I'm honest, I wanted to write something a little bit more digestible."
    y "Since, it is our first time sharing."
    mc "Are you into ghosts Yuri?"
    y 1d "Huhu."
    y 1b "Actually, [player], this poem isn't about a ghost at all."
    mc "Really?"
    mc "Wow, then I must have totally missed the point."
    y 1j "Well, I suppose you did only glance over it."
    y 3k "But remember, poets often express their own thoughts, feelings, and experiences in their work."
    y "Usually, it does more then tell a simple story, or paint a picture."
    y 1l "In this poem, perhaps the subject of the poem is only being symbolically compared to a ghost."
    y "Lingering in her last place of comfort, in her reality. Unable to let go of the past."
    y "And soon to be met with nothing..."
    mc "That's a lot more solemn putting it that way."
    mc "I never even thought of that."
    mc "That's very impressive, Yuri."
    y 1b "Oh, it's nothing really."
    y "Yours was very impressive too!"
    mc "Nah, I could learn a thing or two from you."
    y 1d "That you can, huhu."
    y "I really enjoyed this."
    y 1j "You should always show me your poem first."
    y "Just so I can give you constructive criticism."
    y 1g "After all, the others are very biased to their styles."
    mc "I'll keep that in mind..."
    hide yuri with moveoutleft
    scene bg club_day with wipeleft_scene
    "After talking to Yuri, I see Monika is alone at her desk, so I decide to converse with her next."
    show monika 4b at t11 zorder 1 
    m "Hi, [player]!"
    m 1a "Enjoying your time so far?"
    mc "Yeah, I would say so!"
    m 1b "That's great!"
    "Monika's expression quickly changes."
    m 1h "Listen [player] we need to talk about something."
    mc "Sure, shoot."
    "I'm have a feeling this is about Yuri."
    m 1i "It's about Yuri."
    "Knew it."
    m 1g "Look, I've never seen Yuri act as aggressive as she is right now."
    m 1o "..."
    m "It just worries me, because I am the club president, and I need to look after my members"
    m 1e "If you could please talk to her about it, I would greatly appreciate it."
    m 1o "I would myself, but she lashes out at everyone.. Except you."
    "I guess I didn't take into account everyone else's perspectives.. Yuri has been pretty aggressive, but I just thought she'd always been like that."
    mc "Sorry, I just didn't realize that was unusual."
    mc "I just thought that's how she was."
    m 2p "No, she's never acted like this."
    m 1c "Well, now we've got that out of the way.."
    m 1b "Why don't you show me your poem?"
    mc "Sure thing! Here you go."
    m 1j "Mmm.."
    m 1k "It's a nice poem [player]!"
    m 1n "Unsurprisingly, it does remind me of Yuri's style of poems."
    m 1k "She must be rubbing off on you!"
    mc "I guess you could say that.."
    m 1b "Yuri tends to use a lot more metaphors and sophisticated words."
    m 1d "Do you enjoy that writing style, [player]?"
    mc "I think it's a really good way of conveying things."
    mc "It helps tackle deep topics, and I really love all the descriptive images that come to your mind."
    m 1b "It certainly is an effective writing style!"
    m "But don't be afraid to experiment!"
    m 1a "Do you want to read my poem now?"
    mc "Sure thing!"
    call showpoem (poem_m1) from _call_showpoem_1
    m 1b "So, what do you think?"
    mc "I love the poem Monika!"
    mc "It's very abstract, and freeform, if that's what you call it."
    m "Yeah that style has gotten pretty popular nowadays."
    mc "Sorry, I'm not really the best for poem feedback."
    m 1a "Well, you are just a beginner."
    m 1k "If you ever need any feedback, don't be afraid to ask!"
    mc "Thank you Monika, I appreciate that."
    m 4k "Here's Monika's writing tip of the day!"
    m "Sometimes, when writing a poem, or story, your brain gets too fixated on a specific point."
    m "If you try so hard to make it perfect, you'll never make any progress!"
    m "Just force yourself to get something down on the paper, and tidy it up later!"
    m 1a "Another way to think about it is this:"
    m 4b "If you keep your pen in the same spot for too long, you'll just get a big dark puddle of ink."
    m "So, just move your hand and go with the flow!"
    m "That's my advice for today! Thanks for listening."
    mc "Very informative, thank you Monika!"
    m "Don't mention it!"
    show monika at thide zorder 1
    hide monika 
    "After talking to Monika, I decide to talk to Natsuki, seeing as she's finished sharing with Sayori."
    scene bg club_day with wipeleft_scene
    show natsuki 5b at t11 zorder 1
    n "Oh boy, it's [player]!"
    n 5t "Hopefully I can finally show you a good writing style.."
    mc "What, are Yuri's and Monika's writing styles not good?"
    n 5w "Where'd you get that?"
    n 1t "I'm just saying that my writing style is superior."
    n "But first, let's see your poem."
    mc "Okay then Natsuki."
    "I show my poem to Natsuki, and her expression changes."
    n 5w "Are you even taking this seriously?"
    mc "Of course I am! I tried really hard on this poem."
    n 1q "Well you need to try harder."
    n "This poem is just bad."
    "Yuri had a point, it does seem like she's really biased.."
    mc "Really? I thought it was okay.."
    n 1t "Well, you need to get your head out of the gutter."
    n "Let me show you how a real pro writes!"
    "Natsuki excitedly gives me her poem."
    call showpoem (poem_n1) from _call_showpoem_2
    n "Pretty good right?"
    mc "Wow, I actually really like the poem!"
    n 1d "Really?"
    mc "Yeah, I like how you made the rhyme fall flat at the end."
    mc "It really brings out the meaning of the poem."
    n 1c "I didn't expect you to notice that."
    n 1d "But yeah! This poem is about the feeling of giving up."
    n "I doubt I need to explain that."
    n 1t "Unless.. You're really that dense."
    mc "Oh comeon, give me some credit!"
    n 4e "Not with the poem you just showed me!"
    n "You don't deserve any credit just yet!"
    n 1t "You have to earn it."
    mc "Okay then Natsuki, I'll try then."
    n 1e "Good! You better bring a better poem tomorrow."
    show natsuki at thide zorder 1 
    hide natsuki
    "After talking to Natsuki, I finally make my way to Sayori."
    scene bg club_day with wipeleft_scene
    show sayori 1a at t11 zorder 1 
    s "Hi~ [player]!"
    mc "Hi Sayori! What's going on?"
    s 1x "What do you think is going on silly~"
    s 1a "Obviously we are sharing poems!"
    mc "Fair point."
    s "Let me see your poem! I'm sure it'll be great!"
    mc "Natsuki didn't seem to like it, so we'll see."
    s 1d "I already told you~ she can be a bit moody at times."
    mc "I guess you got a point there."
    s 1a "Anyway lets see the poem [player]!"
    "I hand my poem to Sayori."
    s 1d "This is a nice poem [player]!"
    s 1l "Did you write this for someone in specific?"
    mc "No.. I just kind've picked a style and went with it."
    "Real smooth.. [player]."
    "I just can't risk anyone thinking I'm interested in Yuri."
    s 1c "Really? It reminds me a lot of Yuri's poems."
    s 1a "Perhaps you have more in common with her then you realize."
    mc "Perhaps.."
    s 4x "Wanna see my poem now?"
    mc "Of course!"
    call showpoem (poem_s1) from _call_showpoem_3
    mc "Sayori.. Did you perhaps write this poem this morning?"
    s 4m "What? Of course not!"
    s 5a "I wouldn't write it this morning..."
    mc "Sayori, it literally says I want breakfast at the end."
    s 5b "Alright maybe you caught me..."
    mc "But still, it's a really cheery poem."
    mc "I really enjoyed it! It just seems like something you would write.."
    s 1a "Of course! I love writing about happy things."
    s 1c "But a raincloud or two never hurts every so often!"
    mc "Wow, I wouldn't expect that from you Sayori."
    s 1h "Well.. Things can't always be happy."
    s 1r "Even though I want them to be!"
    mc "I wish they always were too."
    show sayori at thide zorder 1 
    hide sayori
    "After talking to Sayori, my eye catches Yuri and Natsuki sharing their poems.."
    show yuri 1i at t21 zorder 1 
    show natsuki 1g at t22 zorder 2 
    "They gingerly exchange sheets of paper, sharing their respective poems."
    "As they read in tandem, I watch each of their expressions change."
    "Natsuki's eyebrows furrow in frustration."
    "Meanwhile, Yuri has a kind of smirk I can't quite make out."
    n 1q "{i}What's with this language??{/i}"
    y 1f "Huh?"
    y "What'd you say Natsuki?"
    n 1c "Nothing."
    "Natsuki dismissively returns the poem to the desk with one hand."
    n "I guess you could say it's fancy."
    y 1i "Thanks. Yours is.. cute."
    play music t7a
    n 2h "Cute?"
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How could that be cute?"
    y 1h "I knew that."
    y "I was just talking about the writing."
    y "I was just trying to say something nice."
    n "Eh?"
    n 5w "You mean you have to try that hard to say something nice?"
    n "Thanks, but it didn't come out nice at all!"
    stop music fadeout 1.0
    "Yuri's expression fades from relatively neutral to an expression of complete rage."
    play music t7g
    y 1r "{b}Oh shut the fuck up Natsuki!{/b}"
    y "{b}All you ever do is complain and bitch, you gave me a very similar compliment, and I'm the bad one here?{/b}"
    show natsuki 1p at h22 zorder 2 
    "Natsuki clearly taken aback by Yuri's words, then fires back, in an even louder tone."
    n 5p "{b}Well maybe if you tried being a little fucking nicer to the club, I would be nicer to you.{/b}"
    n "{b}Have you even tried looking back on your own behavior?"
    n "{b}Your fucking awful snarky remark on Monika needing to try harder? Yeah I heard that!{/b}"
    n "{b}You also yelled at me too before for just making a comment about [player]!{/b}"
    n "{b}When it was just a joke!{/b}"
    "Yuri's expression becomes more extreme."
    y 1y7 "{b}We both know thats not true!{/b}"
    y 1y4 "{b}You're just saying that to make yourself feel better."
    "I need to do something about this soon.. I look over to Sayori."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1 
    hide yuri 
    hide natsuki 
    show sayori 1v at t11 zorder 1 
    "Sayori is practically crying.. I think she's too inconsolable to do anything about this."
    show sayori at thide zorder 1
    hide sayori 
    show monika 1h at t11 zorder 1 
    "I then look over to Monika, and she looks back at me."
    "We both look at each other, I need to decide if me or Monika should take care of this."
    stop music fadeout 2 
    menu:
        "I will take care of it.":
            $decision_argument = 1
        "Let Monika take care of it.":
            $decision_argument = 2
if decision_argument == 1:
    $ decisions_ending += 1
    "I decide that it would be best if I take care of it. After all, I do know Yuri the best."
    mc "I'll take care of it Monika."
    m "Don't mess this up.."
    show monika at thide zorder 1 
    hide monika
    "I look back towards Natsuki and Yuri. Both appear to still be pissed, but just as Natsuki is about to formulate a response.."
    show natsuki 5p at t22 zorder 2
    show yuri 1y4 at t21 zorder 1 
    "I cry in my loudest possible voice..."
    mc "{b}ENOUGH GUYS!{/b}"
    #End demo here possibly?
    "Both girls turn to look at me, and both of their expressions break."
    show natsuki 1n at h22 zorder 1 
    show yuri 1o at h21 zorder 1
    "..."
    "Silence fills the room."
    "Then Yuri and Natsuki both leave the room, still in silence."
    y "..."
    hide yuri with moveoutleft
    n "..."
    hide natsuki with moveoutright
    play music t10
    "While the argument has dissolved, I don't know if that'll last. Especially after an argument like that.."
    "I decide that I should converse with Sayori and Monika, and then quickly go after Yuri."
    show sayori 1v at t21 zorder 1 
    show monika 1o at t22 zorder 2
    mc "I think I'm going to go talk to Yuri."
    m 1p "That's probably for the best, I doubt she'll want to talk to anyone else anyway."
    m "Me and Sayori will go talk to Natsuki.."
    mc "Okay, sounds like a plan."
    show sayori at thide zorder 1 
    show monika a thide zorder 2 
    hide sayori
    hide monika 
    scene corridor with wipeleft_scene
    #probably put cg here too? Not 100% sure yet
    "I make my way into the hallway, and search for Yuri."
    show yuri 1w at t11 zorder 1 
    "Then, I find her, knees on the ground, with labored breathing."
    "Is she having a panic attack?"
    "I rush to her side."
    "There's a knife on the floor next to her, why does she have that?"
    mc "Yuri..?"
    stop music fadeout 0.5
    y "...help me."
    play music uyuri_panic
    "I immediately hug Yuri, and try my best to help her calm down.."
    "From this close, the breathing is much more apparent. Her heartbeat even becomes audible, it's racing."
    #put cg here when ready
    mc "Yuri.. is everything okay?"
    "Yuri shakes her head."
    mc "Look, just try to relax. You're in a safe place now."
    mc "Just breathe in, and out."
    "We stay like that for a while."
    "Yuri takes deep breathes, though unsteady and shakey."
    "We continue like that, in and out."
    "It takes a while, but Yuri's breathes start stablizing."
    stop music fadeout 1.0
    play music yurirecover
    "I start to get the sense that Yuri is recovering."
    y "[player]..?"
    mc "Yes?"
    y "The last few days have been really hard on me.."
    y "It's been really difficult.."
    mc "Yuri, I'm always available if you need someone to talk to."
    mc "We can all have dark thoughts sometimes, and sometimes we need others to help us.."
    mc "But you shouldn't take your anger out on the club..."
    y "..."
    y "I want you to meet me here tomorrow."
    y "It's important.."
    mc "Will you try to do better for the club?"
    y "...just meet me here tomorrow."
    "Why won't Yuri answer my question?"
    "I would push on, but she seems like she's in a dark place, so I let it go."
    mc "I'll be here tomorrow. I'm always here to help you Yuri."
    y "Thanks [player]..."
    "Me and Yuri both get up."
    scene corridor with wipeleft_scene
    show yuri 1q at t11 zorder 1  
    y "Well I'm going to go home now."
    mc "Okay, I need to finish up with some club stuff so I'll be heading back in there."
    y "Okay, see you soon [player]."
    hide yuri with moveoutright
    "Yuri leaves to go home, and I head back into the clubroom."
    jump end_of_day1
if decision_argument == 2:
    $ decisions_ending -= 1
    "I give Monika a nod to signal to her to stop the argument."
    "She understands, and goes to interject in the argument."
    show monika at thide zorder 1 
    hide monika 
    scene bg club_day with wipeleft_scene
    show monika 1r at t31 zorder 1 
    show yuri 1y4 at t32 zorder 1 
    show natsuki 5p at t33 zorder 1 
    "Just as Natsuki is about to fire back Monika screams."
    m 5b "{b}ENOUGH!{/b}"
    #Demo could end here?
    show natsuki 1i at s33 zorder 1
    show yuri 1y7 at t32 zorder 1 
    y "..."
    "Silence fills the room for a few seconds but Yuri then fires back."
    y 1y4 "{b}SHUT UP MONIKA!{/b}"
    y "{b}YOU'RE A SHIT PRESIDENT. GO FUCK YOURSELF.{/b}"
    show monika 1o at t31 zorder 1 
    "Nobody in the room expected that response."
    "I decide to interject and help Monika."
    mc "Yuri what the hell? Are you hearing yourself right now? You need to calm down."
    show yuri 1o at s32  zorder 1 
    y 1r "Fuck this."
    hide yuri with moveoutleft
    show monika at thide 
    show natsuki at thide 
    scene bg club_day with wipeleft_scene
    show natsuki 1n at s22
    show monika 1o at s21
    stop music fadeout 2.0
    "For the most part.. Silence fills the air once again. The only thing that can be heard is Sayori's sobs."
    "And though it is silent again, the air feels much heavier, I decide to break the silence."
    mc "I'll go reason with Yuri..."
    "The girls don't even look at me, they just silently nod."
    scene bg corridor with wipeleft_scene
    "I make my way into the hallway, and search for Yuri."
    play music uyuri_panic
    show yuri 1w at d11 zorder 1 
    "I find her, knees on the ground. I can hear her labored breathing, even from here."
    "Is she having a panic attack?"
    "I rush to her side."
    mc "Yuri?"
    show yuri 1p at h11 zorder 1 
    y "[player]?"
    show yuri 4e at s11 zorder 1 
    y "I.. thought.. you.."
    "I pull Yuri into a tight embrace."
    #cg here
    "I can feel Yuri's heartbeat when I embrace her. It's kind've scary how fast and loud it is."
    mc "Don't push yourself."
    mc "Just breathe in and out."
    "We sit there for a while until Yuri's heartbeat and breathing start slowing down."
    stop music fadeout 1.0
    play music yurirecover
    y "I.. I thought you hated me."
    mc "I don't hate you."
    mc "You were just getting too aggressive."
    y "You.. don't understand."
    y "Come here tomorrow [player]. Please?"
    mc "If you promise to make up to the club."
    y "Please.. just come here tomorrow."
    "I would push further, but she seems really hurt right now."
    "I don't know why she won't agree, but it's probably better if I dont."
    mc "Ok.. I'll come here tomorrow."
    y "Okay.. I'll see you tomorrow then."
    "I decide to head back into the clubroom to check on the rest of the club members."
    stop music fadeout 2.0
    jump end_of_day2 

    
    
    






    
    



    
    

    




    







    





















    



