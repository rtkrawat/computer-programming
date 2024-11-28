# 20. Find the longest palindromic substring
def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""
    result = s[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(result):
                result = sub
    return result
print(longest_palindromic_substring("babad"))
