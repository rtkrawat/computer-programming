# 12. Find the longest substring without repeating characters
def longest_unique_substring(s):
    char_set = set()
    left = 0
    result = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        result = max(result, right - left + 1)
    return result
print(longest_unique_substring("abcabcbb"))
