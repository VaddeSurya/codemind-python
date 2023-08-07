n = int(input())
sum1 = 0

while n != 1 and n != 4:
    sum1 = 0
    while n != 0:
        digit = n % 10
        sum1 += digit * digit
        n //= 10
    n = sum1

if n == 1:
    print("True")
else:
    print("False")
