# Given a string str containing alphanumeric characters. The task is to calculate the sum of all the numbers present in the string.
def findSum(s):
    x=""
    for i in s:
        if((ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90)):
            x+=" "
        else:
            x+=i
    x=x.split()
    c=0
    for i in x:
        c+=int(i)
    return c
