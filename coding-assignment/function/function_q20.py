# Given a string s as input. Delete the characters at odd indices of the string. Return the final string after deletion of characters at odd indices


def delAlternate(s):
    c = ""
    for i in range(len(s)):
        if i % 2 == 0:
            c += s[i]
        else:
            pass
    return c


print(delAlternate("hello"))
