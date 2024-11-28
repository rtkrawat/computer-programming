# Given an array arr, swap the kth element from the beginning with the kth element from the end
def swapKth(self, k, arr):
        arr[k-1],arr[-k]=arr[-k],arr[k-1]
        return arr
        
