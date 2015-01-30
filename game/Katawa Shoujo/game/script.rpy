image bg dorm = "school_dormhisao.jpg" ##Inicializan todos los fondos
image bg courtyard = "school_courtyard.jpg"
image bg restaurant = "city_restaurant.jpg"
image bg clubentrance = "city_clubint.jpg"
image bg clubpool = "city_clubpool.jpg"
image bg schoolentrance = "school_dormext.jpg"
image bg classroom = "school_scienceroom.jpg"
image bg alley = "city_alley.jpg"
image bg black = "black.png"
image bg hallway = "school_hallway2.jpg"
image bg lillynormal = "Lilly_14_1.jpg"
image bg lillyworried = "Lilly_14_2.jpg"
image bg lillyending = "Lilly_2_2.jpg"
image bg lillyhouse = "shizu_houseext_ni.jpg"
image bg busride = "busride_ni.jpg"
image bg empty = "Hanako_8_1.jpg"
image bg hanakolooking = "Hanako_7_1.jpg"
image bg hanakohappy = "Hanako_7_4.jpg"
image bg hanakoworry = "Hanako_7_3.jpg"
image bg hanakofocused = "Hanako_7_2.jpg"

image lilly normal = "lilly_basic_smile.png" ##Inicializan todos los personajes
image lilly please = "lilly_basic_oops.png"
image lilly pouting = "lilly_basic_pout.png"
image lilly cheerful = "lilly_behind_cheerful.png"
image lilly outnormal = "lilly_basic_smile_che_close.png"
image lilly outcheerful = "lilly_basic_satisfied_che_close.png"
image lilly outworry = "lilly_basic_oops_che_close.png"
image lilly backsurprise = "lilly_back_surprise.png"
image lilly backlisten = "lilly_back_listen.png"

image hanako normal = "hanako_basic_bashful.png"
image hanako worry = "hanako_basic_worry.png"
image hanako outnormal = "hanako_basic_bashful_cas.png"
image hanako outhappy = "hanako_emb_emb_cas.png"
image hanako outsad = "hanako_emb_sad_cas.png"

define m = Character('Me', color="#00AA00") ##El color de los nombres de los personajes
define h = Character('Hanako', color="#503070")
define l = Character('Lilly', color="#A37A00")

init: ##Definir donde sera la posicion "left", "right" y "center" para que no use las que estan de default
    $ left = Position(xpos=0.185, xanchor='left')  
    $ center = Position(xpos=0.5, xanchor='center')
    $ right = Position(xpos=0.825, xanchor='right')

label start: ##Empieza igual siempre
    scene bg black
    with fade
    play music "business_ring_03.mp3"
    "Ughh...."
    "What... time is it anyways?"
    scene bg dorm
    with dissolve
    m "FUCK I'M LATE."
    m "Damn alarm didn't work again."
    "The phone? It's probably Hanako again, what could she want?"


menu : ##Primera decicion.
    "To my surprise it's Lilly calling. Should I answer the phone?"
    "Answer her, I'm late already." :
        jump answer

    "There's no time! I can still make it!" :
        jump classroom


label answer: ##Si contesta el telefono

    "Guess I will answer it since I'm late already."
    stop music
    play music "Afternoon.mp3"
    m "Hey Lilly what's up?"
    l "Hello Hisao, how are you?"
    m "I'm fine here, what about you? Shouldn't you be in class right now?"
    l "Haha, well yeah, but I wondered why you haven't arrived so I left to ask you."
    m "That's nice of you. I'm already heading there right now, my alarm didn't work for some reason."
    l "Alright, I will be waiting here for you."
    m "See you there."
    stop music
    scene bg alley
    with fade
    play music "Background Music/Standing_Tall.mp3"
    "Hmmm, Lilly. Why did she call me?"
    "Gahhh I shouldn't think about it too much, she was only bored most likely."
    "..."
    "...{w=0.5} I really can't stop thinking about her."
    scene bg hallway
    with dissolve
    "I'm here."
    show lilly normal
    l "You are late Hisao."
    m "I know, I know. But I'm here now right?"
    show lilly cheerful
    l "I guess so. Let's go in and sit together."
    m "Alright."
    stop music
    scene bg classroom
    with fade
    play music "Background Music/The_Student_Council.mp3"
    show lilly normal at left
    show hanako normal at right
    h "Hey Hisao, Lilly."
    l "Good morning Hanako."
    m "'Morning."
    show lilly pouting

menu: ##Puede mentir o decir la verdad
    h "Say Hisao, want to sit together?"
    "Sorry, I'm sitting with Lilly today." :
     jump honest

    "Sure." :
     jump bastard

