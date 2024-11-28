# Given a string S, we need to find reciprocal of it. The reciprocal of the letter is found by finding the difference between the position of the letter and the first letter ‘A’. Then decreasing the same number of steps from the last letter ‘Z’. The character that we reach after above steps is reciprocal.
# Reciprocal of Z is A and vice versa because if you reverse the position of the alphabet A will be in the position of Z.
# Similarly, if the letter is a small case then the first letter will be 'a' and the last letter will be 'z'. and the definition of reciprocal remains the same.

def reciprocalString(self, S):
        p=''
        for i in S:
            if ord(i)>=97 and ord(i)<=122:
                k=122-ord(i)
                p+=chr(k+97)
            elif ord(i)>=65 and ord(i)<=90:
                k=90-ord(i)
                p+=chr(k+65)
            else:
                p+=i
        return p
