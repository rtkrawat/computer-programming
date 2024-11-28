# Given a number N. You can perform an operation on it multiple times, in which you can change digit 5 to 6 and vice versa.
# You have to return the sum of the maximum number and the minimum number which can be obtained by performing such operations.


def performOperation(n):
    num = str(n)
    max = ""
    min = ""
    for i in num:
        if i == "5":
            max += "6"
        else:
            max += i
    for i in num:
        if i == "6":
            min += "5"
        else:
            min += i

    c = int(max) + int(min)

    return c


print(performOperation(56652))
