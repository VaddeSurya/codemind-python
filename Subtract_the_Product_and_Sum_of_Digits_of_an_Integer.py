n = int(input())

digit_product = 1
digit_sum = 0

while n > 0:
    digit = n % 10
    digit_product *= digit
    digit_sum += digit
    n //= 10

result = digit_product - digit_sum
print(result)
