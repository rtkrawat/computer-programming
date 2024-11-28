# 2 Find the kth smallest element in a tuple
def kth_smallest(t, k):
    return sorted(t)[k-1]
print(kth_smallest((7, 10, 4, 3, 20, 15), 3))
