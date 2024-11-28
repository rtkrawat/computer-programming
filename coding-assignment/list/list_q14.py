# Given an array arr[]. The task is to find the largest element and return it.
def largest(self, arr : list[int]) -> int:
        arr.sort()
        return arr[-1]
        
