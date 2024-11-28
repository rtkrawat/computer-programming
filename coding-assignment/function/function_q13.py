# Calculate factorial of a given number N.


def find_fact(n):
    if n == 0 or n == 1:
        return 1
    return n * find_fact(n - 1)


print(find_fact(5))
