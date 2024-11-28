# Given a Sentence S of length N containing only english alphabet characters, your task is to write a program that converts the given sentence to Snake Case sentence. Snake case is the practice of writing compound words or phrases in which the elements are separated with one underscore character (_) and no spaces, and the first letter of each word written in lowercase. For ease keep all the characters in lowercase.
def snakeCase(self, S , n):
        s=''
        for i in S:
            if ord(i)>=65 and ord(i)<=90:
                s+=chr(ord(i)+32)
            elif i==" ":
                s+="_"
            else:
                s+=i
        return s
