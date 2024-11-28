# write a program to count frequency of elements in list and return in the form of a dictionary.


def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq


print(count_frequency(["a", "b", "a", "c", "b", "a"]))
