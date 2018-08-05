from unittest import TestCase

word = input('enter the word you would like to test: ')
def is_isogram(word):
    if type(word) != str:
        raise TypeError('Argument should be a string')

    elif word == "":
      return (word, False)
    else:
        for char in word:
            if word.count(char) > 1:
                return (word, False)
    return (word, True)

print(is_isogram(word))