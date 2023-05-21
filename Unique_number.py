def unique_number(n):
    digits = set(str(n))
    if len(digits) == len(str(n)):
        return "Unique Number"
    else:
        return "Not Unique Number"
n = int(input())
result = unique_number(n)
print(result)
