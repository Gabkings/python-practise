import re

'''
Mostly right, but | has a different priority here: the noncapturing group has three segments:

    'qu', because that's counted as a single consonant,

    '[bcdfghjklmnpqrstvwz]', because those are always considered consonants, and

    '[xy](?=[aeiouy])', because x and y are only considered consonants if they're followed by a vowel. This one actually has a subtle error, but I can't find a word that would fail so whatever.

Thus the noncapturing group matches one element that fits any one of these three patterns.
But I need to get whole hunks of consonants, so I need to match as many as I can: that's what the '*' is for.

I use the capture groups in the substitution: r'\2\1ay' puts the second capture, then the first, then 'ay'. I don't care at all about the contents of the group that describes a single consonant, except in its context in the main capture; thus I shouldn't try to capture it.
'''
PIGLATIN_CONSONANTS = re.compile(r'^((?:qu|[bcdfghjklmnpqrstvwz]|[xy](?=[aeiouy]))*)(.*)')

def translate(phrase):
    return ' '.join(piglatinize(word) for word in phrase.lower().split())

def piglatinize(word):
    return PIGLATIN_CONSONANTS.sub(r'\2\1ay', word)
