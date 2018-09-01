sentence = input("Please enter a sentence: ")
vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
words = sentence.split()

count = 0


def find_vowel(word):
    for i in range(len(word)):
        if word[i] in vowels:
            return i
    return -1


for word in words:
    vowel = find_vowel(word)

    if(vowel == -1):
        print(word, ' ', end='')

    elif(vowel == 0):
        print(word + "way", ' ', end='')

    else:
        print(word[vowel:] + word[:vowel] + "way", ' ', end='')
        break
