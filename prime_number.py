num = int(input())
is_prime = True
for i in range(2, int(num/2)+1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num > 1:
    print("prime")
else:
    print("not a prime")
