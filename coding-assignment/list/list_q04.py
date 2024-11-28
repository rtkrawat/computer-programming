# Given an array, arr of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found
def thirdLargest(self,arr):
        arr.sort()
        return(arr[-3])
