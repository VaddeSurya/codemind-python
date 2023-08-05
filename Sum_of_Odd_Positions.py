n = int(input())
arr = list(map(int, input().split()))
even = 0
for i in range(len(arr)):
    if i % 2 != 0:
        even += arr[i]
print(even)
