# You are given an array of integers, your task is to divide the array into two sub-arrays (left and right) containing half of the array elements. Find the sum of the subarrays and then return the multiply of both the subarrays.

# Note: If the length of the array is odd then the right half will contain one element more than the left half.


def multiply(arr):
    # Code here
    l = 0
    r = 0
    leng = len(arr)
    ln = len(arr) // 2
    if leng % 2 == 0:
        left = arr[0:ln]
        right = arr[ln:]
        for i in range(ln):
            l += left[i]
            r += right[i]

    else:

        left = arr[0:ln]
        right = arr[ln:]

        for i in range(ln):
            l += left[i]
        for j in range(ln + 1):
            r += right[j]

    m = r * l
    return m


x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(multiply(x))
