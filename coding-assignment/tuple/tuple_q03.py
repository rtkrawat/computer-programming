# 3 Rotate a tuple by k elements to the right
def rotate_tuple_right(t, k):
    k = k % len(t)
    return t[-k:] + t[:-k]
print(rotate_tuple_right((1, 2, 3, 4, 5), 2))
