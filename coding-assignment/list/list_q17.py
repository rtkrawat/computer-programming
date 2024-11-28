# Given a sorted array arr consisting of 0s and 1s. The task is to find the index (0-based indexing) of the first 1 in the given array.
def firstIndex(self, arr):
        if 1 not in arr:
            return -1
        else:
            return arr.index(1)
