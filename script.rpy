# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character(_("Me"), color="#1a7f12")
define a = Character(_("Ash"), color="#1d98a4")
define g = Character(_("Guardian"), color="#A41d4c")
define f = Character(_("Fey"), color="#645241")
define s = Character(_("Shadow"), color="#520b0b")
define c = Character(_("Chest"), color="#Ae1dd2")


image treasuremap = "treasuremap.jpg"


# The game starts here.



label start:
    stop music fadeout 1.0
    play music "introduction.opus"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene introductionimage
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    "   In the quiet village of Osgard, a legend echoes through the ages— the fabled Treasure of Osgard hidden deep within the perilous Silent Grove. You, adventurer, arrive in search of riches and glory. Little do you know that the quest for Osgard's treasure will be filled with mystery, choices, and unforeseen consequences. Watch your step."

    scene villagecenter
    with fade

    stop music fadeout 1.0
    play music "villagetheme.opus"

    "   Upon reaching the village center, you learn about the Treasure of Osgard. The villagers are torn between fear and curiosity and ask if you want to try and solve the mystery."

    menu:

        "You think about this very hard, but you choose..."

        "Take the Quest":

            jump takequest

        "Don't take the Quest":

            jump noquest

        "Seek more insight about the village":

            jump insight

label takequest:
    stop music fadeout 1.0
    play music "takequestmusic.opus"

    scene grove
    with fade

    "   As you approach Silent Grove, you find an ancient map portraying a treasure. The map is filled with symbols and some sort of riddle."

    show treasuremap at center
    with Dissolve(2.65)
    pause 4.0

    scene grove
    with fade

    menu:

        "Decipher Symbols on your own":

            jump decipher

        "Trust Instincts":

            jump instinct1

        "Seek Mystic Guidance back at village":

            jump mystic


label decipher:
    stop music fadeout 1.0
    play music "takequestmusic.opus"

    scene grove
    with fade

    "You try to decipher the symbols, but you can't manage to figure out the language."

    menu:

        "Decipher Symbols on your own":

            jump decipher

        "Trust Instincts":

            jump instinct1

        "Seek Mystic Guidance back at village":

            jump mystic








label mystic:
    stop music fadeout 1.0
    play music "mystic.opus"

    scene mysticbackground
    with fade

    "   You decided to seek a mystic's guidance at the village"

    show ash

    "   A middle-aged woman stands at the counter, as you approach her she says..."

    a "Well, I assume you have come to ask about the treasure."

    menu:

        "Show Treasure Map":

            jump mystic1

        "Ask what she knows about the treasure":

            jump mystic2


label mystic1:
    stop music fadeout 1.0
    play music "mystic.opus"

    scene mysticbackground
    with fade

    show ash

    a "Ah, now I sense this map to have magical properties. It is very old and I see symbols that depict a trap on a leading path."

    "   You have learned about a deceiving path that would of lead to very bad consequences. You proceed to thank Ash and leave the shop."

    menu:

        "Return to Silent Grove":

            jump groove2


label groove2:
    stop music fadeout 1.0
    play music "takequestmusic.opus"

    scene grove
    with fade

    menu:

        "Decipher Symbols on your own":

            jump decipher1

        "Trust Instincts and the newly acquired knowledge":

            jump instinct

        "Seek Mystic Guidance back at village":

            jump mystic


label decipher1:
    stop music fadeout 1.0
    play music "takequestmusic.opus"

    scene grove
    with fade

    "You try to decipher the symbols, but you can't manage to figure out the language."

    menu:

        "Decipher Symbols on your own":

            jump decipher

        "Trust Instincts and the newly acquired knowledge":

            jump instinct1

        "Seek Mystic Guidance back at village":

            jump mystic



label instinct1:
    stop music fadeout 1.0
    play music "takequestmusic.opus"

    scene instinctdeath
    with fade

    "You have chosen to traverse with not a lot of knowledge of this land."

    "Regardless, you continue on the path forward."

    menu:

        "Continue the path":

            jump instinctdead

