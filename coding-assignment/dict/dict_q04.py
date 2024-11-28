#4 Group elements of a list by their frequency
def group_by_frequency(lst):
    from collections import defaultdict
    freq_dict = defaultdict(list)
    for item in lst:
        freq_dict[lst.count(item)].append(item)
    return dict(freq_dict)
print(group_by_frequency([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
