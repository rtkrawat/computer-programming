#2 Find the key with the maximum value in a dictionary
def max_value_key(d):
    return max(d, key=d.get)
print(max_value_key({"a": 1, "b": 3, "c": 2}))
