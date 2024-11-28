# 18. Encode a string using Run Length Encoding (RLE)
def run_length_encoding(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        encoding += s[i] + str(count)
        i += 1
    return encoding
print(run_length_encoding("aabbbccde"))
