# Given a string S  and a character X, the task is to find the last index (0 based indexing) of X in string S. If no index found then the answer will be -1.


def LastIndex(s, p):
    if p in s:
        c = s.rindex(p)
        return c
    else:
        return -1


print(LastIndex("hello", "l"))