label instinctdead:
    stop music fadeout 1.0
    play music "instinctdeath.opus"

    scene instinctdeath
    with fade

    "As you walk across you feel uneasy."

    "Suddenly, you feel your feet fall through the ground."

    "As you fall into a deep hole and reach the ground, you see many skulls around you."

    "You are stuck adventurer and it is only a matter of time until you become another skull."

    menu:

        "Restart Adventure":

            return







label instinct:
    stop music fadeout 1.0
    play music "takequestmusic.opus"

    scene instinctcorrect
    with fade

    "You have decided to continue the path with increased knowledge."

    "You avoid a trap that would of took your life most likely."

    "As you travel along the path you come across a guardian"

    menu:

        "Approach Guardian":

            jump guardian



label mystic2:
    stop music fadeout 1.0
    play music "mystic.opus"

    scene mysticbackground
    with fade


    show ash

    a "I know a lot of stories about adventurers ending up dead or disappearing. Some townsfolk have heard stories of a strange creature guarding the depths, but nobody has truly seen it."

    menu:

        "Show Treasure Map":

            jump mystic1

        "Ask what she knows about the treasure":

            jump mystic2




label guardian:
    stop music fadeout 1.0
    play music "guardian.opus"

    scene instinctcorrect
    with fade

    show guardian

    g "A traveler I see, you must solve the riddle to get past the gates."

    g "What has many keys but can't open any doors?"

    menu:

        "A salesman":

            jump guardiansalesman

        "A piano":

            jump correct

        "A keyboard":

            jump guardiankeyboard


label guardiansalesman:
    stop music fadeout 1.0
    play music "guardian.opus"

    scene instinctcorrect
    with fade

    show guardian

    g "That is incorrect. Try again."

    menu:

        "A salesman":

            jump guardiansalesman

        "A piano":

            jump correct

        "A keyboard":

            jump guardiankeyboard


label guardiankeyboard:
    stop music fadeout 1.0
    play music "guardian.opus"

    scene instinctcorrect
    with fade

    show guardian

    g "That is incorrect. Try again."

    menu:

        "A salesman":

            jump guardiansalesman

        "A piano":

            jump correct

        "A keyboard":

            jump guardiankeyboard


label correct:
    stop music fadeout 1.0
    play music "mystic.opus"

    scene instinctcorrect
    with fade

    show guardian

    g "That is correct. You may proceed."

    "The guardian gives you a key. You can feel something special about, but you don't know what it is."

    menu:

        "Continue":

            jump chapter4


label chapter4:
    stop music fadeout 1.0
    play music "mystic.opus"

    scene instinctcorrect
    with fade

   

    "As you continue your journey, you start to hear whispers coming from all around the forest."

    "You feel a sensation that you are being watched."

    menu:

        "Follow Whispers":

            jump followwhispers

        "Ignore Whispers":

            jump ignorewhispers


label followwhispers:
    stop music fadeout 1.0
    play music "disorientation.opus"

    scene disorientationimage
    with fade

    play sound "whispers.mp3"


    "You start to become nauseous and start hallucinating voices in your head."

    "You have become trapped in your own thoughts."

    "Adventurer, you have become lost forever."

    menu:

        "Restart Adventure":

            return

    

label ignorewhispers:
    stop music fadeout 1.0
    play music "mystic.opus"

    scene instinctcorrect
    with fade

    "You choose to ignore the whispers and continue your journey."

    menu:

        "Continue down the path":
            jump chapter5




label chapter5:
    stop music fadeout 1.0
    play music "chapter5.opus"

    scene chamberbackground
    with fade

    "   As you traverse deeper into Silent Grove, you come across a structure that seems to be a chamber. There is a small chest sitting by this structure, and it seems to be emmiting a strange purple light."

    "There is also a statue of some type of cryptid by the chest."

    "   You feel as if this energy is from a different world."

    menu:

        "Confront the Statue":

            jump statue            

        "Carefully take the treasure":

            jump careful

        "Take the treasure along with the statue":

            jump notcareful


