# 6 Check if a tuple is a permutation of another tuple
def is_permutation(t1, t2):
    return sorted(t1) == sorted(t2)
print(is_permutation((1, 2, 3), (3, 2, 1)))
