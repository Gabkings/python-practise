'''
1: creation of function called printValue
2: the function should take two strings 
3: the first if should test whether the first string is longer than the second
'''

def printValue(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len2 > len1:
        print(s2)
    else:
        print(s1)
        print(s2)


# printValue("one","three")
