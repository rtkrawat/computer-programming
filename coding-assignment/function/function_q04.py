# Given an array arr[] containing positive elements. A and B are two numbers defining a range. The task is to check if the array contains all elements in the given range (inclusive).

# Note: If the array contains all elements in the given range return true otherwise return false.


def check_elements(arr, A, B):
    c = []
    m = True
    for i in range(A, B + 1):
        c.append(i)
    for i in c:
        if i in arr:
            pass
        else:
            m = False
            break
    return m


print(check_elements(([2, 3, 4, 5, 6]), 2, 5))
