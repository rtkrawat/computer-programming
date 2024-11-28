# Given two strings S1 and S2 . Return "1" if both strings are anagrams otherwise return "0" .

def areAnagram(ob, S1, S2):
        if sorted(S1)==sorted(S2):
            return "1"
        else:
            return "0"
