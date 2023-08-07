n = int(input())
arr = list(map(int, input().split()))
se = int(input())
found = False
for i in arr:
    if se == i:
        found = True
        break
if found:
    print("True")
else:
    print("False")
