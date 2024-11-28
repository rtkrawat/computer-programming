# Given a string str containing only lowercase letters, generate a string with the same letters, but in uppercase.


def to_upper(str):
    c = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            c += chr(ord(i) - 32)
        else:
            c += i
    return c


print(to_upper("hello"))
