# 10 Find the most common pair of consecutive elements in a tuple
def most_common_consecutive_pair(t):
    from collections import Counter
    pairs = Counter((t[i], t[i + 1]) for i in range(len(t) - 1))
    return pairs.most_common(1)[0][0] if pairs else None
print(most_common_consecutive_pair((1, 2, 3, 2, 1, 2, 3, 2)))
