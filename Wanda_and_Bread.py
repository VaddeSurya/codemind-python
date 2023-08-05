n,m,k=map(int,input().split())
tot=(n+k-1)//k
if tot<=m:
    print("YES")
else:
    print("NO")