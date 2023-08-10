n=int(input())
arr=list(map(int,input().split()))
firsthalf=0
secondhalf=0;
hfindex=len(arr)//2
for i in range(hfindex):
    firsthalf+=arr[i]
for i in range(hfindex,len(arr)):
    secondhalf+=arr[i]
print(firsthalf)
print(secondhalf)
