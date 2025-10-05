# Declare characters
define b = Character("Blorgo", color="#c8ffc8")
define m = Character("Miss Maisie", color="#60aae7")
define t = Character("Trafalgar", color="#0d4b0d")
define k = Character("Kaylan", color="#34337e")
define me = Character("Melina", color="#e7a760")
define ka = Character("Katie", color="#ff8cc8")
define l = Character("Lloyd", color="#8cf0ff")
define s = Character("Suzy", color="#ffdd60")
define la = Character("Landon", color="#a6ff70")
define st = Character("Students", color="#aaaaaa")
define sena = Character("Commander Sena Azor", color="#ffd966")



# Start of the game
label start:

    ### SCENE 1 ###
    play music "audio/bgaud.ogg" loop
    
    scene bg lot
    with fade

    "In the year 2189 on Mars, some students are getting ready for a field trip with their teacher."

    show blorgo yawn
    with dissolve
    b "Where are we going today?"
    hide blorgo yawn
    with dissolve

    show trafalgar excited
    with dissolve
    t "Miss Maisie said we’re going to the Sun!!"
    hide trafalgar excited 
    with dissolve

    show kaylan smile
    with dissolve
    k "Isn’t the Sun hot? My mommy gave me a camera so I could take pictures!"
    hide kaylan smile
    with dissolve

    show kaylan camera
    with dissolve
    k "Look at it!"
    hide kaylan camera
    with dissolve

    show blorgo reach
    with dissolve
    b "Ooooh, that looks super cool! Lemme see!"
    hide blorgo reach
    with dissolve

    show maisie stern
    with dissolve
    m "Boys!! Hurry to the bus immediately."
    hide maisie stern
    with dissolve

    jump scene2


label scene2:
    ### SCENE 2 ###
    scene bg bus
    with fade

    show maisie normal
    with dissolve
    m "Now, everyone. Please put on your seatbelts, and if you need help, raise your hand."
    hide maisie normal
    with dissolve

    "Several students raise their hands. Miss Maisie moves to help them."
    

    show trafalgar excited
    with dissolve
    t "Miss Maisie, Blorgo can’t put on his seatbelt!"
    hide trafalgar excited
    with dissolve

    show blorgo normal
    with dissolve
    b "Miss Maisie?"
    hide blorgo normal
    with dissolve

    show maisie normal
    with dissolve
    m "Yes, Blorgo?"
    hide maisie normal
    with dissolve
    
    show blorgo normal
    with dissolve
    b "Are we actually going to the Sun?"
    hide blorgo normal
    with dissolve

    show maisie smile
    with dissolve
    m "You must be really excited, Blorgo."
    hide maisie smile
    with dissolve

    show blorgo normal
    with dissolve
    b "Not really… how can I be excited when I don’t know where we’re going?"
    hide blorgo normal
    with dissolve

    show maisie normal
    with dissolve
    m "Don’t worry, you’ll know real soon."

    m "Ready for lift off?"
    hide maisie normal
    with dissolve

    st "{size=+10}Yes, Miss Maisie!{/size}"

    "The rocket bus takes off, zipping into space."

    jump scene3


label scene3:
    ### SCENE 3 ###
    scene bg space
    with fade

    show maisie smile
    with dissolve
    m "Kids!" 
    "She claps once and the bus falls quiet."

    m "Can someone tell me where we’re going today?"
    hide maisie smile
    with dissolve
    
    show melina 
    with dissolve
    me "We’re going to the Sun to learn about space weather and how it affects—"
    hide melina 
    with dissolve
    
    show kaylan smile
    with dissolve
    k "We’re going to the Sun!!!"
    hide kaylan smile
    with dissolve

    st "{size=+10}Yaaayyyy!{/size}"

    show maisie stern
    with dissolve
    m "Settle down. Kaylan, apologise."
    hide maisie stern
    with dissolve

    show kaylan smile
    with dissolve
    k "I’m sorry, Melina."
    hide kaylan smile
    with dissolve 

    show melina
    with dissolve
    me "Apology accepted."
    hide melina 
    with dissolve

    show maisie smile
    with dissolve
    m "Excellent, Melina. That’s correct. This field trip is about the Sun and our last unit in class."

    m"Now, look out the bridge."
    hide maisie smile
    with dissolve

    scene sunshot
    with fade
    
    b "Whoaaa… this is so cool!"

    m "What are we looking at, kids?"

    st "The Sun!"

    m "Correct. Now… how many layers is the Sun’s atmosphere made of?"

    show katie 
    with dissolve
    ka "3 layers!"
    hide katie
    with dissolve
    
    show lloyd with dissolve
    l "No, 4!"
    hide lloyd with dissolve

    m "Settle down. You’re both right. Who can name one?"

    show landon with dissolve
    la "Chomospere!"
    hide landon with dissolve
    
    show suzy with dissolve
    s "Corona!"
    hide suzy with dissolve
    
    show blorgo normal with dissolve
    b "Photosphere!"
    hide blorgo normal with dissolve

    "The students argue loudly until Miss Maisie claps again."

    m "Students! What did I say about answering questions?"

    st "We should raise our hands first, Miss Maisie."

    m "Good. Now let’s try again."

    jump scene4


