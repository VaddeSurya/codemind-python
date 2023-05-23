def sum(n):
    factors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            factors_sum += i
    return factors_sum
n = int(input())
factors_sum = sum(n)
if factors_sum > n:
    print(True)
else:
    print(False)
