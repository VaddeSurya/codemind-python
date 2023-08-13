n=int(input())
arr=list(map(int,input().split()))
zeros=[]
nonzeros=[]
for i in arr:
    if i==0:
        zeros.append(i)
    else:
        nonzeros.append(i)
res=nonzeros+zeros
print(*res)