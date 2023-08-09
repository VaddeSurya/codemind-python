n=int(input())
arr=list(map(int,input().split()))
all_bin=False
for i in arr:
    if i==1 or i==0:
        all_bin=True
    else:
        all_bin=False
        break
if all_bin:
    print("True")
else:
    print("False")