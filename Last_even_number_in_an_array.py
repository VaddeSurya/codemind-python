n=int(input())
array=list(map(int, input().split()))
last=None
for num in array:
    if num%2==0:
        last=num
print(last)
