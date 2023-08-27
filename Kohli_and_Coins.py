n=int(input())
c=0
if n%5!=0:
    print('-1')
else:
    r=n%10
    a=r//5
    c=c+((n//10)+a);
    print(c)