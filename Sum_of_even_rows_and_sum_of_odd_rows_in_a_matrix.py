r,c=map(int,input().split())
mat=[]
s=0
s1=0
j=0
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
for i in range(r):
    if i%2==0:
        for j in range (c):
            s=s+mat[i][j]
    else:
        for j in range(c):
            s1=s1+mat[i][j]
print(s,end=" ")
print(s1)