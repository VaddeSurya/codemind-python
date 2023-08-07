n=int(input())
sq=n*n
sum1=0
while(sq>0):
    dig=sq%10
    sum1+=dig
    sq//=10
if n==sum1:
    print("Neon Number")
else:
    print("Not Neon Number")
