# Given an array arr of even size consisting of positive integers. After sorting the array, find the sum of the product of i-th element from starting and i-th element from last.
def altProduct(self, arr):
        arr.sort()
        p=len(arr)//2
        s=arr[:p]
        k=arr[p:]
        d=k[::-1]
        sum=0
        for i ,j in zip(s,d):
            sum+=int(i)*int(j)
        return sum
