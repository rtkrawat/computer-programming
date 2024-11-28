# Given an array arr of even size, sort the first half of the array in ascending order and the second half in descending order.
def customSort(self, arr):
        p=len(arr)//2
        k=arr[:p]
        k.sort()
        s=arr[p:]
        s.sort()
        d=s[::-1]
        return k+d
