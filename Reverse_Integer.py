n=int(input())
rev=0
revNEG=False
if(n<0):
    revNEG=True
    n=abs(n)
while(n!=0):
    dig=n%10
    rev=(rev*10)+dig
    n//=10
if revNEG:
    rev=-rev
print(rev)