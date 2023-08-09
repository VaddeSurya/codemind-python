n=int(input())
arr7=list(map(int,input().split()))
arr=[]
arr2=[]
for i in arr7:
    if i%2!=0:
        arr.append(i)
    else:
        arr2.append(i)
arr3=arr+arr2
print(*arr3)