def is_isogram(word):
    if type(word) != str:
        raise TypeError('Argument should be a string')

    elif word == " ":
        return word, False
    else:
        word = word.lower()
        for letter in word:
            if word.count(letter) > 1:
                return word, False

                return word, True


print is_isogram("abolishment")
