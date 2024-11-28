# Given a string S which consists of alphabets , numbers and special characters. You need to write a program to split the strings in three different strings S1, S2 and S3 such that the string S1 will contain all the alphabets present in S , the string S2 will contain all the numbers present in S and S3 will contain all special characters present in S.  The strings S1, S2 and S3 should have characters in same order as they appear in input.

def splitString(ob, S): 
        s=''
        n=''
        w=''
        for i in S:
            if ord(i)>=65 and ord(i)<=90:
                s+=i
            elif ord(i)>=97 and ord(i)<=122:
                s+=i
            elif ord(i)>=48 and ord(i)<=57:
                n+=i
            else:
                w+=i
        l=[s,n,w]
        return l
