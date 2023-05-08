def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
found = False
for i in range(2, n//2 + 1):
    if n % i == 0:
        if is_prime(i) and is_prime(n//i) and i != n//i:
            print(i, n//i)
            found = True
            break
if not found:
    print("-1")
