# Given an array arr, rotate the array by one position in clock-wise direction.
def rotate(self, arr):
    p=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=p
    return arr
