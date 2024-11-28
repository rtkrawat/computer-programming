# 5 Find all possible pairs of elements in a tuple
def tuple_pairs(t):
    pairs = []
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            pairs.append((t[i], t[j]))
    return pairs
print(tuple_pairs((1, 2, 3, 4)))
