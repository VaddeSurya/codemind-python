n = int(input())
arr = list(map(int, input().split()))
arr1 = []
total = 0
for i in arr:
    while i > 0:
        total += i % 10
        i //= 10
    arr1.append(total)
    total = 0 
print(sum(arr1))
