# 15. Check if a string can be rearranged to form a palindrome
def can_form_palindrome(s):
    from collections import Counter
    count = Counter(s)
    odd_count = sum(1 for val in count.values() if val % 2 != 0)
    return odd_count <= 1
print(can_form_palindrome("carrace"))
