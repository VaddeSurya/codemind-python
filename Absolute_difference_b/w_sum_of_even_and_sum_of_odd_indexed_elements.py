n=int(input())
arr=list(map(int,input().split()))
esum=0
eodd=0
for i in range(n):
    if i%2==0:
        esum+=arr[i]
    else:
        eodd+=arr[i]
print(abs(esum-eodd))