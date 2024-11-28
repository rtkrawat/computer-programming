# 19. Decode a Run Length Encoded (RLE) string
def run_length_decoding(s):
    decoding = ""
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        count = ""
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        decoding += char * int(count)
    return decoding
print(run_length_decoding("a2b3c2d1e1"))
