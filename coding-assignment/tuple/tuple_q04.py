# 4 Convert a nested tuple into a flat tuple
def flatten_nested_tuple(t):
    if not isinstance(t, tuple):
        return (t,)
    result = ()
    for item in t:
        result += flatten_nested_tuple(item)
    return result
print(flatten_nested_tuple((1, (2, (3, 4)), (5, 6))))
