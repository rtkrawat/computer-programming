#8 Remove keys with None values from a dictionary
def remove_none_values(d):
    return {k: v for k, v in d.items() if v is not None}
print(remove_none_values({"a": 1, "b": None, "c": 3}))