label scene4:
    ### SCENE 4 ###
    scene bg sun
    with fade

    
    m "Now, who can tell me what space weather is?"

    "The children look puzzled. Blorgo raises his hand slowly."

    
    b "Is it like… the rain and snow we get on our planet?"

    
    m "Great question, Blorgo! Not quite. Space weather happens when the Sun releases solar wind, solar flares, and coronal mass ejections."

    
    t "What do those things do?"

    
    m "The solar wind is like an invisible river of charged particles. Sometimes there are outbursts — powerful solar flares, or huge bubbles called coronal mass ejections. These can shake up a planet’s magnetic shield."

    
    ka "Does it hurt people?"

    
    m "Earth is protected by its magnetic field and atmosphere — like a superhero shield! But strong space weather can cause auroras, or disrupt satellites and electricity grids."

    
    me "Wow, does every planet get space weather?"

    m "That’s right! But planets like Mars, with weak magnetic fields, aren’t as protected."

    
    b "Is that why we’re so safe, Miss Maisie?"

    m "Exactly! That’s why scientists study space weather."

    jump scene5


label scene5:
    ### SCENE 5 ###
    scene bg sun
    with dissolve

    
    t "Miss Maisie, what happens to astronauts when there’s strong space weather?"

    
    m "Excellent question! Astronauts sometimes move to shielded areas on the ISS during solar storms. On Earth, humans are mostly safe, but astronauts must be extra careful."

    
    b "What about satellites?"

    
    m "They can be disturbed by solar storms — signals scrambled, or even electrical problems. That’s why space weather tracking is so important."

    
    me "And auroras happen because of space weather?"

    
    m "Yes! Auroras are glowing lights caused when solar energy hits Earth’s magnetic field."

    
    t "I wish we could see one!"

    m "Maybe you will see one soon. Now, why doesn’t Mars have strong auroras?"

    
    ka "Because it doesn’t have a strong magnetic field?"

    m "That’s right!"

    scene bg auroras
    with fade
    "The students stared in wonder at the stunning movements of the auroras"

    jump scene6


label scene6:
    ### SCENE 6 ###
    

    show maisie smile with dissolve
    m "When the Sun sends solar flares or CMEs, they can hit Earth’s magnetic field. That causes geomagnetic storms."
    
    
    b "What happens during those storms?"

    
    m "Satellites can lose signal, electricity grids can be disrupted, even airplanes near the poles can have trouble. GPS and phones too!"

    
    me "So should we be worried?"

   
    m "Not at all! Most space weather is mild. Scientists track the Sun closely and warn us if something big is coming."
    hide maisie smile with dissolve
    
    show katie with dissolve
    ka "I think space weather is amazing! I want to protect our technology someday!"
    hide katie with dissolve
    "The kids chatter excitedly as the bus turns around."

    jump scene611

