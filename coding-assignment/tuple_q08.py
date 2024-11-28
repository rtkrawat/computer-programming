# 8 Partition a tuple into k nearly equal parts
def partition_tuple(t, k):
    avg = len(t) / float(k)
    partitions = []
    last = 0.0
    while last < len(t):
        partitions.append(t[int(last):int(last + avg)])
        last += avg
    return partitions
print(partition_tuple((1, 2, 3, 4, 5, 6), 3))
