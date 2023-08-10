n = int(input())
arr = list(map(int, input().split()))
even = set()
for num in arr:
    if num % 2 == 0:
        even.add(num)
count = len(even)
print(count)
