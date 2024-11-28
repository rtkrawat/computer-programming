#Given a string S, consisting only of english alphabets, replace all the alphabets with the alphabets occuring at the same position when counted in reverse order of alphabets. For example, 'a' would be replaced by 'z', 'b' by 'y', 'c' by 'x' and so on. Any capital letters would be replaced by capital letters only.

def convert(self, s):
        o=''
        for i in s:
            if i.isupper():
                k=ord(i)-65
                o+=chr(90-k)
            elif i.islower():
                k=ord(i)-97
                o+=chr(122-k)
        return o
