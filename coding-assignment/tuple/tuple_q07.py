# 7 Find the longest increasing subsequence in a tuple
def longest_increasing_subsequence(t):
    if not t:
        return ()
    lis = [() for _ in range(len(t))]
    lis[0] = (t[0],)
    for i in range(1, len(t)):
        for j in range(i):
            if t[i] > t[j] and len(lis[i]) < len(lis[j]) + 1:
                lis[i] = lis[j] + (t[i],)
        if not lis[i]:
            lis[i] = (t[i],)
    return max(lis, key=len)
print(longest_increasing_subsequence((3, 10, 2, 1, 20)))
