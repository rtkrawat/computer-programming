# 14. Count the number of times a substring appears in a string
def count_substring(s, sub):
    count = 0
    start = 0
    while start < len(s):
        pos = s.find(sub, start)
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
    return count
print(count_substring("hello hello", "lo"))
