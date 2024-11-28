# You have given a non-empty string. This string can consist of lowercase and uppercase english alphabets. Convert the string into an alternating sequence of lowercase and uppercase characters without changing the character at the 0th index.
def getCrazy(self, S):
        k=''
        for i in range(len(S)):
            if S[0].islower():
                if i%2!=0:
                    k+=S[i].upper()
                else:
                    k+=S[i].lower()
            else:
                if i%2!=0:
                    k+=S[i].lower()
                else:
                    k+=S[i].upper()
        return k
