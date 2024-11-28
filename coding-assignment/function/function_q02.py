# Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern.

# Help Geek to build a star pattern.
"""
Input: 5
Output:
* 
* * 
* * * 
* * * * 
* * * * *
* * * *
* * *
* *
*
"""


def printTriangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()
    for i in range(1, n):
        for j in range(n - i):
            print("*", end=" ")
        print()


printTriangle(5)