label scene611:
    m "Before we arrive home, I have a surprise for you guys. Look at the window outside."

    scene bg spacestation
    with fade

    "Outside the window, a massive space station glides into view, gleaming silver against the stars."

    
    b "This station is huge!!! Oh, Miss Maisie!"


    "The ship gently docks at the station’s foyer. The kids unbuckle their seatbelts and step out, wide-eyed."
    scene bg space deck
    show maisie smile
    with dissolve
    m "This is the NASA Space Station. It belongs to the people of Earth. We’ll be joined by Commander Sena Azor — she’s an astronaut from Earth. Earth people live in groups called countries, and there are many of them. She’s from a country called Ghana."
    hide maisie smile
    with dissolve

    show sena normal
    with dissolve
    sena "(waving cheerfully) Hello, young scientists! Welcome aboard my home in space. I’m Commander Sena Azor, a scientific researcher for NASA on Earth."
    hide sena normal
    with dissolve

    show blorgo normal
    with dissolve
    b "(starry-eyed) Wow… you live here?"
    hide blorgo normal
    with dissolve

    show sena normal
    with dissolve
    sena "That’s right! And one of the biggest challenges I face up here is something you’ve been learning about today — space weather."
    hide sena normal
    with dissolve

    scene bg deckshot
    with fade
    ka "(tilting her head) Does space weather hurt you?"
    

    sena "Sometimes it can be dangerous. When the Sun sends out strong solar storms, I have to move into a shielded part of the station to stay safe from harmful radiation."


    me "(leaning forward) Does it only affect you up here, or does it affect Earth too?"
    

    
    sena "Great question! Space weather reaches Earth as well. It can make satellites glitch — which means GPS might not work right. GPS helps people find their location. It can also interrupt radio signals, which affects pilots and sometimes spaceships."
    sena "Big storms from the Sun can even make electricity on Earth act funny — lights flicker, or the power goes off for a while! And sometimes, it makes beautiful auroras dance in the sky."
    

    
    t "(eyes wide) So you can lose your GPS?"
    

    sena "Exactly! People like farmers can be affected — their tractors might not plant seeds in straight rows. Even people using phones or maps can be affected."
    

    b "What about astronauts like you?"
    

    sena "We have to be extra careful. When a big storm comes, I stop spacewalks, protect the computers, and move into the shielded room. NASA scientists on Earth warn us ahead of time so we can stay safe."
 

    ka "(giggling) So space weather is like… the Sun sneezing on everybody or having a fever?"
    
    sena "(laughs warmly) That’s a good joke! And just like sneezes, some are tiny and harmless — but some are huge and powerful."
    

    m "(to the class) See, children? Space weather isn’t just science far away — it affects farmers, pilots, astronauts, and even you at home."
  

    "The children gather at the station window, gazing down at Earth glowing beneath them. A soft shimmer of auroras dances near the poles."

    
    sena "That’s the aurora — a beautiful gift from space weather. Proof that the Sun and Earth are always connected."

    scene bg space deck
    show maisie normal
    with dissolve
    m "What do we say to Commander Sena?"
    hide maisie normal
    with dissolve

    st "{size=+10}Thank you, Commander Sena!{/size}"

    "They walk back to the spaceship, board it, and fasten their seatbelts as the bus detaches from the station, beginning its trip home."

    jump scene7



label scene7:
    ### SCENE 7 ###
    scene bg space
    with fade

    
    m "Before we arrive home, let’s share something new we learned today."

    show trafalgar excited with dissolve
    t "I learned the Sun can send storms that change how we use our phones."
    hide trafalgar excited with dissolve
    
    show katie with dissolve
    ka "Auroras are magical lights that come from the Sun."
    hide katie with dissolve

    show blorgo normal with dissolve
    b "Space weather can be dangerous for astronauts, but scientists keep them safe."
    hide blorgo normal with dissolve

    show melina with dissolve
    me "Earth’s magnetic field is like a superhero shield!"
    hide melina with dissolve

    
    m "Wonderful answers! Remember, the universe is full of surprises."

    jump scene8


label scene8:
    ### SCENE 8: HEADING HOME ###
    scene bg docking
    with fade

    "The rocket bus glides into the school’s docking bay. Children rush off, full of excitement."

    show maisie smile
    with dissolve
    m "See you tomorrow, scientists! Don’t forget to share what you learned with your families!"
    hide maisie smile
    with dissolve

    "The students run home, their heads full of auroras, sunspots, and dreams of future adventures."


    stop music fadeout 2.0
    return