label honest: ##Si dice la verdad
    m "Sorry Hanako, Lilly asked me to sit with her today."
    
    show hanako worry at right
    show lilly cheerful at left

    h "Oh, alright... See you later then"

    hide hanako

    m "She seemed sad..."
    l "Well, we can't worry about that now, we are already behind in classwork!"

    hide lilly

    "We start working on the classwork and we barely finished when the alarm sounded."

    show lilly normal
    l "Whoo, glad we could finish that."
    m "Yeah, we barely made it back there."
    l "Say Hisao...{w=0.5}\nDo you want to have dinner today?"
    "What. \n{w=0.5}Did...{w=0.1} Did she just ask me out?"
    "I must be the luckiest man alive, of course I won't deny her."
    show lilly cheerful
    m "Sure, I would love to."
    hide lilly
    stop music
    scene bg restaurant
    with fade
    play music "Background Music/Nocturne.mp3"
    "Guess it's actually happening... YES."
    "Is she here already? I can't see her."
    "Was I stood up? \nWas this all just a joke?"
    "What if..."
    l "Hey Hisao!"
    show lilly outnormal
    with dissolve
    m "Nice to see you Lilly, I was beggining to worry you wouldn't be showing up for some reason."
    show lilly outworry
    l "Oh no Hisao, I wouldn't do that to you. \nI was looking forward to this moment."
    show lilly outcheerful
    "What."
    m "Right, so was I. Guess I'm just a little paranoid."
    l "Well, let's get down to it then."
    hide lilly
    scene bg lillynormal
    with fade
    "She looks so beautiful just patiently waiting for her food."
    "Makes me wonder why she would invite someone like me to dinner."
    play music "Background Music/High_Tension.mp3"
    "This must be some kind of bad prank."
    "Yeah it's probably that, we never really talked in school so this is quite sudden, her calling me in the morning..."
    "Wait."
    "How did she get my number?" 
    "Is she some kind of stalker?"
    "Am I in for some trouble?"
    "Should I run away?"
    "There's no way this is just a simple date, it's too good for that."
    "What is the trick? Is there a hidden camera? A microphone under the table? \nWHAT IS IT!?"
    "...{w=0.3}No, it can't be. Maybe she simply didn't have any plans for today so she invited me."
    "But..."
    l "Hisao?"
    m "Mhm?"
    l "Are you feeling fine?"
    "She could probably tell I was freaking out thinking she's a stalker."
    m "Yeah, don't worry. Everything is good."

    
menu: ##Correr o quedarse
    "What should I do? I'm a bit scared she's stalker but I also really want to have a date with her."
    "Continue with the date.":
        jump goodendinglilly

    "RUN AWAY!":
        jump badendinglilly


label bastard: ##Si miente a la hora de sentarse con Lilly
    "I said I will sit with Lilly but I honestly like Hanako a bit more."
    m "Sure."
    show lilly please at left
    show hanako normal at right
    l "Oh...{w=0.5} Okay Hisao...{w=0.5} See you later then..."
    hide lilly
    "Wow, she seemed really sad. Maybe I should sit with her as I said."
    m "I'm sorry Hanako, I said I was sitting with Lilly before."
    show hanako worry
    h "Aw, that's fine I guess... See you later Hisao."
    m "I'm sorry."
    hide hanako 
    with fade
    "Well, that's two girls I have let down in a minute."
    "I should probably tell Lilly I will be sitting with her after all."
    m "Hey Lilly, I can sit with you after all!"
    show lilly backsurprise
    l "Huh? What about Hanako?"
    m "I told her \"Sorry but I'm sitting with Lilly today.\""
    show lilly backlisten
    l "Hisao! You can't do that!"
    "Aaand she's mad."
    l "You can't just lie to a girl and then come up saying everything is alright."
    l "I won't be sitting with you today."
    m "But... but."
    l "But nothing, you should not lie Hisao. Goodbye."
    hide lilly
    "Well, that didn't work out."
    "I wonder if Hanako would still want to sit with me. Where is she anyways?"
    scene bg empty
    with fade
    "Huh? She's not in her seat."
    "Guess she wasn't feeling too well or something."
    "It's just me today then..."
    "...{w=0.8}That's sad."
    play music "Background Music/To_Become_One.mp3"
    scene bg black
    with dissolve
    "Well Lilly is mad at me and Hanako is missing. This couldn't get much worse."
    "Guess I'm just destined to be alone..."
    "Yeah, someone like me couldn't be with a pretty girl like Hanako or Lilly."
    "I should stop trying."
    "...{w=1.0}That's probably for the best."
    "{w=1.2}.:. Bad Ending"
    return
    


