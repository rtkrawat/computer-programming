# 6 Create a dictionary from two lists
def lists_to_dict(keys, values):
    return dict(zip(keys, values))
print(lists_to_dict(["a", "b", "c"], [1, 2, 3]))
