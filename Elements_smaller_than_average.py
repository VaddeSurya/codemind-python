n=int(input())
arr=list(map(int,input().split()))
sum1=sum(arr)//len(arr)
count=0
for i in (arr):
    if i<=sum1:
        count+=1
print(count)