# Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern.

"""
Input: 5
Output:
* * * * *
* * * * 
* * * 
* *  
* 
"""


def printTriangle(N):
    for i in range(1, N + 1):
        for j in range(N - i + 1):
            print("*", end=" ")
        print()


printTriangle(5)
