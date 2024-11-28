# You are given an integer n. You need to convert all zeroes of n to 5.
def convertFive(self, n):
        if n==0:
            return 5
        else:
            k=0
            while n:
                p=n%10
                if p==0:
                    k=k*10+5
                else:
                    k=k*10+p
                n=n//10
            o=0
            while k:
                l=k%10
                o=o*10+l
                k//=10
            return o