label goodendinglilly: ##Si se queda en la cita con Lilly
    stop music
    "Yeah that's ridiculous, there's no way Lilly is a stalker."
    play music "Background Music/Lullaby_of_Open_Eyes.mp3"
    m "What about you Lilly, everything good? You seem a bit blushed."
    scene bg lillyworried
    l "Haha yeah, I'm just really happy."
    m "Something good happened at school?"
    l "Well, I'm having a date with the boy I like. So that's something."
    "What.\nShe likes me? I would have never guessed that..."
    m "Oh yeah..."
    scene bg lillynormal
    "My heart is pumping way too fast."
    l "Hisao?"
    "Oh god, is this real life?"
    m "Yeah?"
    "Here it comes."
    l "Would you like to be my boyfriend?"
    "Aaaaand I'm dead. I must be, why would someone as beautiful as Lilly ever want to date someone like me?\nI don't know, and probably never will but for now, I want to be with her."
    m "It would be my pleasure."
    scene bg lillyworried
    l "I'm glad."
    "If this is being dead I don't want to be alive."
    scene bg lillynormal
    "...{w=0.5}Guess we are dating now."
    "My girlfriend is so pretty."
    "Never thought I would say that someday. I'm really happy."
    scene bg black
    with dissolve
    "And so the night went on and we finished dinner and decided to head home."
    "We are at her house now, I should probably say goodbye."
    scene bg lillyhouse
    with dissolve
    show lilly outnormal
    with dissolve
    l "This is my house."
    m "Guess this is goodnight."
    l "Guess it is."
    scene bg black
    with fade
    "I start turning around to go back but something stop me.\nIt's Lilly."
    scene bg lillyending
    with dissolve
    m "Lilly?"
    l "Good night, Hisao."
    "This made me feel strangely happy for some reason."
    m "Good night, Lilly."
    scene bg black
    with fade
    "Guess I have a girlfriend now, and a cute one at that."
    "I'm really happy."

    "{w=0.8}.:. Good Ending"
    return

label badendinglilly: ##Si se escapa de la cita con Lilly
    "I don't really know if she's a stalker or not. But I sure as hell won't wait to find out."
    m "I..."
    scene bg lillyworried
    l "Hisao?"
    m "I...{w=0.2} {i}Ihavetogonow!{/i}"
    scene bg black
    with fade
    "Huff huff...{w=0.5}I don't even know if she said something before I bolted out of there."
    "I should probably head back home."
    scene bg busride
    with fade
    "That was really weird... There's just no way I'm going to believe her when I don't even know how she got my number."
    "Of course she was a stalker, she must have been."
    "I refuse to believe anything else...{w=0.5} It would feel too bad otherwise."
    "Maybe I messed up, maybe I didn't. I will probably never know for sure."
    scene bg black
    with fade
    "{i}I wish I was right...{/i}{w=1.0}"
    
    "{w=1.0}.:. Bad Ending"
    return

label classroom: ##Si no contesta su celular en la casa

    "I don't have time to answer it. Better head to class first."
    stop music
    scene bg alley
    with fade
    play music "Background Music/Standing_Tall.mp3"
    "I'm close to school now. Still I can't help but wonder why Lilly called me."
    "Probably Hanako asked her to call me. After all, I always sit with Hanako in class."
    "Yeah, it's probably that."
    scene bg hallway
    with fade
    "Oh, is that Hanako?"
    m "Hey Hanako."
    show hanako normal
    h "Hello Hisao, you are late."
    m "Yeah yeah, my alarm broke down again."
    h "Well that's no good. Anyways, want to sit together again?"
    m "Sure."
    stop music
    scene bg classroom
    with fade
    play music "Background Music/The_Student_Council.mp3"
    show lilly please at left
    show hanako normal at right
    l "Hisao you are alright! I was worried you didn't answer my call."
    m "Yeah sorry about that, my alarm broke and I just hurried off here."
    show lilly normal
    l "Oh, at least you are here then."
    l "Say... Do you want to sit together?"
    show hanako worry at right
    
menu: ##Decide si miente o no
    "Well, I already told Hanako I would be sitting with her..."
    "Yeah, sure!":
        jump bastard2
          
    "Sorry, I already promised Hanako to sit with her.":
        jump honest2


