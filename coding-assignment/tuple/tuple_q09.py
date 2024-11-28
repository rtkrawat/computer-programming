# 9 Find all unique elements in a tuple, preserving order
def unique_elements(t):
    seen = set()
    result = []
    for elem in t:
        if elem not in seen:
            seen.add(elem)
            result.append(elem)
    return tuple(result)
print(unique_elements((1, 2, 2, 3, 3, 4)))
