#You are given a string S, convert it into a magical string.
#A string can be made into a magical string if the alphabets are swapped in the given manner: a->z or z->a, b->y or y->b, and so on. 
def magicalString (ob,S):
        p=''
        for i in S:
            k=122-ord(i) 
            p+=chr(97+k)
        return p
