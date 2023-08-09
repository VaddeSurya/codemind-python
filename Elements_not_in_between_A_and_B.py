n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
flag=0
arr1=[]
for i in arr:
    if i<a or i>b:
        flag=1
        arr1.append(i)
if flag!=1:
    print(-1)
else:
    print(*arr1)