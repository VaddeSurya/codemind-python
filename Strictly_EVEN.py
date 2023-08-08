n = int(input())
arr = list(map(int, input().split()))
strictly_even = True
for i, num in enumerate(arr):
    if num % 2 == 0 and i % 2 != 0:
        strictly_even = False
        break

if strictly_even:
    print("True")
else:
    print("False")
