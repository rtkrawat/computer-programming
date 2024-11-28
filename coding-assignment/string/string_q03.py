#Given string str of a constant length, print a triangle out of it. The triangle should start with the first character of the string and keep growing downwards by adding one character from the string.
#The spaces on the left side of the triangle should be replaced with a dot character. 
def printTriangleDownwards(self, s):
        for i in range(1,len(s)+1):
            for j in range(len(s)-i):
                print(".",end="")
            for j in range(i):
                print(s[j],end="")
            print()
