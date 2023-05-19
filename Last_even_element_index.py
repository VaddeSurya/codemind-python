N = int(input())
array = list(map(int, input().split()))
last = None
for i in range(N-1, -1, -1):
    if array[i] % 2 == 0:
        last = i
        break
print(last)

