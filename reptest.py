import sys
import time
import random

def get(type):

#    random.seed(time.time() + 64738)
    rng = random.SystemRandom(time.time() * 64738)
    sort = random.SystemRandom(time.time() * 64738)
    if type == 'dick':
        rng.shuffle(DICK)
        return sort.choice(DICK)
    elif type == 'iching':
        linecount = ["hello"]
        lineplace = 8
        for g in range (6): 
            rng.shuffle(ICHING)
            coin3 = sort.choice(ICHING) 
            if coin3 == 1 :
                linecount.append(lineplace);
            lineplace = lineplace-1
        return linecount

ICHING = [1, 1, 1, 0, 0]

DICK = [
    "You have herpes.",
    "It is small and insignificant like the rest of your life.",
    "No one cares about your incher.",
    "I advise you to keep the lights off and substitute for a strap-on instead.",
    "It's practically an innie.",
    "The only thing you'll successfully have sex with is a pasta strainer.",
    "Your sex reassignment surgery will be a breeze.",
    "Your dick is so ugly it cries itself to sleep at night.",
    "It looks like a California raisin."
]

