N = int(input())
arr = list(map(int, input().split()))
unique= set()
for i in arr:
    if i % 2 != 0:
        unique.add(i)
print(len(unique))
