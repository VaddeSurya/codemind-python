def sum_of_proper_divisors(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum
n = int(input())
m = int(input())
sum_n = sum_of_proper_divisors(n)
sum_m = sum_of_proper_divisors(m)
if sum_n == m and sum_m == n:
    print("Amicable")
else:
    print("Not Amicable")
