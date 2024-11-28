# Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.
def PalinArray(arr):
    c=0
    for i in arr:
        if str(i)==str(i)[::-1]:
            pass
        else:
            c+=1
    if c==0:
        return True
    else:
        return False
