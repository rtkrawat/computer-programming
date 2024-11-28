#9 Find keys with the highest values in a dictionary
def top_n_keys(d, n):
    return sorted(d, key=d.get, reverse=True)[:n]
print(top_n_keys({"a": 1, "b": 3, "c": 2}, 2))
