from random import random


def coin_flip():
    face = random()
    if face > 0.5:
        faceup = 'head'
    else:
        faceup = 'tail'
    return faceup


con = coin_flip()
print(con)
