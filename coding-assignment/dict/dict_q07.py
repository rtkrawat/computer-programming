#7 Count the occurrences of each character in a string
def char_occurrences(s):
    from collections import Counter
    return dict(Counter(s))
print(char_occurrences("hello world"))
