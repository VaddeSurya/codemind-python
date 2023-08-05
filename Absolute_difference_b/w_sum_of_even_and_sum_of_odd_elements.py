n = int(input())
arr = list(map(int, input().split()))
even = 0
odd = 0
for i in arr:
    if i % 2 == 0:
        even += i
    else:
        odd += i
diff = abs(even-odd)
print(diff)
