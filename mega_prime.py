def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_mega_prime(n):
    if not is_prime(n):
        return "Not Mega Prime"
    for digit in str(n):
        if not is_prime(int(digit)):
            return "Not Mega Prime"
    return "Mega Prime"
n=int(input())
print(is_mega_prime(n))