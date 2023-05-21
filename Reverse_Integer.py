def reverse_integer(x):
    negative = False
    if x < 0:
        negative = True
        x = -x
    result = 0
    while x > 0:
        digit = x % 10
        result = result * 10 + digit
        x = x // 10
    if negative:
        result = -result
    if result < -2**31 or result > 2**31 - 1:
        return 0

    return result
print(reverse_integer(int(input())))
