n=int(input())
sum1=0
pro=1
while(n>0):
    dig=n%10;
    sum1+=dig;
    pro*=dig;
    n//=10
if(sum1==pro):
    print("Spy Number")
else:
    print("Not Spy Number")