n=int(input())
arr=list(map(int,input().split()))
arr1=[]
for i in arr:
    if i not in arr1:
        arr1.append(i)
print(sum(arr1))