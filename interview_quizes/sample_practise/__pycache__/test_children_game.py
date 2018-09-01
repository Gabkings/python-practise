import unittest

from children_game import find_vowel
from children_game import format_string


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class PigLatinTest(unittest.TestCase):
    
    def test_word_beginning_with_a(self):
        self.assertEqual(("apple"), "appleay")

    


if __name__ == '__main__':
    unittest.main()

'''
Mostly right, but | has a different priority here: the noncapturing group has three segments:

'qu', because that's counted as a single consonant,

'[bcdfghjklmnpqrstvwz]', because those are always considered consonants, and

'[xy](?=[aeiouy])', because x and y are only considered consonants if they're followed by a vowel. This one actually has a subtle error, but I can't find a word that would fail so whatever.

Thus the noncapturing group matches one element that fits any one of these three patterns. But I need to get whole hunks of consonants, so I need to match as many as I can: that's what the '*' is for.

I use the capture groups in the substitution: r'\2\1ay' puts the second capture, then the first, then 'ay'. I don't care at all about the contents of the group that describes a single consonant, except in its context in the main capture; thus I shouldn't try to capture it.
'''

'''
This is an interesting solution! 
But there are a few things that I couldn't understand.

Is the following interpretation of the regex correct?

r' -> Indicates the use of raw string

^ -> Start from the beginning of the sentence

( ->Creates a group to capture the expression inside it

(?: -> Creates a group that won't capture the expression inside it

qu|[bcdfghjklmnpqrstvwz]|[xy] -> Matches 'qu' OR a consonant OR 'either x or y'

(?=[aeiouy])) -> A vowel follows the previous expression

*) The group can be matched zero or more times

(.*)' -> Any character zero or more times

Why do you have to use these groups anyway? Is it because you want to use them in the .sub() later?

What about the (?:) groups? Why don't you want to capture them?

Also, why does it work for words like 'school' and 'therapy'?

'''
'''
This is an interesting solution! 
But there are a few things that I couldn't understand.

Is the following interpretation of the regex correct?

r' -> Indicates the use of raw string

^ -> Start from the beginning of the sentence

( ->Creates a group to capture the expression inside it

(?: -> Creates a group that won't capture the expression inside it

qu|[bcdfghjklmnpqrstvwz]|[xy] -> Matches 'qu' OR a consonant OR 'either x or y'

(?=[aeiouy])) -> A vowel follows the previous expression

*) The group can be matched zero or more times

(.*)' -> Any character zero or more times

Why do you have to use these groups anyway? Is it because you want to use them in the .sub() later?

What about the (?:) groups? Why don't you want to capture them?

Also, why does it work for words like 'school' and 'therapy'?
'''