label bastard2: ##Si miente despues de no contestar el telefono
    "Well, Lilly is prettier than Hanako. I guess it wouldn't hurt."
    m "Yeah, sure!"
    show lilly cheerful
    l "Yay, let's go then!"
    hide lilly
    h "Oh... Okay Hisao, see you later then...{w=0.2}"
    hide hanako
    "Wow, Hanako looked pretty bad back there. I guess it was a bad idea to break my promise."
    "I better tell Lilly I can't sit with her."
    show lilly backlisten
    m "Hey Lilly wait up."
    l "Yes Hisao?"
    m "I'm sorry but I can't sit with you, I had already promised Hanako I would sit with her."
    show lilly backsurprise
    l "What? Hisao you can't do that. I can't believe you lied to me and Hanako."
    m "But..."
    l "But nothing Hisao, go apologize to Hanako right now and don't talk to me."
    hide lilly
    "Ouch, guess she is pretty mad at me for lying."
    "I better apologize to Hanako then."
    "Huh?"
    scene bg empty
    with fade
    "Where did she go?"
    "Was she that mad at me?" 
    "It's just me today then..."
    "...{w=0.8}That's sad."
    play music "Background Music/To_Become_One.mp3"
    scene bg black
    with dissolve
    "Well Lilly is mad at me and Hanako is missing. This couldn't get much worse."
    "Guess I'm just destined to be alone..."
    "Yeah, someone like me couldn't be with a pretty girl like Hanako or Lilly."
    "I should stop trying."
    "...{w=1.0}That's probably for the best."
    "{w=1.2}.:. Bad Ending"
    return

label honest2: ##Si dice la verdad despues de no contestar el telefono
    "I better not lie to Hanako."
    m "Sorry, I already promised Hanako to sit with her."
    show lilly pouting at left
    show hanako normal at right
    l "Aww, okay. See you later then."
    hide lilly
    m "That could've been worse."
    show hanako normal
    h "Guess so. Well, let's get to work, we are late already!"
    m "Sure thing."
    hide hanako
    "We start furiously working on the classwork and we barely finish it by the time the bell rings."
    show hanako normal
    m "Woo, glad we finished that."
    h "Yeah, barely made it."
    h "Say... do you have any plans for today?"
    m "None at all. Anything in mind?"
    h "I wanted to go play pool if you don't mind."
    m "Sure let's go."
    hide hanako
    scene bg dorm
    with fade
    play music "Background Music/Air_Guitar.mp3"
    "I better start getting ready to go out."
    "Though I can't help but wonder why she would invite me out of nowhere."
    "Could it be she likes me?"
    "...{w=0.5}Nah that can't be."
    "...{w=0.5}Or can it?"
    scene bg black
    with fade
    "I start heading to the club and quickly arrive there."
    stop music
    scene bg clubentrance
    with fade
    play music "Background Music/Nocturne.mp3"
    "Well I'm here, now where is Hanako?"
    h "Hey Hisao!"
    show hanako outnormal
    m "Hey Hanako, you look nice."
    show hanako outhappy
    h "Haha, thanks. You don't look too shabby yourself."
    m "Well then, let's get to playing."
    h "Let's."
    hide hanako
    stop music
    scene bg hanakohappy
    with fade
    play music "Background Music/Innocence.mp3"
    "We start playing and she is looking very happy."
    "As always I try not to notice that scar in her face though sometimes I fail."
    "She looks very pretty tonight."
    scene bg hanakofocused
    "Also kinda funny when she is so focused."
    "I wonder if she likes me."
    scene bg hanakolooking
    h "Say Hisao..."
    m "Mmm?"
    h "What do you think about us?"
    "Oh wow, I wasn't expecting that."
    m "We are very good friends, right?"
    scene bg hanakoworry
    h "Right, friends."
    "She looks kinda sad about that."


menu: ##Confesarse a Hanako o no
    "Maybe I should make my move."
    "Tell her I like her.":
        jump love

    "Remain friends, can't risk it.":
        jump friends

label love: ##Si se confiesa
    "I better tell her now. Won't get many chances like this."
    stop music
    scene bg clubpool
    show hanako outsad
    play music "Background Music/Aria_de_l'Etoile.mp3"
    m "Hanako..."
    h "Hisao?"
    m "I...{w=0.5}I actually really like you."
    "And I said it. Now we wait."
    show hanako outhappy
    h "Hisao..."
    "She seems relieved."
    h "I also like you a lot."
    m "I'm glad."
    h "Well, I guess we are dating now."
    m "Guess we are."
    h "I'm so happy."
    scene bg black
    with fade
    hide hanako
    "I'm dating Hanako now. Life couldn't be better."
    "I want to see her again."
    "Guess I have all the time in the world."
    "...{w=0.5}I'm happy."
    "{w=0.8}.:. Good Ending"
    return

label friends: ##Si se caga y no confiesa
    stop music
    play music "Background Music/Caged_Heart.mp3"
    "I can't risk it. We can't be more than friends."
    "She wouldn't like me."
    scene bg hanakofocused
    "Though she did invite me here..."
    "Gahhh, I can't decide."
    "...{w=0.5}I better play it safe, can't risk losing her."
    "Yeah, we are just friends."
    scene bg black
    with fade
    "The rest of the night went on normally. Nothing eventful happened and we both went back home."
    "At least we are friends right?"
    "...{w=0.5}Yeah, it's probably better than nothing."
    "...{w=0.8}I should've asked her."
    "{w=0.8}.:. Bad Ending"
    return