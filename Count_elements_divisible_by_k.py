N, K = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for num in arr:
    if num % K == 0:
        count += 1

print(count)
