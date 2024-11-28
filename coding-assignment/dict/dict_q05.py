# 5 Find the intersection of two dictionaries
def intersect_dicts(d1, d2):
    return {k: d1[k] for k in d1 if k in d2 and d1[k] == d2[k]}
print(intersect_dicts({"a": 1, "b": 2, "c": 3}, {"b": 2, "c": 4, "d": 3}))
