n = int(input())
arr = list(map(int, input().split()))

all_even = True  

for i in arr:
    if i % 2 != 0:
        all_even = False
        break  

if all_even:
    print("True")
else:
    print("False")