label statue:
    stop music fadeout 1.0
    play music "chapter5.opus"

    scene chamberbackground
    with fade

    show statue

    "You can see this statue portrays a very strange creature. It seems to be a presence around you."

    "It seems to be carved out of a shiny material, and you notice very strange markings on it."

    "Curiously, you move to the chest past the statue."

    menu:

        "Carefully take the treasure":

            jump careful

        "Take the treasure along with the statue":

            jump notcareful


label notcareful:
    stop music fadeout 1.0
    play music "growlmusic.opus"

    scene chamberbackground
    with fade

    play sound "growl.opus"

    "You hear a loud growl and you start to panic."

    "The ground starts trembling and you start to become uneasy."

    "You slowly feel your whole body disintegrating one by one."

    "Adventurer, you have dissipated before your very own eyes."

    menu:

        "Restart Adventure":

            return


label careful:
    stop music fadeout 1.0
    play music "chapter5.opus"

    scene chamberbackground
    with fade

    "You carefully take the small chest with you."

    "You try to be as careful as possible."

    "The chest is almost weighless, with purple particles still emmiting from it."


    menu:

        "Proceed with caution":

            jump chapter6


label chapter6:
    stop music fadeout 1.0
    play music "shadows.opus"

    scene chapter6background
    with fade    
    
    "As you progress the path, you start to feel like you are being watched again."

    "Suddenly the forest around you turns dark and day becomes night."

    show shadowperson

    "A shadow stands before you, with a mystical presence."

    "This being can communicate telepathically with you."

    menu:

        "Start heading towards the trail on the left":

            jump chapter7


        "Follow the icy wind filled with voices":

            jump wind

        "Ask the shadow what it wants":

            jump shadow1



label wind:
    stop music fadeout 1.0
    play music "shadows.opus"

    scene chapter6background
    with fade    

    "You decide to follow the voices in the wind."

    show fey

    "You stumble across an elf?"

    f "Hey, can I have your name?"

    menu:

        "Yes":

            jump yesdeath


        "No":

            jump nocontinue



label yesdeath:

    play sound "portal.opus"
    stop music fadeout 1.0
    play music "deathyes.opus"

    

    scene feywild
    with fade 

    "You are lost forever in this realm. Nameless and forgotten."

    menu:

        "Restart Adventure":

            return



label nocontinue:

    
    stop music fadeout 1.0
    play music "shadows.opus"

    scene chapter6background
    with fade   


    "You refused to tell this creature your name."

    "You walk back to where the shadow is standing."

    menu:

        "Start heading towards the trail on the left":

            jump chapter7


        "Follow the icy wind filled with voices":

            jump wind

        "Ask the shadow what he wants":

            jump shadow1


label shadow1:

    
    stop music fadeout 1.0
    play music "shadows.opus"

    scene chapter6background
    with fade   

    show shadowperson


    s "Beware adventurer, that treasure holds great power and only the most honorable are fit to open it."

    s "Watch your own shadow and stay alert."

    "You understood exactly what this being said to you, as you feel a special connection."

    "You take into account the shadow's advice."

    menu:

        "Go to the path on the left":

            jump chapter7

        "Follow the icy wind's voices":

            jump wind



label chapter7:

    
    stop music fadeout 1.0
    play music "chapter7.opus"

    scene village2
    with fade   

    "You travel the path on the left and make it back to the village."

    "The townsfolk gather around you shocked in disbelief."

    "You place the chest down."

    show chest

    "One villager shouts: 'You must open it traveller! Please Open it!'"

    menu:

        "Open Chest":

            jump openchest

