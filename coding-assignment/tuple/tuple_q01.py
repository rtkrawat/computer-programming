# 1 Merge two tuples, alternating elements from each
def alternate_merge(t1, t2):
    merged = []
    for i in range(min(len(t1), len(t2))):
        merged.append(t1[i])
        merged.append(t2[i])
    return tuple(merged + list(t1[min(len(t1), len(t2)):]) + list(t2[min(len(t1), len(t2)):]))
print(alternate_merge((1, 2, 3), (4, 5, 6, 7)))
