n=int(input())
arr=list(map(int,input().split()))
k=int(input())
sum1=0
for i in range(min(len(arr),k)):
    sum1+=arr[i]
print(sum1)
    