# Given a string containing multiple words, count the characters in each word and display them.
def countChars(self,s):
        k=s.split()
        l=[]
        for i in k:
            l.append(len(i))
        return l
            
