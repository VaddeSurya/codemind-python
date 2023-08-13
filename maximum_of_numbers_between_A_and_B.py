N = int(input())
arr = list(map(int, input().split()))
A, B = map(int, input().split())
maxi = -1
for num in arr:
    if A <= num <= B and num > maxi:
        maxi = num
print(maxi)
