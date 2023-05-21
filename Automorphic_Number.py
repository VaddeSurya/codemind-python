n = int(input())
square = n ** 2
num_digits = len(str(n))
last_digits = square % (10 ** num_digits)
if last_digits == n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
