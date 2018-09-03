def longest(string):
    words = string.split(' ')
    return max(words, key=len)
