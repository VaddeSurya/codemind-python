n=int(input())
arr=list(map(int,input().split()))
aver=abs(sum(arr)/len(arr))
print("{:.2f}".format(aver))