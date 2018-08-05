def remove_duplicates(string):
    unique = ''.join(sorted(set(string)))
    removed = len(string) - len(unique)
    return unique, removed


remove_duplicates('aaabbbac') = > ('abc', 5)
remove_duplicates('a') = > ('a', 0)
remove_duplicates('thelexash') = > ('aehlstx', 2)