label openchest:

    play sound "chestopen.opus"
    play sound "magic.opus"
    stop music fadeout 1.0
    play music "chapter7.opus"

    scene village2
    with fade

    "As you open the chest a wave of tremendous energy took the air."

    "The chest vibrates with a constant purple field."

    "You hear a voice in your head."

    c "Finally, a worthy adventurer."

    c "I have been waiting for centuries until the right person found me."

    c "Adventurer, there is only one step left for greatness."

    c "Hold me up in the air and the village will be free."

    menu:

        "Hold Chest Up":

            jump victory



label victory:

    
    stop music fadeout 1.0
    play music "heroicmusic.opus"


    scene villageheroic
    with fade

    "As you hold the chest up, it disappears into a clump of purple particles."

    "The purple particles fly all around the village and the joy of people can be heard."

    "You notice the village transforming."

    "Rivers that were dry start running again."

    "Village houses are transformed and repaired."

    "Old people rejuvenate and are young again."

    "Sick people are cured."

    "Again, you hear happiness all around the village center."

    "You did it adventurer."

    "You solved the mystery and in the process freed the village."

    "You are the hero of the village adventurer."

    "The End"

    menu:

        "Main Menu":

            return

        "Credits":

            jump credits1


label credits1:

    
    stop music fadeout 1.0
    play music "heroicmusic.opus"

    scene villageheroic
    with fade


    "Mystery & Adventure theme: https://freesound.org/people/tyops/sounds/264873/
"

    "Grove Image: https://www.artstation.com/artwork/xY31ar"

    "Mystic Background: https://www.pinterest.com/pin/daily-ambient-atmosphere-for-writing-more-listen-to-magic-for-sale-magic-shop-mythical-mystic-a--379146862374167535/
"

    "Background Instinct: https://www.freepik.com/free-photos-vectors/sinister-surroundings/43"

    "Instinct Death theme: https://freesound.org/people/theoctopus559/sounds/705317/"

    "Guardian Background: https://freesound.org/people/UNIVERSFIELD/sounds/702869/"

    "Disorientation Theme: https://freesound.org/people/MATRIXXX_/sounds/658288/"

    "Sinister Image: https://www.prompthunt.com/prompt/cl9g6x2le1542q7lqo1zk56r5?selectedAsset=cl9g6x49e1598q7lq9r1wo4rp"

    "Whispers Sounds: ohnobones on freesoundorg.com"

    "Chamber Background: https://www.artstation.com/artwork/aYZAOk"

    "Cryptid Image: https://www.etsy.com/listing/972997789/mothman-model-for-dungeons-and-dragons"

    "Sound for Growl: https://freesound.org/people/cylon8472/sounds/249686/"

    "Mystical Sound: https://freesound.org/people/UNIVERSFIELD/sounds/706529/"

    "Fey Image: https://criticalrole.fandom.com/wiki/Fey"

    "Fey Background: https://deathbymage.com/2017/02/21/realms-of-the-feywild-a-land-of-mystery-and-oddity/"

    "Village2 Background: https://thenerdd.com/2021/05/07/making-your-starting-town-in-dd/"

    "Chest Image: https://www.reddit.com/r/DnD/comments/jdnbu2/oc_the_chest_of_magic_nullification_envelopes_the/"

    "Heroic Music: https://freesound.org/people/SoundFlakes/sounds/423499/"

    menu:

        "Main Menu":

            return











label noquest:
    stop music fadeout 1.0
    play music "villagetheme.opus"

    scene villagecenter
    with fade

    "   You decided not to take the quest."

    "   Your journey ends early adventurer."

    menu:

        "Return to villagers and accept quest":

            jump takequest

        "End your adventure":

            return

label insight:
    stop music fadeout 1.0
    play music "insight.opus"

    scene villagecenter
    with fade

    "   The villagers tell you all about the strange occurances happening at the village."
    
    "   They tell you how their village was built a long time ago from the ground up and has never been to war. You learn that many have tried to solve the mystery, but ended up dead or never to be seen again."

    "   The villagers also tell you how a lot of them have become sick and their rivers stopped running."

    menu:

        "Take the Quest":

            jump takequest

        "Don't take the Quest":

            jump noquest 










    # This ends the game.

    return
