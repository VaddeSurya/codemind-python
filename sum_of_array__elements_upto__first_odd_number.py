n=int(input())
arr=list(map(int,input().split()))
sum1=0
for i in range(len(arr)):
    if arr[i]%2!=0:
        break
    sum1+=arr[i]
print(sum1)
        