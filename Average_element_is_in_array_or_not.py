n = int(input())
arr = list(map(int, input().split()))
sum1 = sum(arr)
aver = sum1 // len(arr)
found = False
for num in arr:
    if num == aver:
        found = True
        break
if found:
    print("True")
else:
    print("False")
