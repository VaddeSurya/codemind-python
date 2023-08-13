n=int(input())
arr=list(map(int,input().split()))
arr1=[]
for i in arr:
    arr1.append(i*i)
print(*sorted(arr1))