n = int(input())
sum1 = 0

for i in range(1, n + 1):
    if n % i == 0:
        sum1 += 1

if sum1 == 2:
    print("Prime")
else:
    print("Not Prime")
