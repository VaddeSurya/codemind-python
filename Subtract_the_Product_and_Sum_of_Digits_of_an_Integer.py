n = int(input())
sum1 = 0
pro = 1
while n > 0:
    dig = n % 10
    sum1 += dig
    pro *= dig
    n //= 10
result = pro - sum1
print(result)
