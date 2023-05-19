n=int(input())
array=list(map(int, input().split()))
hey=sum(array)
result=hey/n
print("{:.2f}".format(result))