def is_isogram(word):
    # to get the type of word
    if type(word) != str:
      # print error
        raise TypeError("Argument should be a String")
        # remove space
    elif word.strip() == "":
        return(word, False)
    else:
      # change to lower case
        word = word.lower()
        # check each letter in word
        for char in word:
          # count the number of words
            if word.count(char) > 1:
                return (word, False)
            else:
                return(word, True)


print(is_isogram('Machine'))
