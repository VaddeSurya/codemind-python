import math
n = int(input())
pronic = False
for i in range(int(math.sqrt(n)) + 1):
    product = i * (i + 1)
    if product == n:
        pronic = True
        break
if pronic:
    print("YES")
else:
    print("NO")
