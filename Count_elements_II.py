m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
common=set(a)^set(b)
count=len(common)
print(count)