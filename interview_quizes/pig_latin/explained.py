# Credits to DUznanski for his solution:
# http://exercism.io/submissions/c79beee84e694323b62f37c389224eaf

import re

PIGLATIN_CONSONANTS = re.compile(r'^((?:qu|[bcdfghjklmnpqrstvwz]|[xy](?=[aeiouy]))*)(.*)')
# ^ -> starts from the begining of the string
# () -> creates a group that will be captures by \1
# (?:) -> creates a group that won't be captured
# qu|[bcdfghjklmnpqrstvwz]|[xy](?=[aeiouy] -> specifies what is considered a consonant: 'qu', normal consonants, and 'x' or 'y' followed by a vowel
# * -> consonants happening zero or more times
# (.*) -> any character zero or more times


def translate(phrase):
    return ' '.join(PIGLATIN_CONSONANTS.sub(r'\2\1ay', word)
                    for word in phrase.lower().split())