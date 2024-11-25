import time
import sys
import random
from threading import Timer
#from replit import audio

letter_og = '''
    November 24, 2024
    Dearest Helene,
    I don’t even know where to start because, honestly, my brain turns into a melted Slurpee whenever I think about you (which is all the time, by the way).
    You’re like... the moon in my dark, starless night sky. No, wait, you’re cooler than the moon, like,
    if the moon wore eyeliner and listened to My Chemical Romance.
    You’re the most enigmatic person I’ve ever met. (Yeah, I had to look up that word, but it felt right.) It’s like you have this mysterious aura around you, and
    I’m just a moth, hopelessly flying toward your beautifully dark flame. You’re so different from everyone else—so deep and poetic and, like, otherworldly.
    I swear, even the way you walk through the hallways makes it look like you’re in a music video.
    I’m not gonna lie; I’ve definitely tried to memorize your schedule so I can "accidentally" bump into you between classes.
    (I hope that’s not weird? It’s not weird, right?) Anyway, every time I see you, my heart feels like it’s moshing at a pop-punk concert. It’s painful, but in,
    like, the best way possible.
    You probably think I’m just some random dork, but I feel like we’re meant to be. Like, the universe put us in the same school for a reason.
    I’ve been listening to all the bands you have on your backpack patches, and I’ve even started trying to write poetry because I want to understand your vibe.
    Here’s one I wrote about you:
    "She walks alone, a shadow’s grace,
    In her eyes, a cosmic space.
    Her headphones on, the world’s a blur,
    My heart beats faster... all for her."
    I know, I know—it’s bad. But I promise I’d write you a million more poems if it would make you smile even once.
    Anyway, I guess what I’m trying to say is that you’re the Juliet to my slightly awkward Romeo (but, like, cooler and with better music taste).
    If you ever want to talk, or, you know, sit together in brooding silence, I’d be the happiest guy alive.
    Forever wishing to be the eyeliner to your smokey eyes,
    Denis
    P.S. I wrote your name in sharpie on my arm last night. It smudged, but my love never will.
    '''
letter= letter_og
clone_text = [
    "You smell like a mix of sadness and Febreze, and it’s honestly intoxicating.",
    "Every time I see you, my stomach does flips, like when I eat gas station sushi.",
    "I’d let you copy my homework, even though last time I accidentally handed in a blank page.",
    "Your hair reminds me of a wet mop—but like, the coolest wet mop ever.",
    "I bet your favorite color is black, just like my search history after midnight.",
    "If we were animals, I’d be a lonely raccoon, and you’d be the fancy trash can I dream about.",
    "I’d hold your hand, but they’re so clammy, you might think I just got out of a swamp.",
    "If love was a video game, I’d already be out of lives, but I’d still spam ‘restart’ for you.",
    "I’d write your name in the sky, but my handwriting’s so bad the planes would probably crash.",
    "I like the way you chew gum—so loud, it’s like a beautiful, angry horse eating hay."
]
#letter=letter.split(" ")

prompt_text = '''______     _                               _ _   _                 _                  _   _            _     
| ___ \   | |                             (_) | | |               | |                | | | |          | |  _ 
| |_/ /___| |_ _   _ _ __   ___  __      ___| |_| |__   ___  _   _| |_   _ __ ___  __| | | |_ _____  _| |_(_)
|    // _ \ __| | | | '_ \ / _ \ \ \ /\ / / | __| '_ \ / _ \| | | | __| | '__/ _ \/ _` | | __/ _ \ \/ / __|  
| |\ \  __/ |_| |_| | |_) |  __/  \ V  V /| | |_| | | | (_) | |_| | |_  | | |  __/ (_| | | ||  __/>  <| |_ _ 
\_| \_\___|\__|\__, | .__/ \___|   \_/\_/ |_|\__|_| |_|\___/ \__,_|\__| |_|  \___|\__,_|  \__\___/_/\_\\__(_)
                __/ | |                                                                                      
               |___/|_|                                                                                      '''
sorry = ''' _____                           _   _                _                   
/  ___|                         | | (_)              ( )                  
\ `--.  ___  _ __ _ __ _   _    | |_ _ _ __ ___   ___|/ ___   _   _ _ __  
 `--. \/ _ \| '__| '__| | | |   | __| | '_ ` _ \ / _ \ / __| | | | | '_ \ 
/\__/ / (_) | |  | |  | |_| |_  | |_| | | | | | |  __/ \__ \ | |_| | |_) |
\____/ \___/|_|  |_|   \__, ( )  \__|_|_| |_| |_|\___| |___/  \__,_| .__/ 
                        __/ |/                                     | |    
                       |___/                                       |_|    '''

yes = ''' _____ _                      _     _                   _ 
/  ___| |                    (_)   | |                 | |
\ `--.| |__   ___   ___  __ _ _  __| |  _   _  ___  ___| |
 `--. \ '_ \ / _ \ / __|/ _` | |/ _` | | | | |/ _ \/ __| |
/\__/ / | | |  __/ \__ \ (_| | | (_| | | |_| |  __/\__ \_|
\____/|_| |_|\___| |___/\__,_|_|\__,_|  \__, |\___||___(_)
                                         __/ |            
                                        |___/             '''

no = ''' _____ _                      _     _                    __
/  ___| |                    (_)   | |                _ / /
\ `--.| |__   ___   ___  __ _ _  __| |  _ __   ___   (_) | 
 `--. \ '_ \ / _ \ / __|/ _` | |/ _` | | '_ \ / _ \    | | 
/\__/ / | | |  __/ \__ \ (_| | | (_| | | | | | (_) |  _| | 
\____/|_| |_|\___| |___/\__,_|_|\__,_| |_| |_|\___/  (_) | 
                                                        \_\
                                                           '''

#source = audio.play_file("black_parade_intrumental.mp3")
#source.paused = False


def reset_letter(letter):
    spaces = []
    for i in range(len(letter)):
        if letter[i] == " ":
            spaces.append(i)
    rand_letter_index = random.choice(spaces)
    rand_phrase = random.choice(clone_text)
    letter = letter[
        0:rand_letter_index] + f"\033[31m{rand_phrase}\033[0m" + letter[
            rand_letter_index:]
    return letter


'''def reset_new_letter(inout_letter):
    spaces = []
    for i in range(len(input_letter)):
        if input_letter[i] == " ":
                spaces.append(i)
        rand_letter_index = random.choice(spaces)
        rand_phrase = random.choice(clone_text)
        input_letter = input_letter[0:rand_letter_index] + f"\033[31m{rand_phrase}\033[0m" + input_letter[rand_letter_index:]
        input_letter = input("write without the red text" + letter)'''


def difference_dector(str, compare_to):
    differences = 0
    for i in range(len(str)):
        if str[i] != compare_to[i]:
            differences += 1
    if differences <= 100:
        return f"\033[31m{yes}\033[0m"
    else:
        return f"\033[31m{no}\033[0m"


start_time = time.time()
for i in range(10):
    letter = reset_letter(letter)
timeout = 30
t = Timer(timeout, print, [f"\r\033[31m{sorry}\033[0m"])
t.start()
prompt = f"\033[31m{prompt_text}\033[0m" + letter
answer = input(prompt)
difference_dector(letter, letter_og)
t.cancel()