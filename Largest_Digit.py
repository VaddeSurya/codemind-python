n=int(input())
lag=0
while(n>0):
    dig=n%10
    if dig>lag:
        lag=dig
    n//=10
print(lag)