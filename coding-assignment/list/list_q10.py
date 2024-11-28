# Given an array arr[] of integers, change the given array such that at any index i it contains the sum of all elements except itself. Simple way arr[i] should be arr[0] + arr[1] ... arr[i-1] + arr[i+1] ... arr[n-1].
def sumArray(self, arr):
        p=sum(arr)
        for i in range(len(arr)):
            arr[i]=p-arr[i]
        return arr
