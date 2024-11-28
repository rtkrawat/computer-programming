# Given a positive integer x and an array arr of positive integers. We need to find the farthest index at which x is present. If any occurrence of x doesn't exist, then return -1.
def findIndex(self, arr, x):
        if x not in arr:
            return "-1"
        else:
            p=arr[::-1]
            return len(arr)-p.index(x)
