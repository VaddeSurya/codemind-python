n = int(input())
arr = list(map(int, input().split()))
odd = []
sum1 = 0
for i in arr:
    if i % 2 != 0 and i not in odd:
        sum1 += i
        odd.append(i)
print(sum1)
